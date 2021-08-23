from django.db import models
from django.contrib.auth.models import User


class Volume(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Bookshelf(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    volume = models.ForeignKey(Volume, null=True, on_delete=models.CASCADE)
    is_private = models.BooleanField()

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    val = models.IntegerField()
    volume = models.ForeignKey(Volume, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.val)


class ReadingPos(models.Model):
    val = models.IntegerField(null=True)
    volume = models.OneToOneField(Volume, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.val)
