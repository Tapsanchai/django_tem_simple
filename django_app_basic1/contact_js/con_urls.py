from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

# from .bjs_views import LoginView, ShowIndex,ShowDataView,DeleteBlog,CreateBlog,UpdateBlog,LoginView,LogoutView,RegisterView
from .con_views_main_contact import *
from .con_views_sub_alternate_email import *
from .con_views_sub_alternate_phone import *
from .con_views_sub_personal_address import *
#route URLs

app_name = 'contact_js'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('render/',ShowMainDataView.as_view(), name='render_query'),
    path('create_full_contact/', CreateContactView.as_view(), name='create_full_contact'),
    path('update_full_contact/<int:id>/', UpdateContactView.as_view(), name='update_full_contact'),
    path('delete_full_contact/<int:id>/', DeleteContactView.as_view(), name='delete_full_contact'),

    path('create_or_update_alternate_email/show_list/', CreateOrUpdateAlternateEmailView.as_view(), name='list_alternate_email'),
    path('create_or_update_alternate_email/create/<int:id>/', CreateOrUpdateAlternateEmailView.as_view(), name='create_alternate_email'),
    path('create_or_update_alternate_email/update/<int:id>/', CreateOrUpdateAlternateEmailView.as_view(), name='update_alternate_email'),
    path('delete_alternate_email/<int:id>/', DeleteAlternateEmailView.as_view(), name='delete_alternate_email'),

    path('create_or_update_alternate_phone/show_list/', CreateOrUpdateAlternatePhoneView.as_view(), name='list_alternate_phone'),
    path('create_or_update_alternate_phone/create/<int:id>/', CreateOrUpdateAlternatePhoneView.as_view(), name='create_alternate_phone'),
    path('create_or_update_alternate_phone/update/<int:id>/', CreateOrUpdateAlternatePhoneView.as_view(), name='update_alternate_phone'),
    path('delete_alternate_phone/<int:id>/', DeleteAlternatePhoneView.as_view(), name='delete_alternate_phone'),

    path('create_or_update_personal_address/show_list/', CreateOrUpdatePersonalAddressView.as_view(), name='list_personal_address'),
    path('create_or_update_personal_address/create/<int:id>/', CreateOrUpdatePersonalAddressView.as_view(), name='create_personal_address'),
    path('create_or_update_personal_address/update/<int:id>/', CreateOrUpdatePersonalAddressView.as_view(), name='update_personal_address'),
    path('delete_personal_address/<int:id>/', DeletePersonalAddressView.as_view(), name='delete_personal_address'),

] 
