from django.forms import widgets
from .bjs_models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

# User = get_user_model()
class ChkRegisForm(forms.ModelForm):
    re_password = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name', 'last_name']

    def clean(self, *args, **kwargs):
        cleaned_data = super(ChkRegisForm, self).clean(*args, **kwargs)
        print('come to user_form_clean')
        # get_username = cleaned_data.get('username')
        # get_password = cleaned_data.get('password')
        print(self.cleaned_data)

        if not cleaned_data.get('username'):
            self._errors['username'] = self.error_class(['username is required'])
        if not cleaned_data.get('password'):
            self._errors['password'] = self.error_class(['password is required'])
        if not cleaned_data.get('re_password'):
            self._errors['re_password'] = self.error_class(['re_password is required'])
        if not cleaned_data.get('email'):
            self._errors['email'] = self.error_class(['email is required'])
        if not cleaned_data.get('first_name'):
            self._errors['first_name'] = self.error_class(['first_name is required'])
        if not cleaned_data.get('last_name'):
            self._errors['last_name'] = self.error_class(['last_name is required'])
        elif cleaned_data.get('re_password') != cleaned_data.get('password'):
            self._errors['re_password'] = self.error_class(['comfirm-password failed'])
            self._errors['password'] = self.error_class(['comfirm-password failed'])
            # self._errors['__all__'] = self.error_class(['comfirm-password failed'])
        elif User.objects.filter(username = cleaned_data.get('username')).exists():
            self._errors['username'] = self.error_class(["This username already has a use."])
            
        return self.cleaned_data