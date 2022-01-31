from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q 
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView
from .models import *   #call class object from db
from .form_control import Chk_Form
# Create your views here.
#V

# index
# class IndexView(generic.ListView):
#     template_name = 'index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Blogs.objects.order_by('-time_created')[:]

def show_index(request):
    blog_lists = Blogs.objects.all().order_by("-time_created")
    # test = [(item.blog_hashtags) for item in blog_lists]
    # print("test =",test, "->", type(test))
    # for tag_k,tag_v in enumerate(test):
    #     print("tag_K =",tag_k)
    #     print("tag_V =",tag_v)

    base_content = {
    'web_title': 'Home page.',
    'blog_lists': blog_lists,
    }

    return render(request, 'index.html', base_content)

# create blogs
def show_create_blogs(request):
    if request.method == 'POST' and request.POST.get('create_blogs'):
        # get_name = request.POST.get('create_blogs')
        # get_post = request.POST
        # print("request.POST.get('create_blogs') =",get_name)
        # print('request.POST =',get_post)
        chk_from = Chk_Form(request.POST)
        if chk_from.is_valid():
            print("ไม่มีค่าว่าง")
            chk_from.save()
            print("บันทึกแล้ว")
            messages.success(request, "Create blogs success.", extra_tags='text-success')
            return redirect('/')
        else:
            print("มีค่าว่าง")
            base_content = {
            'web_title': 'Create page.',
            'form': chk_from,
            }
            return render(request, 'create_blogs.html', base_content)
    else:
        print("get link")
        # ary_list = ['value1','value2','']
        # ary_list_index = []
        # for i in range(len(ary_list)):
        #     ary_list_index.append(i)
        # print("new_ary_list_index =", ary_list_index, "->", type(ary_list_index))
        # print("ary_list =", ary_list, "->", type(ary_list))

        # new_ary_list = enumerate(ary_list)
        # print("new_ary_list =", new_ary_list, "->", type(new_ary_list))

        # for key in new_ary_list:
        #     print("key =", key)
        # print("ary_list[1] =", ary_list[1], "->", type(ary_list))
        chk_from = Chk_Form(None)
        base_content = {
        'web_title': 'Create page.',
        'form': chk_from,
        # 'ary_list': ary_list,
        # 'ary_list_index': ary_list_index,
        # 'new_ary_list': new_ary_list,
        }
        # print(chk_from['blog_type'].html_initial_id)
        return render(request, 'create_blogs.html', base_content)

# edit blogs
def show_edit_blogs(request, post_id=None):
    get_data_blog = get_object_or_404(Blogs, id=post_id)    
    chk_update = Chk_Form(request.POST or None, request.FILES or None, instance=get_data_blog)

    if request.method == 'POST':
        # print("get_POST =",request.POST)
        if chk_update.is_valid():
            print("ไม่มีค่าว่าง")
            instance = chk_update.save(commit=False)
            instance.save()
            messages.success(request, "Update blogs success.", extra_tags='text-success')
            return redirect('/')
        else:
            print("มีค่าว่าง")

    base_content = {
        'web_title': 'Edit page.',
        'blog_lists': get_data_blog,
        'form': chk_update,
    }
    return render(request, 'edit_blogs.html', base_content)

# delete blogs
def show_delete_blogs(request, post_id):
    get_data_blog = get_object_or_404(Blogs, id=post_id)
    get_data_blog.delete()
    messages.success(request, "Delete blogs success.", extra_tags='text-success')
    return redirect('/')

# search blogs
def show_query_search(request):
    if request.method == 'GET' and request.GET.get('search_txt'):
        query_search = request.GET.get('search_txt', None)

        object_list = Blogs.objects.filter(Q(title__icontains=query_search) | Q(content__icontains=query_search)).order_by("-time_created")
        print("object_list = ",object_list)
        # if object_list.count() == 0:
        #     print("ว่างเปล่า")
        # else:
        #     print("ไม่ว่างเปล่า")
        base_content = {
            'web_title': 'Home page.',
            'blog_lists': object_list,
        }
        return render(request, 'index.html', base_content)
    else:
        return redirect('/')

def show_query_tags(request, tag_name=None):
    if request.method == 'GET':
        object_list = Blogs.objects.filter(Q(blog_hashtags__icontains=tag_name)).order_by("-time_created")
        base_content = {
            'web_title': 'Home page.',
            'blog_lists': object_list,
        }
        return render(request, 'index.html', base_content)
        # return HttpResponse("tag_name = " + tag_name)
    else:
        return redirect('/')

# register
def show_user_register(request):
    if request.method == 'POST' and request.POST.get('Create_Account'):
        get_username = request.POST.get('username_txt')
        get_password = request.POST.get('userpassword_txt')
        get_re_password = request.POST.get('chk_userpassword_txt')
        get_firstname = request.POST.get('firstname_txt')
        get_lastname = request.POST.get('lastname_txt')
        get_email = request.POST.get('useremail_txt')
        
        if get_re_password == get_password:
            if User.objects.filter(username = get_username).exists():
                messages.warning(request, "This 'username' already has a use.", extra_tags='text-warning')
                return redirect('/register')
            else:
                insert_data = User.objects.create_user(
                    username=get_username,
                    password=get_password,
                    email=get_email,
                    first_name=get_firstname,
                    last_name=get_lastname,
                )
                insert_data.save()
                messages.success(request, "Create success.", extra_tags='text-success')
                return redirect('/')
        else:
            messages.warning(request, "Your 'password' is wrong.", extra_tags='text-warning')
            return redirect('/register')
        
    else:
        base_content = {
        'web_title': 'Register page.',
        }
        return render(request, 'user_register.html', base_content)

# test_chk_register
def chk_username_register(request):
    get_username = request.GET.get('username_txt')
    response = {
    'is_taken': User.objects.filter(username=get_username).exists()
    }
    return JsonResponse(response)

# login
def show_user_login(request, show_popup=None):
    if request.method == 'POST' and request.POST.get('Login'):
        print('get POST Submit')
        get_username = request.POST.get('username_txt')
        get_password = request.POST.get('password_txt')
        print("username: ",get_username," password: ",get_password)
        chk_login = authenticate(request, username=get_username, password=get_password)
        if chk_login is not None:
            login(request, chk_login)
            request.session['username'] = chk_login.username
            messages.success(request, "Login success.", extra_tags='text-success')
            return redirect('/')

        else:
            messages.warning(request, "User not found.", extra_tags='text-warning')
            return redirect('/')
    # elif request.method == 'GET' and request.GET.get('S'):
    #     if request.GET.get('S') == "popup_login":
    #         show = request.GET.get('S')
    #         # return redirect(request.GET.get('S'))
    #         return HttpResponse("get S = " + show)
    #     else:
    #         show = request.GET['S']
    #         return HttpResponse("Not get S = {}".format(show))
        # return redirect(request.GET.get('S')) 
    elif request.method == 'GET' and show_popup == 'show-popup':
        status = show_popup
        print("value =",status)
        request.session['get_popup'] = status
        return redirect('/')
    elif request.method == 'GET' and show_popup == 'non-popup':
        status = show_popup
        print("value =",status)
        del request.session['get_popup']
        return redirect('/')
    else:
        return redirect('/')

# logout
def show_user_logout(request):
    logout(request)
    # del request.session['username']
    messages.success(request, "Logout success.", extra_tags='text-success')
    return redirect('/')









# def show_pagination(request):
#     get_count_blogs = Blogs.objects.all().count
#     page = 1
#     want_show = 4
#     get_list = Blogs.objects.all()
#     first_blog = get_list.first()
#     last_blog = get_list.last()

#     return render(request, 'test_page.html',{'sum_blogs': get_count_blogs, 'list': get_list, 'want_show': want_show,
#     'first_blog': first_blog, 'last_blog': last_blog})


