from django.conf import settings
from django.db import models

# Create your models here.

def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    ext = filename.split('.')[-1]
    return '%s/%s.%s' % (instance.owner.username, pid, ext)


class Photo(models.Model):
    image = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    thumbnail_image = models.ImageField(blank=True)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


