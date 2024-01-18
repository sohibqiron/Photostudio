from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request,'mainapp/test.html')

def index(request):
    return render(request,'mainapp/index.html')


def about(request):
    return render(request,'mainapp/about.html')

def blog(request):
    return render(request,'mainapp/blog.html')

def gallery(request):
    return render(request,'mainapp/gallery.html')

def testimonial(request):
    return render(request,'mainapp/testimonial.html')

