from django.forms import widgets
from .bjs_models import *
from django import forms
from django.core.exceptions import ValidationError

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field
# from django.contrib.auth.models import get_user_model


class Chk_Form(forms.ModelForm):
    class Meta:
        model = JS_Blogs
        fields = [
            'title',
            'content',
            'create_by',
            'blog_type',
            'blog_hashtags',
        ]


    # method for cleaning the data

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'  # get or post
    #     self.helper.layout = Layout(
    #         Field('title', css_class="text-center"),
    #         Field('blog_hashtags', css_class="text-danger"),

    #     )

    def clean(self, *args, **kwargs):
        cleaned_data = super(Chk_Form, self).clean(*args, **kwargs)
        # get_titlename = self.cleaned_data.get('title')
        # get_content = self.cleaned_data.get('content')
        get_blog_hashtags = cleaned_data.get('blog_hashtags')
        # get_chk_length = self.get('chk_blog_hashtags_length')
        
        # print("chk_length = ",get_chk_xlength)
        print("get hashtags data =", get_blog_hashtags)
        # print("จำนวนข้อมูล =", len(get_blog_hashtags))
        # if (len(get_blog_hashtags)) !=  5:
        #     print("กรอกข้อมูลไม่ครบ")
        #     print("")
        # print("Blog_Type =", cleaned_data.get('blog_type'))
        print(self.cleaned_data)
        if not cleaned_data.get('title'):
            # if not cleaned_data.get('title'):
            # raise ValidationError({'title': "Title should have at least 10 letters"})
            self._errors['title'] = self.error_class(['title is required'])
        if not cleaned_data.get('content'):
            self._errors['content'] = self.error_class(['content is required'])
        if not cleaned_data.get('blog_type'):
            self._errors['blog_type'] = self.error_class(['blog_type is required'])
        if not cleaned_data.get('create_by'):
            self._errors['create_by'] = self.error_class(['create_by is required'])

        if not cleaned_data.get('blog_hashtags'):
            self._errors['blog_hashtags'] = self.error_class(['blog_hashtags is required'])
        elif (len(get_blog_hashtags)) <= 1 :
            print("เงื่อนไขเช็คจำนวน เป็นจริง")
            # self._errors['blog_hashtags'] = get_blog_hashtags
            self._errors['blog_hashtags'] = self.error_class(['please selecet at least 2 tag'])

        return self.cleaned_data