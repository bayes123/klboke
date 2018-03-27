from django.db import models

# Create your models here.
from django.db import models
from django.utils.six import python_2_unicode_compatible

#python_2_unicode_compatible 装饰器用于兼容Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    url=models.URLField(blank=True)
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)#同时注意我们为 DateTimeField 传递了一个 auto_now_add=True 的参数值。auto_now_add 的作用是，当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间。created_time 记录用户发表评论的时间，我们肯定不希望用户在发表评论时还得自己手动填写评论发表时间，这个时间应该自动生成。
    post=models.ForeignKey('blog.Post') #这个评论是关联到某篇文章（Post）的，由于一个评论只能属于一篇文章，一篇文章可以有多个评论，是一对多的关系，因此这里我们使用了 ForeignKey

    def _str_(self):
        return self.text[:20]