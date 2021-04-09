from django.db import models

# Create your models here.
class Complain(models.Model):
    issue = models.CharField(max_length = 200)
    solution = models.TextField()
    def __str__(self):
        return self.issue
    def show_desc(self):
        return self.solution[:50]
