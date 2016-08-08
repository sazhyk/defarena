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


class CapsUpload(models.Model):
    class Meta:
        db_table = 'account_caps'

    caps_name = models.CharField(blank=False, null=False, max_length=150)
    files = models.FileField(storage=settings.UPLOAD_PATH)
    description = models.TextField(max_length=400)
    timestamp = models.DateTimeField(blank=False, auto_now=True)
