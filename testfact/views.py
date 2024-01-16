from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Factura, Producto
from django.shortcuts import get_object_or_404

from django.conf import settings
import os
import pdfkit
import tempfile


# Create your views here.
def factura(request, id):
    factura = Factura.objects.get(id=id)
    get_object_or_404(Factura, id=id)
    return render(request, 'asistencia.html', {
        'factura': factura
    })
def facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturas.html', {
        'facturas': facturas
    })


def generar_pdf(request,id):
    # Datos de la plantilla html
    factura = Factura.objects.get(id=id)
    productos = Producto.objects.filter(factura_id=id)

    datos = {
        'factura': factura
    }

    # Renderizar el contenido HTML utilizando la plantilla y los datos
    html_template = 'layouts/factpdf.html'
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
    factura = Factura.objects.get(id=id)
    productos = Producto.objects.filter(factura_id=id)
    return render(request, 'layouts/factpdf.html', {
        'factura': factura,
        'productos': productos
    })
