from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .bjs_views import LoginView, ShowIndex,ShowDataView,DeleteBlog,CreateBlog,UpdateBlog,LoginView,LogoutView,RegisterView
#route URLs

app_name = 'blog_js'
urlpatterns = [
    path('',ShowIndex.as_view(), name='index'),
    path('render_blogs/',ShowDataView.as_view(), name='show_data'),
    path('delete_blog/',DeleteBlog.as_view(), name='delete_blog'),
    path('create_blog/',CreateBlog.as_view(), name='create_blog'),
    path('update_blog/<int:pk>/',UpdateBlog.as_view(), name='update_blog'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
] 
