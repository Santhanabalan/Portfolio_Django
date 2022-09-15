from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Cgpa(models.Model):
    name = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    sem1 = models.FloatField(max_length=255)
    sem2 = models.FloatField(max_length=255)
    sem3 = models.FloatField(max_length=255)
    sem4 = models.FloatField(max_length=255)
    sem5 = models.FloatField(max_length=255)
    sem6 = models.FloatField(max_length=255)

    def __str__(self):
        return self.name

class Sgpa(models.Model):
    name = models.CharField(max_length=255)
    cn1 = models.CharField(max_length=255)
    cc1 = models.FloatField()
    cg1 = models.FloatField()
    cn2 = models.CharField(max_length=255)
    cc2 = models.FloatField()
    cg2 = models.FloatField()
    cn3 = models.CharField(max_length=255)
    cc3 = models.FloatField()
    cg3 = models.FloatField()
    cn4 = models.CharField(max_length=255)
    cc4 = models.FloatField()
    cg4 = models.FloatField()
    cn5 = models.CharField(max_length=255)
    cc5 = models.FloatField()
    cg5 = models.FloatField()
    cn6 = models.CharField(max_length=255)
    cc6 = models.FloatField()
    cg6 = models.FloatField()
    cn7 = models.CharField(max_length=255)
    cc7 = models.FloatField()
    cg7 = models.FloatField()


    def __str__(self):
        return self.name  