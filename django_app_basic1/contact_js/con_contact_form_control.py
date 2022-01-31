from django.forms import widgets
from .con_models import *
from django import forms
from django.core.exceptions import ValidationError



class CheckFormCreateContact(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [
            'contact_id','hn','title_th','f_name_th','l_name_th','m_name_th','email','home','date_of_birth','age',
            'title_en','f_name_en','l_name_en','m_name_en','work','work_phone_exten','main_fax',
            'gender','nationality'
        ]

    def clean(self):
        cleaned_data = super().clean()
        print('data_form = ', self.cleaned_data)
        if(not cleaned_data.get('hn')):
            self._errors['hn'] = self.error_class(['hn is required'])
        if(not cleaned_data.get('title_th')):
            self._errors['title_th'] = self.error_class(['title_th is required'])
        if(not cleaned_data.get('f_name_th')):
            self._errors['f_name_th'] = self.error_class(['f_name_th is required'])
        if(not cleaned_data.get('l_name_th')):
            self._errors['l_name_th'] = self.error_class(['l_name_th is required'])
        if(not cleaned_data.get('date_of_birth')):
            self._errors['date_of_birth'] = self.error_class(['date_of_birth is required'])

        if(not cleaned_data.get('title_en')):
            self._errors['title_en'] = self.error_class(['title_en is required'])
        if(not cleaned_data.get('f_name_en')):
            self._errors['f_name_en'] = self.error_class(['f_name_en is required'])
        if(not cleaned_data.get('l_name_en')):
            self._errors['l_name_en'] = self.error_class(['l_name_en is required'])
        if(not cleaned_data.get('gender')):
            self._errors['gender'] = self.error_class(['gender is required'])
        if(not cleaned_data.get('nationality')):
            self._errors['nationality'] = self.error_class(['nationality is required'])


        return self.cleaned_data