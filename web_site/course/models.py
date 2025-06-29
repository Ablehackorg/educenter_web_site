from enum import unique

from django.db import models
from django.utils.safestring import mark_safe
from home.models import Language


# Create your models here.

llist =Language.objects.all()
list1 = []

for rs in llist:
    list1.append((rs.code, rs.name))
langlist = (list1)


class Course(models.Model):
    title= models.CharField(max_length=100)
    keywords= models.CharField(max_length=100)
    description = models.TextField()
    image= models.ImageField(upload_to ='images')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class CourseLang(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lang = models.CharField(max_length=6, choices=langlist)
    title= models.CharField(max_length=100)
    keywords= models.CharField(max_length=100)
    description = models.TextField()
    image= models.ImageField(upload_to ='images')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Subject(models.Model):
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='subject_images/')
    price = models.CharField()
    detail =models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class SubjectLang(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lang = models.CharField(max_length=6, choices=langlist)
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='subject_images/')
    price = models.CharField()
    detail =models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class Student(models.Model):
    name =models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Tutor(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='subject_images/')

    def __str__(self):
        return self.name
    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class TutorLang(models.Model):
    tutor = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lang = models.CharField(max_length=6, choices=langlist)
    subject = models.ForeignKey(Tutor,on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='subject_images/')

    def __str__(self):
        return self.name
    def image_tag(self):
        return mark_safe('<img src"{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
