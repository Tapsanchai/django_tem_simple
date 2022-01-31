from django.forms import widgets
from .bjs_models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

# User = get_user_model()
class ChkLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    fields = ['username', 'password']

    def clean(self, *args, **kwargs):
        cleaned_data = super(ChkLoginForm, self).clean(*args, **kwargs)
        print('come to user_form_clean')
        get_username = cleaned_data.get('username')
        get_password = cleaned_data.get('password')
        print(self.cleaned_data)

        def chk_validate_required(g_username, g_password):
            if not g_username and not g_password:
                self._errors['username'] = self.error_class(['username is required'])
                self._errors['password'] = self.error_class(['password is required'])
                return False
            elif not g_username:
                self._errors['username'] = self.error_class(['username is required'])
                return False 
            elif not g_password:
                self._errors['password'] = self.error_class(['password is required'])
                return False 
            else: 
                return True

        call_chk_validate = chk_validate_required(get_username,get_password)
        if not call_chk_validate:
            print('value is null or empty')
        else:
            print('value is vaild')
            chk_real_account = authenticate(username = get_username, password = get_password)
            if not chk_real_account:
                self._errors['__all__'] = self.error_class(['username or password is wrong'])

        #         raise ValidationError(self.error_class(['username or password is wrong']))
                # self._errors['__all___'] = self.error_class(['username or password is wrong'])
        # chk_username = User.objects.filter(username = cleaned_data.get('username'))
        # if not chk_username.exists():
        #     self._errors['username'] = self.error_class(['This username does not exist'])
        
        return self.cleaned_data