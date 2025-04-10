from django.urls import path
from .views import IndexView, AddPhotoView

urlpatterns = [
    path('add_photo/', AddPhotoView.as_view(), name='add_photo'),
    path('', IndexView.as_view(), name='home'),
]
