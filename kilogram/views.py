from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
# Create your views here.
from kilogram.forms import CreateUserForm, UploadForm


def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')

    if (isinstance(request.user, User) == False):
        return redirect('/accounts/login')

    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form' : form})



class IndexView(TemplateView):
    template_name = 'kilogram/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'

    form_class = CreateUserForm
    success_url = reverse_lazy('created_user')

class RegistrationCompletedView(TemplateView):
    template_name = 'registration/signup_done.html'



