from django.db import models


# Create your models here.
class Book(models.Model):

    title = models.CharField("书名", max_length=50, unique=True)
    price = models.DecimalField('定价', max_digits=5, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=5, decimal_places=2, default=0.0)
    pub = models.CharField('出版社', max_length=50, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    def __str__(self):
        return "书名:    %s, 出版社: %s, 定价: %s,零售价:%s" % (self.title, self.pub, self.price,self.market_price)

class Person(models.Model):
    name = models.CharField("姓名", max_length=50, unique=True)
    age = models.DecimalField('年龄', max_digits=5, decimal_places=2)
    mailbox = models.CharField("邮箱", max_length=50, unique=True)

    class Meta:
        db_table = 'book'
        verbose_name ='图书'
        verbose_name_plural ='图书'



class Author(models.Model):
    name = models.CharField('姓名', max_length=20)
    age = models.IntegerField('年龄', default=18)
    email = models.EmailField('邮箱', null=True)
