from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from laureats.serializers import *
from laureats.models import *
from rest_framework.views import APIView
from django.http import HttpResponse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework import permissions



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
    
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [permissions.IsAuthenticated]


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
            print("LE SERIALIZER :")
            print(data.get('emails_list'))
            print("END OF  SERIALIZER :")
            msg = EmailMessage(data.get('subject'),
                data.get('message'), to=data.get('emails_list'))
            msg.send()
            return Response({"success": "Sent"})
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)
