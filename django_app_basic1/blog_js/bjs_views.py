from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, F, Func, Value, CharField
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView
import json
import json_tricks


from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

from .bjs_models import *  # call class object from db
from .bjs_form_control import Chk_Form
from .bjs_form_login_control import ChkLoginForm
from .bjs_form_register import ChkRegisForm

# Create your views here.


class ShowIndex(ListView):
    def get(self, request, *args, **kwargs):
        base_context = {
            'page_title': 'Index Page',
            'some_data': 'Hello Index.'
        }
        return render(request, 'bjs_index.html', base_context)
        # return HttpResponse("Hello Index.")

    def post(self, request, *args, **kwargs):
        pass


class ShowDataView(ListView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('txt'):
            query_search = request.GET.get('txt')
            print("query_search =", query_search, "-->", type(query_search))
            # chk_value = print('value = none || empty') if query_search is None or query_search == "" else print('value = NOT none || empty')
            # convert_json_str = json.loads(query_search)
            # print("convert_json_str =",convert_json_str, "-->", type(convert_json_str))

            object_list = JS_Blogs.objects.filter(Q(title__icontains=query_search) | Q(content__icontains=query_search)).values("id", "title", "content", "create_by", "time_updated", "blog_hashtags",).annotate(
                blog_type=F("blog_type__type_name")).order_by("-time_created")
            print("object_list = ", object_list)
            context = {
                'data': list(object_list),
            }
            return JsonResponse(context)

        elif request.GET.get('id'):
            query_search = request.GET.get('id')
            print("query_search =", query_search, "-->", type(query_search))
            # chk_value = print('value = none || empty') if query_search is None or query_search == "" else print('value = NOT none || empty')
            # convert_json_str = json.loads(query_search)
            # print("convert_json_str =",convert_json_str, "-->", type(convert_json_str))

            object_list = JS_Blogs.objects.filter(Q(id=query_search)).values("id", "title", "content", "create_by", "time_updated", "blog_hashtags",).annotate(
                blog_type=F("blog_type__type_name")).order_by("-time_created")
            print("object_list = ", object_list)
            context = {
                'data': list(object_list),
            }
            return JsonResponse(context)

        elif request.GET.get('tag'):
            query_search = request.GET.get('tag')
            print("query_search =", query_search, "-->", type(query_search))
            object_list = JS_Blogs.objects.filter(Q(blog_hashtags__icontains=query_search)).values("id", "title", "content", "create_by", "time_updated", "blog_hashtags",).annotate(
                blog_type=F("blog_type__type_name")).order_by("-time_created")
            print("object_list = ", object_list)
            context = {
                'data': list(object_list),
            }
            return JsonResponse(context)

        else:
            all_object_list = JS_Blogs.objects.values("id", "title", "content", "create_by", "time_updated", "blog_hashtags",).annotate(
                blog_type=F("blog_type__type_name")).order_by("-time_created")
            print("all_object_list = ", all_object_list)
            convert_datetime = json.dumps(list(all_object_list) ,indent=4, sort_keys=True, default=str)
            # convert_datetime2 = json_tricks.dumps(list(all_object_list))
            # print("convert_datetime = ", convert_datetime)
            # print("convert_datetime2 = ", convert_datetime2)
            context = {
                'data': convert_datetime
            }

            return JsonResponse(context)


class CreateBlog(ListView):
    def get(self, request, *args, **kwargs):
        Blog_Form = Chk_Form(None)
        base_context = {
            'page_title': 'Create Page',
            'some_data': 'Hello Create_Blogs.',
            'form': Blog_Form
        }
        return render(request, 'bjs_create_blogs.html', base_context)

    def post(self, request, *args, **kwargs):
        get_data_blog = json.loads(request.POST.get('data'))
        print('get_data_blog =', get_data_blog, '-->', type(get_data_blog))

        chk_form = Chk_Form(get_data_blog)
        if chk_form.is_valid():
            print("Status =", True)
            instance = chk_form.save(commit=False)
            instance.save()
            messages.success(
                self.request, 'Create Blogs Successfully', extra_tags='text-success')
            # return redirect("/")
            # return redirect(reverse('blog_js:index'))
            context = {
                'data': get_data_blog,
                'url': reverse('blog_js:index', args=(self.request))
            }
            return JsonResponse(context)
        else:
            print("Status =", False)
            messages_error = chk_form.errors.get_json_data(escape_html=True)

            context = {
                'data': None,
                'messages_error': messages_error
            }
            return JsonResponse(context)


class DeleteBlog(ListView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('id'):
            get_id = request.GET.get('id')
            get_data_blog = get_object_or_404(JS_Blogs, id=get_id)
            if get_data_blog:
                get_data_blog.delete()
                push_message = 'Delete Successfully.'
                messages.success(
                    self.request, 'Delete Successfully', extra_tags='text-success')
            else:
                push_message = 'Delete Failed.'
                messages.warning(self.request, 'Delete Failed',
                                 extra_tags='text-warning')
            context = {
                'data': push_message
            }
            return JsonResponse(context)
        else:
            context = {
                'data': 'Request Method ERROR!!'
            }
            return JsonResponse(context)


class UpdateBlog(ListView):
    def get(self, request, pk, *args, **kwargs):
        get_data_blog = get_object_or_404(JS_Blogs, id=pk)
        if get_data_blog:
            Blog_Form = Chk_Form(None)
            base_context = {
                'page_title': 'Update Page',
                'blog_data': get_data_blog,
                'form': Blog_Form
            }
            return render(request, 'bjs_update_blogs.html', base_context)
        else:
            return HttpResponse('fuck...')

    def post(self, request, pk, *args, **kwargs):
        get_data_blog = json.loads(request.POST.get('data'))
        get_id = pk
        get_blog = JS_Blogs.objects.get(id=get_id)
        print('blog_id =', get_id)
        print('get_data_blog =', get_data_blog, '-->', type(get_data_blog))

        Chk_Blog_Form = Chk_Form(get_data_blog, instance=get_blog)
        if Chk_Blog_Form.is_valid():
            print("Status = ", True)
            Instance = Chk_Blog_Form.save(commit=False)
            Instance.save()
            messages.success(
                self.request, 'Update Blogs Successfully', extra_tags='text-success')
            context = {
                'data': get_data_blog,
                'url': reverse('blog_js:index', args=(self.request))
            }
            return JsonResponse(context)
        else:
            print("Status = ", False)
            messages_error = [{k: [v[0]]}
                              for k, v in Chk_Blog_Form.errors.items()]
            context = {
                'data': None,
                'messages_error': messages_error
            }

            return JsonResponse(context)


class LoginView(ListView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        get_user_form = json.loads(request.POST.get('data'))
        print('get_user_form =', get_user_form, '-->', type(get_user_form))

        chk_login = ChkLoginForm(get_user_form or None)
        if chk_login.is_valid():
            print("Status = ", True)
            get_username = chk_login.cleaned_data.get('username')
            get_password = chk_login.cleaned_data.get('password')
            chk_real_account = authenticate(
                username=get_username, password=get_password)
            login(request, chk_real_account)
            request.session['username'] = get_username
            messages.success(request, "Login success.",
                             extra_tags='text-success')
            context = {
                'data': list(get_user_form),
                'url': reverse('blog_js:index', args=(self.request))
            }
            return JsonResponse(context)

        else:
            print("Status = ", False)
            messages_error = chk_login.errors.get_json_data(escape_html=True)       
            # messages_error2 = json.loads(chk_login.errors.as_json())
            # messages_error = [{k: [v[0]]}
            #                   for k, v in chk_login.errors.items()]
            context = {
                'data': None,
                'messages_error': messages_error,
                # 'messages_error2': messages_error2,
            }
            return JsonResponse(context)


class LogoutView(ListView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Logout success.", extra_tags='text-success')
        context = {
            'data': None,
            'url': reverse('blog_js:index', args=(self.request))
        }
        return JsonResponse(context)


class RegisterView(ListView):
    def get(self, request, *args, **kwargs):
        base_context = {
            'page_title': 'Register Page',
            'some_data': 'Hello Register.'
        }
        return render(request, 'bjs_register_member.html', base_context)

    def post(self, request, *args, **kwargs):
        get_regis_form = json.loads(request.POST.get('data'))
        print('get_user_form =', get_regis_form, '-->', type(get_regis_form))

        chk_form_regis = ChkRegisForm(get_regis_form or None)
        if chk_form_regis.is_valid():
            print("Status = ", True)
            insert_data = User.objects.create_user(
                username=chk_form_regis.cleaned_data.get('username'),
                password=chk_form_regis.cleaned_data.get('password'),
                email=chk_form_regis.cleaned_data.get('email'),
                first_name=chk_form_regis.cleaned_data.get('first_name'),
                last_name=chk_form_regis.cleaned_data.get('last_name'),
            )
            insert_data.save()
            print('create_user successfully') if insert_data else print(
                'create_user failed')
            messages.success(request, "register member success.",
                             extra_tags='text-success')
            context = {
                'data': None,
                'url': reverse('blog_js:index', args=(self.request))
            }
            return JsonResponse(context)
        else:
            print("Status = ", False)
            messages_error = chk_form_regis.errors.get_json_data(escape_html=True)    
            context = {
                'data': list(get_regis_form),
                'messages_error': messages_error
            }
            return JsonResponse(context)
