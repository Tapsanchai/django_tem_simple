from django.db import models
from django.db import transaction
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
# import phonenumbers
# from django.contrib.auth.models import User
# from django.conf import settings
# from django.forms.widgets import NullBooleanSelect, SelectMultiple, CheckboxSelectMultiple
# from multiselectfield import MultiSelectField

# Create your models here.
class GendersModel(models.Model):
    genders_title = models.CharField(max_length=120, unique=True, blank=True)


    def __str__(self):
        return self.genders_title

    

class NationalityModel(models.Model):
    nationality_title = models.CharField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.nationality_title


class ContactModel(models.Model):
    contact_id = models.AutoField(primary_key=True)
    hn = models.SlugField(max_length=120, unique=True, blank=True)
    title_th = models.CharField(max_length=120, unique=False, blank=True)
    f_name_th = models.CharField(max_length=120, unique=True, blank=True)
    l_name_th = models.CharField(max_length=120, unique=True, blank=True)
    m_name_th = models.CharField(max_length=120, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=120, unique=True, blank=True, null=True)
    mobile_phone = models.CharField(max_length=120, unique=True, blank=True, null=True)
    home = models.CharField(max_length=120, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(max_length=120, unique=False, blank=True, null=True)

    title_en = models.CharField(max_length=120, unique=False, blank=True)
    f_name_en = models.CharField(max_length=120, unique=True, blank=True)
    l_name_en = models.CharField(max_length=120, unique=True, blank=True)
    m_name_en = models.CharField(max_length=120, unique=True, blank=True, null=True)

    work = models.CharField(max_length=120, unique=True, blank=True, null=True)
    work_phone_exten = models.CharField(max_length=120, unique=True, blank=True, null=True)
    main_fax = models.CharField(max_length=120, unique=True, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    gender = models.ForeignKey(GendersModel, blank=True, on_delete=models.CASCADE)
    nationality = models.ForeignKey(NationalityModel, blank=True, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_updated= models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return f'{self.hn} {self.f_name_th} {self.l_name_th}'

class PhoneTypeModel(models.Model):
    type_title = models.CharField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.type_title

class AlternatePhoneModel(models.Model):
    contact_by = models.ForeignKey(ContactModel, blank=True, on_delete=models.CASCADE)
    alternate_phone = PhoneNumberField(blank=True, null=False, region="TH")
    # test_phone = PhoneNumberField(blank=True, region="TH")
    phone_type = models.ForeignKey(PhoneTypeModel, blank=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, unique=True, blank=True) 
    primary_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.contact_by} | {self.alternate_phone}'

class EmailTypeModel(models.Model):
    type_title = models.CharField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.type_title

class AlternateEmailModel(models.Model):
    contact_by = models.ForeignKey(ContactModel, blank=True, on_delete=models.CASCADE)
    alternate_email = models.EmailField(max_length=255, unique=True, blank=True)
    email_type = models.ForeignKey(EmailTypeModel, blank=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, unique=True, blank=True) 
    primary_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.contact_by} | {self.alternate_email}'

class PersonalAddressModel(models.Model):
    contact_by = models.ForeignKey(ContactModel, blank=True, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255, unique=False, blank=True)
    address_2 = models.CharField(max_length=255, unique=False, blank=True, null=True)
    building = models.CharField(max_length=255, unique=False, blank=True, null=True)
    district = models.CharField(max_length=255, unique=False, blank=True, null=True)
    city = models.CharField(max_length=255, unique=False, blank=True)
    province = models.CharField(max_length=255, unique=False, blank=True, null=True)
    zipcode = models.CharField(max_length=255, unique=False, blank=True, null=True)
    primary_status = models.BooleanField(default=False)
    alignment_status = models.BooleanField(default=False)

class TestCheckboxModel(models.Model):

    # CALL_GENDER = GendersModel.objects.values_list('id', 'genders_title')
    # GENDER_LIST = []
    # for item in CALL_GENDER:
    #     GENDER_LIST.append(item)

    chk_id = models.AutoField(primary_key=True, auto_created=True)
    chk_name = models.CharField(max_length=255, blank=True)
    chk_gender = models.ManyToManyField(GendersModel, blank=True)
    
    # chk_dender2 = MultiSelectField(choices=GENDER_LIST, blank=True, null=True)

    def __str__(self):
        return self.chk_name




