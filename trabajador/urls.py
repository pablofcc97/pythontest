from django.urls import path
from . import views

urlpatterns = [
    #path('reporte/<int:id>',views.ResultList,  name='reporte'),
    path('reporte-test/<int:id>',views.reporteTest,  name='reporte-test'),
    #path('asistencias/<int:id>', views.ResultList, name='asistencias'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),

    path('reporte/<int:id>', views.generar_pdf, name='generate_pdf'),
]