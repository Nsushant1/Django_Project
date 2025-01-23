from django.db import models
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(default=now,editable=False)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title