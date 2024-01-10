from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'HOME'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return HttpResponse('<h1>about</h1>')

def tasks(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'TASKS'
    return render(request, 'tasks.html', {
        'title': title
    })

def contact(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'CONTACT'
    contact__Form = ContactForm()
    return render(request, 'contact.html', {
        'title': title,
        'form':  contact__Form
    })

def projects(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'Projects'
    return render(request, 'projects.html', {
        'title': title
    })