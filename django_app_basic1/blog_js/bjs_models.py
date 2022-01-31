from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.forms.widgets import NullBooleanSelect, SelectMultiple, CheckboxSelectMultiple
from multiselectfield import MultiSelectField



# Create your models here.
# M
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

class JS_BlogType_Manager(models.Manager):
    def get_by_natural_key(self,type_name):
        return self.get(type_name=type_name)

class JS_BlogType(models.Model):
    objects = JS_BlogType_Manager()

    type_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type_name

    def natural_key(self):
        return (self.type_name)

    class Meta:
        unique_together = (('type_name'),)
    

class JS_BlogTags(models.Model):
    # tag_name = models.CharField(max_length=120, blank=True, null=True, choices=BLOG_TAGS)
    tag_name = models.CharField(max_length=255, blank=True, null=True)
    # tag_name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.tag_name


class JS_Blogs(models.Model):
    #  call oject from BlogTags
    BLOG_TAGS_FROM_BLOGTAGS_MODAL = JS_BlogTags.objects.all()
    # set (key,Value) to list_type 
    BLOG_TAGS = [(item.tag_name, item.tag_name) for item in BLOG_TAGS_FROM_BLOGTAGS_MODAL]

    title = models.CharField(max_length=255, blank=False, unique=True)
    content = models.TextField()
    create_by = models.CharField(max_length=255, blank=False, null=True)
    blog_type = models.ForeignKey(JS_BlogType, blank=False, on_delete=models.CASCADE)
    blog_hashtags = MultiSelectField(choices=BLOG_TAGS, null=True, blank=False, max_length=255)
    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

