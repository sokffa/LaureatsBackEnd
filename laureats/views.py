from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from laureats.serializers import *
from laureats.models import *
from rest_framework.views import APIView
from django.http import HttpResponse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.core.mail import EmailMessage
from rest_framework.response import Response
from django.core.mail import EmailMessage
from rest_framework import viewsets,status,permissions,filters
import matplotlib.pyplot as plt
import numpy as np
import mpld3

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LaureatViewSet(viewsets.ModelViewSet):
    queryset = Laureat.objects.all()
    serializer_class = LaureatSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'prenom','cne','email','filiere__libelle','adresse__ville','adresse__pays']
    permission_classes = [permissions.IsAuthenticated]


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdresseViewSet(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer
    permission_classes = [permissions.IsAuthenticated]


class FiliereViewSet(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['libelle']

    
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'prenom','cne','email','filiere__libelle','etablissement']

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'prenom','cne','email','filiere__libelle','profession__libelle']


class EventViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        response = urlopen("http://ensat.ac.ma/Portail/category/evenements")
        html = response.read()
        soup = BeautifulSoup(html)
        liste = soup.find('main', {'class': 'site-main'})
        return HttpResponse(liste, content_type='text/html; charset=utf-8')
class SendEmailViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            msg = EmailMessage(data.get('subject'),
                data.get('message'), to=data.get('emails_list'))
            msg.send()
            return Response({"success": "Sent"})
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)
class StatsViewSet(APIView):
    def get(self, request):
        fig, ax = plt.subplots(subplot_kw=dict(facecolor='#EEEEEE'))
        N = 100

        scatter = ax.scatter(np.random.normal(size=N),
                            np.random.normal(size=N),
                            c=np.random.random(size=N),
                            s=1000 * np.random.random(size=N),
                            alpha=0.3,
                            cmap=plt.cm.jet)
        ax.grid(color='white', linestyle='solid')

        ax.set_title("Scatter Plot (with tooltips!)", size=20)

        labels = ['point {0}'.format(i + 1) for i in range(N)]
        tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
        mpld3.plugins.connect(fig, tooltip)

        
        return HttpResponse(mpld3.fig_to_html(fig), content_type='text/html; charset=utf-8')
