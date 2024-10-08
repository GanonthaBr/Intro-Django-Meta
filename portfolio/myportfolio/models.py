from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="static/images")

    def __str__(self):
        return self.title