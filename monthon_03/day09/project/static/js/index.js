// 外部js文件
$(function () {
    // 当页面元素加载完成之后执行的JS代码
    // alert('外部JS文件加载完成');
    // // 测试外部数据加载
    console.log(blogData);
    console.log(faderData);
    // 使用faderData在页面加载所有的轮播图

    // 声明本地图片路径
    // 图片路径通常随着项目的位置发生变化 对于路径而言尽量不要写死图片路径 通常采用地址+图片名的方式拼接路径 这样项目位置改变只需要改变图片地址 不需要修改代码
    // var BASE_URL = 'http://127.0.0.1:8000/'
    var BASE_URL = '../static/images/';
    var html = '';
    // 遍历faderData 生成三个li标签拼接到字符串html中
    // 打印字符串
    // <li class="slide">
    //     <a href="#">
    //         <img src="../static/images/banner01.jpg" alt="banner1">
    //         <span class="imginfo">
    //             爬虫微课5小时 Python 学习路线!
    //         </span>
    //     </a>
    // </li>
    $.each(faderData,function(i,o){
        html += '<li class="slide">';
        html += '<a href="#">'
        html += `<img src="${BASE_URL+o.img_url}" alt="">`
        html += '<span class="imginfo">';
        html += o.img_info;
        html += '</span></a></li>'
    })
    console.log(html);
    // 将拼接好的字符串作为兄弟元素添加到fader_controls前
    $('.fader_controls').before(html);

    // jquery-->easyfader-->index.js
    // 调用jQuery.easyfader.min.js提供的函数 实现轮播功能
    $('.fader').easyFader();

})