from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Project(models.Model):
    FILTER = (
        ('web','Web'),
        ('app','App'),
        ('aiml','AI/ML'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_src = models.URLField()
    project_link = models.URLField()
    tag = models.CharField(max_length=200,choices=FILTER)

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    FILTER = (
        ('cs','Coursera'),
        ('udm','UDEMY'),
        ('kct','KCT'),
        ('fl','FutureLearn'),
        ('gl','Great Learning'),
        ('aws','AWS'),
        ('ms','Microsoft'),
    )
    name = models.CharField(max_length=255)
    img_src = models.URLField()
    credential = models.URLField()
    tag = models.CharField(max_length=200,choices=FILTER)

    def __str__(self):
        return self.name