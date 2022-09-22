from django.shortcuts import render
    # dispone de paginas pre-diseñadas para presentar datos
from rest_framework import generics
    # indica el model y campos a serializar
from .serializers import PersonasSerializer
    # cuales seran los datos disponibles en la pagina
from .models import Personas

# Create your views here.
class PersonasViewSet(generics.ListCreateAPIView):
    # cuales son los datos a mostrar
    queryset = Personas.objects.all()
    # como seran serializados
    serializer_class = PersonasSerializer

class PersonasBuscarViewSet(generics.ListAPIView):
    serializer_class = PersonasSerializer
    def get_queryset(self):
        id_persona = self.kwargs['id']
        return Personas.objects.filter(id=id_persona)