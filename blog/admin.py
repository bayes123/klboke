from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):   #让后台的信息更加具体
    list_display=['title','created_time','modified_time','category','author']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)