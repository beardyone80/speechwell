from django.db import models
from ckeditor.fields import RichTextField
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from resources.models import Specialty, Therapist
from django.utils.text import slugify

'''
Disorder model including relationship
with Specialty model and Therapist model
'''


class Disorder(models.Model):
    disorderID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True, default='')
    slug = models.SlugField(
        max_length=200, unique=True, null=False, default=''
        )
    # select author from Therapist model
    author = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    disorder_type = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        storage=RawMediaCloudinaryStorage(), blank=True, null=True
        )
    description = RichTextField()  # RichTextField for additional formatting
    excerpt = models.TextField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Title: {self.title}"
