#模板标签

#最新文章模板标签  (先写好函数，然后将函数注册为模板标签即可)
from django import template
from ..models import Post,Category

register=template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()