from . import views
from django.urls import path

urlpatterns = [
    path('getimages/', view=views.getdata,name='Images-get'),
    path('getimage/', view=views.get_image_from_text,name='Image-get'),
    
]
