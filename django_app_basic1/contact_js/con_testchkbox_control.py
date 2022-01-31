from django.forms import widgets
from .con_models import *
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import CheckboxSelectMultiple

# from multiselectfield import MultiSelectField



class CheckFormCheckbox(forms.ModelForm):
    chk_gender = forms.ModelMultipleChoiceField(
        queryset=GendersModel.objects.all(),
        widget = CheckboxSelectMultiple()
    )
    class Meta:
        model = TestCheckboxModel
        fields = ('chk_gender','chk_name')


    def clean(self):
        cleaned_data = super().clean()

        if(not cleaned_data.get('chk_gender')):
            self._errors['chk_gender'] = self.error_class(['chk_gender is required'])
        if(not cleaned_data.get('chk_name')):
            self._errors['chk_name'] = self.error_class(['chk_name is required'])

        return self.cleaned_data
