from django.forms import widgets
from .con_models import *
from django import forms
from django.core.exceptions import ValidationError



class CheckFormCreatePersonalAddress(forms.ModelForm):
    class Meta:
        model = PersonalAddressModel
        fields = ('contact_by','address_1','city','primary_status','alignment_status')

    def clean(self):
        cleaned_data = super().clean()
        print('data_form = ', self.cleaned_data)
        if(not cleaned_data.get('address_1')):
            self._errors['address_1'] = self.error_class(['address_1 is required'])
        if(not cleaned_data.get('city')):
            self._errors['city'] = self.error_class(['city is required'])

        return self.cleaned_data

    def save(self, *args, **kwargs):
        if not self.cleaned_data['primary_status']:
        # The use of return is explained in the comments
            return super(CheckFormCreatePersonalAddress, self).save(*args, **kwargs)  
        else:
            with transaction.atomic():
                PersonalAddressModel.objects.filter(primary_status=True, contact_by=self.cleaned_data['contact_by']).update(primary_status=False)
                # The use of return is explained in the comments
                return super(CheckFormCreatePersonalAddress, self).save(*args, **kwargs)