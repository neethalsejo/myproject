from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    branch=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='img',blank=True)
    description=models.TextField(blank=True)
    district=models.CharField(max_length=250,unique=True)
    pediatrician= models.CharField(max_length=250,unique=True)
    urologist = models.CharField(max_length=250,unique=True)
    physician = models.CharField(max_length=250,unique=True)
    gynaecologist = models.CharField(max_length=250,unique=True)
    ent = models.CharField(max_length=250,unique=True)
    available=models.BooleanField(default=True)

    class Meta:
        ordering=('branch',)
        verbose_name='hospital'
        verbose_name_plural='hospitals'
    def get_url(self):
        return reverse('taskapp:hospital_by_branch',args=[self.slug])

    def __str__(self):
        return  '{}'.format(self.branch)


class Patient(models.Model):
    username=models.CharField(max_length=250)
    pname=models.CharField(max_length=250,)
    slug=models.SlugField(max_length=250)
    age=models.CharField(max_length=250,)
    gender=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    address=models.TextField(blank=True)
    branch=models.TextField(blank=True)
    diseas=models.TextField(blank=True)
    dname=models.CharField(max_length=250,)
    appdate=models.DateTimeField()
    bookeddate=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pname',)
        verbose_name = 'patient'
        verbose_name_plural='patients'

    def __str__(self):
        return '{}'.format(self.pname)