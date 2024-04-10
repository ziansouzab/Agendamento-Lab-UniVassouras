from rest_framework import generics, status
from .serializers import AgendaSerializer, SalaSerializer
from rest_framework.views import APIView
from .models import Agenda, Sala
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView




class CreateView(generics.ListCreateAPIView):   
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer        

    def perform_create(self, serializer):
        """Salva os dados do post e cria uma nova Agenda."""                        
        serializer.save()     

    def get(self, request, format=None):
        agendas = Agenda.objects.all()
        sala_id = request.GET.get('sala')
        if(sala_id != None):
            agendas = agendas.filter(sala=sala_id)
        
        data_inicial = request.GET.get('data_inicial')
        data_final = request.GET.get('data_final')
        
        if(data_inicial != None and data_final != None):
            agendas = agendas.filter(date_init__gte=data_inicial)\
                .filter(date_init__lte=data_final)\
        
        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data)
       

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer


class CreateView(ListCreateAPIView):   
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def perform_create(self, serializer):
        """Salva os dados do post e cria uma nova Sala."""
        serializer.save()

class DetailsView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
