from .forms import PhotoForm
from django.views.generic import ListView, CreateView
from .models import Photo
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Photo
    template_name = 'myApp/index.html'
    context_object_name = 'photos'


class AddPhotoView(CreateView):
    model = Photo
    template_name = 'myApp/add_photo.html'
    form_class = PhotoForm
    success_url = reverse_lazy('home')
