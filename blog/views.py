# from django.http import HttpResponse
# from django.shortcuts import render
# # Create your views here.
#
#
# def index(request):
#     """
#     return HttpResponse("欢迎访问我的博客首页!我是柯琳琳~")
#     """
# #这里我们不再是直接把字符串传给 HttpResponse 了，而是调用 Django 提供的 render 函数。
#     # 这个函数根据我们传入的参数来构造 HttpResponse。
#     return render(request,'blog/index.html',context={'title':'我的博客首页','welcome':'欢迎访问我的博客首页'})
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return render(request, 'blog/index.html', context={
#                       'title': '我的博客首页',
#                       'welcome': '欢迎访问我的博客首页'
#                   })
import markdown
from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from .models import Post,Category


def index(request):   #post_list是一个QuerySet(类似于一个列表的数据结构)
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    #记得在顶部导入CommentForm
    form=CommentForm()
    #获取这篇post下的全部评论
    comment_list=post.comment_set.all()
    #将文章、表单、以及文章下的评论列表作为模板变量传给detail.html模板，以便渲染相应数据
    context={
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'blog/detail.html', context=context)

#主页视图函数中我们通过 Post.objects.all() 获取全部文章，而在我们的归档和分类视图中，我们不再使用 all 方法获取全部文章，而是使用 filter 来根据条件过滤。先来看归档视图：
def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

