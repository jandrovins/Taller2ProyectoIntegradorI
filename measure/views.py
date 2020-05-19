from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import requests

def measure(request):
    error = False
     # Verifica si hay un parámetro value en la petición POST
    if request.method == "POST":  # when user sends registration info:
        args = {
            'codigo' : request.POST['codigo'],
            'latitud' : request.POST['latitud'],
            'longitud' : request.POST['longitud'],
            'terreno' : request.POST['terreno'],
            'area' : request.POST['area'],
        }
        if int(args['area']) <= 0:
            error = True
        response = requests.post('http://127.0.0.1:8000/measure/', args)
        measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measure/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures, 'error': error})
