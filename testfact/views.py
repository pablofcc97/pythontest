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

#wkhtmltopdf
from django.http import HttpResponse
from django.shortcuts import render
from .models import Factura, Producto
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
import tempfile
import subprocess


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


def generar_pdf(request, id):
    factura = Factura.objects.get(id=id)
    productos = Producto.objects.filter(factura_id=id)

    datos = {
        'factura': factura,
        'productos': productos
    }

    # Renderizar el contenido HTML utilizando la plantilla y los datos
    html_template = 'layouts/factpdf.html'
    html = render_to_string(html_template, datos)

    # Crear un archivo temporal para el HTML
    temp_html = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    temp_html.write(html.encode('utf-8'))
    temp_html.close()

    # Configuración para el PDF
    output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    output_pdf.close()

    # Ejecutar wkhtmltopdf para convertir HTML a PDF
    subprocess.run([settings.WKHTMLTOPDF_PATH, temp_html.name, output_pdf.name])

    # Leer el contenido del PDF generado
    with open(output_pdf.name, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    # Responder con el PDF
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=mi_pdf.pdf'

    # Eliminar archivos temporales
    os.unlink(temp_html.name)
    os.unlink(output_pdf.name)

    return response

def reporteTest(request, id):
    factura = Factura.objects.get(id=id)
    productos = Producto.objects.filter(factura_id=id)
    return render(request, 'layouts/factpdf.html', {
        'factura': factura,
        'productos': productos
    })
