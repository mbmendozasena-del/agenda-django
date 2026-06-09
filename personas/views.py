from django.shortcuts import render, redirect, get_list_or_404
from .models import Persona, Ciudad
from .utils import render_to_pdf
from django.http import HttpResponse

from django.views.generic import View


# Create your views here.
def llamar_incio(request):
    return render(request, 'inicio.html')

def llamar_contacto(request):
    return render(request, 'contacto.html')

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html',{'personas':personas})

class ListEmpleadosPdf(View):
    
    def get(self, request, *args, **kwargs):
        personas = Persona.objects.all()
        data = {
            'count': personas.count(),
            'personas': personas
        }
        pdf = render_to_pdf('personas/lista_personas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')