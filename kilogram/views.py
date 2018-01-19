from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
# Create your views here.
from kilogram.forms import CreateUserForm, UploadForm


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')


    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form' : form})



class IndexView(ListView):
    # model = Photo

    context_object_name = 'user_photo_list'
    paginate_by = 1

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'

    form_class = CreateUserForm
    success_url = reverse_lazy('created_user')

class RegistrationCompletedView(TemplateView):
    template_name = 'registration/signup_done.html'



