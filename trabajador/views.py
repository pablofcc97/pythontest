from pydoc import doc

from django.http import HttpResponse
from django.shortcuts import render
from .models import Movements, Worker
from django.shortcuts import get_object_or_404

from django.conf import settings
import os
import pdfkit
import tempfile


# Create your views here.
def asistencias(request, id):
    worker = Worker.objects.get(id=id)
    get_object_or_404(Worker, id=id)
    return render(request, 'asistencia.html', {
        'worker': worker
    })
def trabajadores(request):
    workers = Worker.objects.all()
    return render(request, 'workers.html', {
        'workers': workers
    })

def tasks(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'TASKS'
    return render(request, 'tasks.html', {
        'title': title
    })

def projects(request):
    #return HttpResponse('<h1>hola mundo</h1>')
    title = 'Projects'
    return render(request, 'projects.html', {
        'title': title
    })

def generar_pdf(request,id):
    # Datos de la plantilla html
    movements = Movements.objects.filter(worker_id=id)
    worker = Worker.objects.get(id=id)

    datos = {
        'movements': movements,
        'worker': worker
    }

    # Renderizar el contenido HTML utilizando la plantilla y los datos
    html_template = 'layouts/pdf.html'
    html = render(request, html_template, datos).content.decode('utf-8')

    # Configuración para el PDF, refrencia a la ruta del ejecutable wkhtmltopdf
    configuracion_pdf = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)

    opciones_pdfkit = {
        'page-size': 'A4',
        'encoding': 'utf-8',

    }
    # Generar el PDF
    pdf = pdfkit.from_string(html, False, configuration=configuracion_pdf)

    # Responder con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=mi_pdf.pdf'

    #DESCARGAR DEFRENTE EL PDF
    #response['Content-Disposition'] = f'attachment; filename="example.pdf"'

    return response

def reporteTest(request, id):
    movements = Movements.objects.filter(worker_id=id)
    worker = Worker.objects.get(id=id)
    return render(request, 'layouts/pdf.html', {
        'worker': worker,
        'movements': movements
    })
