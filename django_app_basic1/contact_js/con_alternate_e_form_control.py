from django.forms import widgets
from .con_models import *
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



class CheckFormCreateAlternateEmail(forms.ModelForm):
    class Meta:
        model = AlternateEmailModel
        fields = ('contact_by','alternate_email','email_type','description','primary_status')

    def clean_alternate_email(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('alternate_email')
        print('clean_alternate_email = ', data)
        
        try:
            validate_email(data)

        except Exception as e:          
            print("bad email, details: ",e)
            raise ValidationError(('alternate_email is required'), code='none_email')

        return data


    def clean(self):
        cleaned_data = super().clean()
        data_email = cleaned_data.get('alternate_email')
        print('email = ', data_email, '-->', type(data_email))
        print('data_form = ', self.cleaned_data)
        # if( not cleaned_data.get('alternate_email')):
        #     # raise ValidationError(('alternate_email','alternate_email is kuy'), code='none_email')
        #     raise ValidationError({'alternate_email':'alternate_email is kuy'}, code='none_email')
            # self._errors['alternate_email'] = self.error_class(['test is required'])
            # self.add_error('alternate_email',ValidationError(('format your email is woung.'), code='test'))

        if(not cleaned_data.get('email_type')):
            self._errors['email_type'] = self.error_class(['email_type is required'])
        if(not cleaned_data.get('description')):
            self._errors['description'] = self.error_class(['description is required'])
        # if(not cleaned_data.get('alternate_email')):
        #     self._errors['alternate_email'] = self.error_class(['alternate_email is required'])

        return self.cleaned_data

    def save(self, *args, **kwargs):
        if not self.cleaned_data['primary_status']:
        # The use of return is explained in the comments
            return super(CheckFormCreateAlternateEmail, self).save(*args, **kwargs)  
        else:
            with transaction.atomic():
                AlternateEmailModel.objects.filter(primary_status=True, contact_by=self.cleaned_data['contact_by']).update(primary_status=False)
                # The use of return is explained in the comments
                return super(CheckFormCreateAlternateEmail, self).save(*args, **kwargs)