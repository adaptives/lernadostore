from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    placement = models.IntegerField()

    
class CourseGroup(models.Model):
    title = models.CharField(max_length=255)
    sanitizedTitle = models.CharField(max_length=255)
      

class Course(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=255)
    sanitizedTitle = models.CharField(max_length=255)
    category = models.ForeignKey(CourseCategory, null=True)
    group = models.ForeignKey(CourseGroup, null=True)
    