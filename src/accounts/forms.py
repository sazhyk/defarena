# -*- coding: utf8 -*-

from django.forms import ModelForm
from .models import CapsUpload


class FileUploadForm(ModelForm):
    class Meta:
        model = CapsUpload

        fields = ('caps_name', 'files', 'description')
