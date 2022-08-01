from django.shortcuts import render

def home(request):

    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    
    return render(request,'error_404.html', data)
