from django.shortcuts import render

def about(request):
    return render(request, '<имя_приложения>/about.html')

def contact(request):
    return render(request, '<имя_приложения>/contact.html')

def services(request):
    return render(request, '<имя_приложения>/services.html')
