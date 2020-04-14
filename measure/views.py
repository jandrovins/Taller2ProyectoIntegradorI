from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import requests

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET and 'scale' in request.GET:
        value = request.GET['value']
        scale = request.GET['scale']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'temperature_abril14', 'value': value, 'scale': scale}
            response = requests.post('http://127.0.0.1:8000/measure/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measure/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})
