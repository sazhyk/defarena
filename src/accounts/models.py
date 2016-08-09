from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

from django.conf import settings


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class CapsUpload(models.Model):

    caps_name = models.CharField(blank=False, null=False, max_length=150)
    files = models.FileField(storage=settings.UPLOAD_PATH, upload_to=user_directory_path)
    description = models.TextField(max_length=400)
    timestamp = models.DateTimeField(blank=False, auto_now=True)
