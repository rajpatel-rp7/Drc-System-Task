from django.shortcuts import render, redirect
from account.models import User
from app.models import FileUpload
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = User.objects.all()
    files = FileUpload.objects.all()
    return render(request, 'index.html', {'context': context, 'files': files})


# Login Required Decorators
# This decorator is restrict unlogedin user to upload file
@login_required()
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form,})
