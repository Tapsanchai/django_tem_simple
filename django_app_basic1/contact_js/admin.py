from django.contrib import admin
from .con_models import GendersModel, NationalityModel, ContactModel, PhoneTypeModel, AlternatePhoneModel, EmailTypeModel, AlternateEmailModel, PersonalAddressModel, TestCheckboxModel
from .con_contact_form_control import CheckFormCreateContact
from .con_alternate_e_form_control import CheckFormCreateAlternateEmail
from .con_alternate_p_form_control import CheckFormCreateAlternatePhone
from .con_personal_a_form_control import CheckFormCreatePersonalAddress
from .con_testchkbox_control import CheckFormCheckbox
# Register your models here.


class GendersAdmin(admin.ModelAdmin):
    list_display = ['id', 'genders_title']
    list_display_links = ['genders_title']
admin.site.register(GendersModel, GendersAdmin)


class NationalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'nationality_title']
    list_display_links = ['nationality_title']
admin.site.register(NationalityModel, NationalityAdmin)


class ContactAdmin(admin.ModelAdmin):
    form = CheckFormCreateContact
    list_display = ['contact_id', 'hn', 'title_th', 'f_name_th', 'l_name_th',
                    'date_of_birth', 'gender', 'nationality', 'time_updated']
    # list_editable = ['title_th','f_name_th','l_name_th','date_of_birth','gender','nationality']
    list_display_links = ['hn']
    list_filter = ['gender', 'nationality']
    search_fields = ['hn']
admin.site.register(ContactModel, ContactAdmin)


class PhoneTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_title']
    list_display_links = ['type_title']
admin.site.register(PhoneTypeModel, PhoneTypeAdmin)


class AlternatePhoneAdmin(admin.ModelAdmin):
    form = CheckFormCreateAlternatePhone
    list_display = ['id', 'alternate_phone', 'contact_by',
                    'phone_type', 'description', 'primary_status']
    list_display_links = ['alternate_phone']
    list_filter = ['phone_type', 'contact_by']
    search_fields = ['alternate_phone', 'contact_by', 'primary_status']
admin.site.register(AlternatePhoneModel, AlternatePhoneAdmin)


class EmailTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_title']
    list_display_links = ['type_title']
admin.site.register(EmailTypeModel, EmailTypeAdmin)


class AlternateEmailAdmin(admin.ModelAdmin):
    form = CheckFormCreateAlternateEmail
    list_display = ['id', 'alternate_email', 'contact_by',
                    'email_type', 'description', 'primary_status']
    list_display_links = ['alternate_email']
    list_filter = ['email_type', 'contact_by', 'primary_status']
    search_fields = ['alternate_email', 'contact_by']
    # list_editable = ['primary_status']
admin.site.register(AlternateEmailModel, AlternateEmailAdmin)


class PersonalAddressAdmin(admin.ModelAdmin):
    form = CheckFormCreatePersonalAddress
    list_display = ['id', 'address_1', 'contact_by', 'building', 'district',
                    'city', 'province', 'zipcode', 'primary_status', 'alignment_status']
    list_display_links = ['address_1']
    list_filter = ['province', 'contact_by', 'primary_status']
    search_fields = ['address_1', 'contact_by']
admin.site.register(PersonalAddressModel, PersonalAddressAdmin)

class TestCheckboxAdmin(admin.ModelAdmin):
    form = CheckFormCheckbox
    list_display = ['chk_id', 'chk_name']
    list_display_links = ['chk_name']

admin.site.register(TestCheckboxModel, TestCheckboxAdmin)