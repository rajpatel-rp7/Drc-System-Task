from django.db import models
from account.models import User
from django.core.exceptions import ValidationError


# Create your models here.
# File Extension Validetor for uploading specific extension file
# We can also create a validator.py for this function for Code Reusability
def validate_file(value):
    value= str(value)
    if value.endswith('.pdf') != True and value.endswith('.mp4') != True and value.endswith('.mkv') \
            != True and value.endswith('.avi') != True and value.endswith('.m4v') != True and value.endswith('.webm'):
        raise ValidationError('Only PDF and Videos File can be uploaded')
    else:
        return value


# Maximum Upload Size validator
def validate_file_size(value):
    filesize = value.size
    # 200MB File Size into Bytes is 209,715,200
    if filesize > 209715200:
        raise ValidationError('The maximum file size that can be uploaded is 200MB')
    else:
        return value


# user_directory_path is for creating directory and storing file after uploading file
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # We can also chanege user_<id> to user_<email>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/', null=True, blank=False, verbose_name="",
                            validators=[validate_file, validate_file_size])

    def __str__(self):
        # The str(self.file) change the file name into string this is called type conversion
        return str(self.user.email) + ' ' + str(self.file)

    def get_file_name(self):
        return self.file.name