from django.contrib import admin
from .models import *
from .form_control import Chk_Form
# Register your models here.

# class PostModelAdmin(admin.ModelAdmin):
#     form = Chk_Form
#     list_display = ['title','content','create_by','time_created','time_updated']
#     search_fields = ['title','content']
#     list_editable = ['create_by']
#     list_filter = ['create_by','time_created']
#     list_display_links = ['title']
# admin.site.register(Blogs, PostModelAdmin)

# class PostBlogTypeAdmin(admin.ModelAdmin):
#     search_fields = ['type_name']
# admin.site.register(BlogType, PostBlogTypeAdmin)
class BlogTagsAdmin(admin.ModelAdmin):
    list_display = ['id','tag_name']
    list_display_links = ['tag_name']

class BlogAdmin(admin.ModelAdmin):
    form = Chk_Form
    list_display = ['id','title','content','create_by','blog_type','blog_hashtags','time_created','time_updated']
    search_fields = ['title','content']
    list_editable = ['create_by','blog_type','blog_hashtags']
    list_filter = ['create_by','time_created']
    list_display_links = ['title']

admin.site.register(BlogTags,BlogTagsAdmin)
admin.site.register(Blogs, BlogAdmin)
admin.site.register(BlogType)

