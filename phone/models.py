from django.db import models


class Model(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model


class Phone(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              null=True, blank=True)
    image = models.ImageField(upload_to='phones')
    year = models.IntegerField
    kgs = models.IntegerField
    # usd = kgs/90

    def __str__(self):
        return f'{self.title}-{self.model}, {self.year}'
