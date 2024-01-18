from django.urls import path 
from .import views 


urlpatterns = [
    path('test/',views.test),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('blog/',views.blog,name="blog"),
    path('gallery/',views.gallery,name="gallery"),
    path('testimonial/',views.testimonial,name="testimonial"),
    
]
