from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import *
#route URLs

app_name = 'blogs'
urlpatterns = [
    path('', show_index, name='home'),
    path('create/', show_create_blogs, name='create_blogs'),
    path('register/', show_user_register, name='user_register'),
    path('chk_username_register/', chk_username_register, name='chk_username'),
    path('login/', show_user_login, name='user_login'),
    path('login/<slug:show_popup>', show_user_login, name='link_login'),  
    path('logout/', show_user_logout, name='user_logout'),
    path('edit/<int:post_id>/', show_edit_blogs, name='edit_blogs'), 
    path('delete/<int:post_id>/', show_delete_blogs, name='delete_blogs'),
    path('search/', show_query_search, name='search_blogs'),  
    path('search/tag/<str:tag_name>', show_query_tags, name='tag_blogs'),  
    # path('show_pagination', show_pagination, name='show_pagination'),
] 
