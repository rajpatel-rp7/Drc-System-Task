from django import forms
from .models import FileUpload
from app.models import validate_file, validate_file_size


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        fields = ('title', 'file',)
