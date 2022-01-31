from django.contrib import admin
from .bjs_models import JS_BlogType, JS_BlogTags, JS_Blogs
# Register your models here.

class JSBlogTagsAdmin(admin.ModelAdmin):
    list_display = ['id','tag_name']
    list_display_links = ['tag_name']
admin.site.register(JS_BlogTags, JSBlogTagsAdmin)

class JSBlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id','type_name']
    list_display_links = ['type_name']
admin.site.register(JS_BlogType, JSBlogTypeAdmin)

class JSBlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','create_by','blog_type','blog_hashtags','time_created','time_updated']
    search_fields = ['title','content']
    list_editable = ['create_by','blog_type','blog_hashtags']
    list_filter = ['create_by','time_created']
    list_display_links = ['title']
admin.site.register(JS_Blogs, JSBlogAdmin)