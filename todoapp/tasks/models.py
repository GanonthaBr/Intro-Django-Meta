from django.db import models

# Create your models here.
class Todotask(models.Model):
    
    title = models.CharField(max_length=200)
    description  = models.TextField(max_length=1000, default='task description...')
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"