from django.db import models
from django.utils import timezone
from .utils import full_name, sanitize_filename
#from PIL import image
# Create your models here.


PROJEKTY_TYPES = (
    ('RD', ('Rodinne domy')),
    ('INTER', ('Interiery')),
    ('JINE', ('Jine')),
)

class Project(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    screen = models.ImageField(upload_to = 'screen_folder/', default = 'screen_folder/None/no-img.jpg')
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    type = models.CharField(max_length=10, blank=True, null=True, choices=PROJEKTY_TYPES)
    def __str__(self):
        return self.name

class Project_Photo(models.Model):
    rodinny_dum = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo_name = models.CharField(max_length=200)
    number = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to = 'photo_folder/', default = 'photo_folder/None/no-img.jpg')

    def __str__(self):
        return self.photo_name

class Vizualizace(models.Model):
    name = models.CharField(max_length=200)
    screen = models.ImageField(upload_to = 'vizualizace_folder/', default = 'screen_folder/None/no-img.jpg')
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    def __str__(self):
        return self.name
