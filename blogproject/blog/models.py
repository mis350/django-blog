from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
  )

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0, choices=STATUS)

    def __str__(self):
        return f"{self.pk}: {self.title} ({self.get_status_display()}))"


class Comment(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length=200, blank=True, null=True, default='Anonymous')
    email = models.EmailField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)