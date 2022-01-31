from django.forms import widgets
from .con_models import *
from django import forms
from django.core.exceptions import ValidationError


class CheckFormCreateAlternatePhone(forms.ModelForm):
    class Meta:
        model = AlternatePhoneModel
        fields = ('contact_by','alternate_phone','phone_type','description','primary_status')
        # field_classes = {
        #     'slug': MySlugFormField,
        # }
        help_texts = {
            'alternate_phone': ('Rew Your Phone_Number'),
            'contact_by': ('select contact account'),
        }

    # def clean_alternate_phone(self):
    #     cleaned_data = super().clean()
    #     data = cleaned_data.get('alternate_phone')
    #     print('clean_alternate_phone = ', data)

    #     if not data:
    #         # self.add_error('alternate_phone', 'alternate_phone is required')
    #         raise ValidationError(('alternate_phone is required'), code='none_phone_number')
    #     return data


    def clean(self):
        cleaned_data = super().clean()
        data_phone = cleaned_data.get('alternate_phone')
        print('phone = ', data_phone, '-->', type(data_phone))
        print('data_form = ', self.cleaned_data)
        
        if(not cleaned_data.get('alternate_phone') and cleaned_data.get('alternate_phone') is not None):
            self.add_error('alternate_phone',ValidationError(('alternate_phone is required'), code='none_phone_number'))
        if(not cleaned_data.get('contact_by')):
            self._errors['contact_by'] = self.error_class(['contact_by is required'])
        if(not cleaned_data.get('phone_type')):
            self._errors['phone_type'] = self.error_class(['phone_type is required'])
        if(not cleaned_data.get('description')):
            self._errors['description'] = self.error_class(['description is required'])


        return self.cleaned_data

    def save(self, *args, **kwargs):
        if not self.cleaned_data['primary_status']:
        # The use of return is explained in the comments
            return super(CheckFormCreateAlternatePhone, self).save(*args, **kwargs)  
        else:
            with transaction.atomic():
                AlternatePhoneModel.objects.filter(primary_status=True, contact_by=self.cleaned_data['contact_by']).update(primary_status=False)
                # The use of return is explained in the comments
                return super(CheckFormCreateAlternatePhone, self).save(*args, **kwargs)