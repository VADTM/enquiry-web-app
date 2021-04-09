from django.db import models

# Create your models here.
class Student(models.Model):
    issue = models.CharField(max_length = 200)
    Solution = models.TextField()
    def __str__(self):
        return self.name
    def show_desc(self):
        return self.description[:50]
