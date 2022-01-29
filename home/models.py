from django.db import models

# Create your models here.

class enquiry(models.Model):
    FirstName = models.CharField(max_length=264)
    LastName = models.CharField(max_length=264)
    Email = models.CharField(max_length=264)
    PhoneNumber = models.CharField(max_length=264)
    Address = models.CharField(max_length=264)
    Organization = models.CharField(max_length=264)
    Requirements = models.TextField()

    def __str__(self):
        return self.FirstName + "  " + self.LastName
