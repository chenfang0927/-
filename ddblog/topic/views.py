from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from tools.logging_dec import logging_check, get_user_by_request
import json
from .models import Topic
from user.models import UserProfile


# Create your views here.
class TopicViews(View):
    @method_decorator(logging_check)
    def post(self, request, author_id):
        # 作者，就是登录用户
        author = request.myuser
        # 从前端传递的json字符串串
        json_str = request.body
        # 序列化为json对象
        json_obj = json.loads(json_str)
        # 博客内容
        content = json_obj['content']
        # 不带格式的内容，方便剪切
        content_text = json_obj['content_text']
        # 通过剪切保存到博客简介中
        introduce = content_text[:20]
        # 文章标题
        title = json_obj['title']
        # 文章权限
        limit = json_obj['limit']
        if limit not in ['public', 'private']:
            result = {'code': 10300, 'error': 'limit error'}
            return JsonResponse(result)
        # 文章分类
        category = json_obj['category']
        if category not in ['tec', 'no-tec']:
            result = {'code': 10301, 'error': 'category error'}
            return JsonResponse(result)
        # 数据入库
        Topic.objects.create(title=title, content=content,
                             limit=limit, category=category,
                             introduce=introduce, user_profile=author)
        # 返回
        return JsonResponse({'code': 200, 'username': author.username})

    def make_topics_res(self,author,author_topics):
        topics_res=[]
        for topic in author_topics:
            d={}
            d['id']=topic.id
            d['title']=topic.title
            d['category']=topic.category
            d['introduce']=topic.introduce
            d['created_time']=topic.create_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author']=author.nickname
            topics_res.append(d)
        res ={'code':200,'data':{}}
        res['data']['topics']=topics_res
        res['data']['nickname']=author.nickname

        return res

    def get(self,request,author_id):
        try:
            author = UserProfile.objects.get(username=author_id)
        except Exception as e:
            result={'code':10305,'error':'author_id is error'}
            return JsonResponse(result)
        #访问者是游客还是自己

        visitor_name = get_user_by_request(request)



        category=request.GET.get('category')
        filter_category =False
        if category in ['tec','no-tec']:
            filter_category=True

        if visitor_name==author_id:
            if filter_category:
                author_topics = Topic.objects.filter(user_profile_id=author_id)


            else:
                author_topics = Topic.objects.filter(user_profile_id=author_id,
                                                 limit='public')

        res= self.make_topics_res(author,author_topics)
        return  JsonResponse(res)


