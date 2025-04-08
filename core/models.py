from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    post_by = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=True)
    post_image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.name