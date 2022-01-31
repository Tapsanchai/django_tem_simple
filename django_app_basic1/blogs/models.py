from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms.widgets import NullBooleanSelect, SelectMultiple, CheckboxSelectMultiple
from multiselectfield import MultiSelectField



# Create your models here.
# M

class BlogType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class BlogTags(models.Model):
    # UP_SKILLS = 'UpSkills'
    # RECOMMEND = 'Recommend'
    # GENERAL = 'Genneral'

    # BLOG_TAGS = [
    #     (UP_SKILLS, 'UpSkills'),
    #     (RECOMMEND, 'Recommend'),
    #     (GENERAL, 'Genneral'),
    # ]
    # tag_name = models.CharField(max_length=120, blank=True, null=True, choices=BLOG_TAGS)
    tag_name = models.CharField(max_length=255, blank=True, null=True)
    # key_tag_name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.tag_name


class Blogs(models.Model):
    #  call oject from BlogTags
    BLOG_TAGS_FROM_BLOGTAGS_MODAL = BlogTags.objects.all()
    # set (key,Value) to list_type 
    BLOG_TAGS = [(item.id, item.tag_name) for item in BLOG_TAGS_FROM_BLOGTAGS_MODAL]

    # UP_SKILLS = 1
    # RECOMMEND = 2
    # GENERAL = 3

    # BLOG_TAGS = [
    #     (UP_SKILLS, ('',('upskills','Upskills'),),),
    #     (RECOMMEND, 'Recommend'),
    #     (GENERAL, 'Genneral'),
    # ]

    title = models.CharField(max_length=255, blank=False, unique=True)
    content = models.TextField()
    create_by = models.CharField(max_length=255, blank=False, null=True)
    blog_type = models.ForeignKey(BlogType, blank=False, null=True, on_delete=models.CASCADE)
    blog_hashtags = MultiSelectField(choices=BLOG_TAGS, null=True, blank=False, max_length=255)
    time_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    # show and process on only
    '''  
    def clean(self):
        if not len(self.title) > 10:
            raise ValidationError({'title': "Title should have at least 10 letters"})
            '''
