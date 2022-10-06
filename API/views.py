from django.shortcuts import render
    # dispone de paginas pre-diseñadas para presentar datos
from rest_framework import generics, status
    # indica el model y campos a serializar
from .serializers import PersonasSerializer
    # cuales seran los datos disponibles en la pagina
from .models import Personas
from rest_framework.response import Response

# Create your views here.
class PersonasViewSet(generics.ListCreateAPIView):
    # cuales son los datos a mostrar
    queryset = Personas.objects.all()
    # como seran serializados
    serializer_class = PersonasSerializer

class PersonasBuscarViewSet(generics.ListCreateAPIView):
    serializer_class = PersonasSerializer
    def get_queryset(self):
        id_persona = self.kwargs['id']
        return Personas.objects.filter(id=id_persona)

class PersonasEliminarViewSet(generics.DestroyAPIView):
    serializer_class = PersonasSerializer
    def get_queryset(self):
        id_persona = self.kwargs['id']
        return Personas.objects.filter(id=id_persona)
    def delete(self,request,id=None):
        id_persona = id
        print('--'+id_persona)
        p = Personas.objects.filter(id=id_persona)
        if p:
            p.delete()
            return Response({'message':'producto eliminado'},status = status.HTTP_200_OK)
        return Response({'error':'no existen reg con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

class PersonasModificarViewSet(generics.UpdateAPIView):
    serializer_class = PersonasSerializer
    def get_queryset(self):
        id_persona = self.kwargs['id']
        return Personas.objects.filter(id=id_persona)
    def delete(self,request,id=None):
        id_persona = id
        print('--'+id_persona)
        p = Personas.objects.filter(id=id_persona)
        if p:
            p.delete()
            return Response({'message':'producto eliminado'},status = status.HTTP_200_OK)
        return Response({'error':'no existen reg con estos datos'}, status = status.HTTP_400_BAD_REQUEST)