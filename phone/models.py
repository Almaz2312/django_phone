from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Model(models.Model):
    model = models.CharField(max_length=100)
    produced = models.DateField(null=True)

    def __str__(self):
        return f'{self.model} - {self.produced}'


class Phone(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              null=True, blank=True)
    image = models.ImageField(upload_to='phones', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    kgs = models.IntegerField
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}-{self.model}, {self.year}'
