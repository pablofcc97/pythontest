from django.urls import path
from . import views

urlpatterns = [
    path('facturas/reporte-test/<int:id>',views.reporteTest,  name='reporte-test'),
    path('facturas/', views.facturas, name='facturas'),

    path('facturas/reporte/<int:id>', views.generar_pdf, name='generate_pdf'),
]