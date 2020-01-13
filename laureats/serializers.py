from django.contrib.auth.models import User, Group
from rest_framework import serializers
from laureats.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LaureatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laureat
        fields = "__all__"

class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    laureats = serializers.HyperlinkedIdentityField(many=True,view_name='laureat-detail')     
    class Meta:
        model = Promotion
        fields = ['laureats','annee_scolaire']

class AdresseSerializer(serializers.HyperlinkedModelSerializer):
    laureats = serializers.HyperlinkedIdentityField(many=True,view_name='laureat-detail')     
    class Meta:
        model = Adresse
        fields = ['laureats','id','pays','ville','adresse','zip_code']

class FiliereSerializer(serializers.HyperlinkedModelSerializer):
    laureats = serializers.HyperlinkedIdentityField(many=True,view_name='laureat-detail')     
    class Meta:
        model = Filiere
        fields = ['laureats','libelle']

class EtudiantSerializer(serializers.HyperlinkedModelSerializer):
    #laureat = LaureatSerializer(read_only=True)      
    class Meta(LaureatSerializer.Meta):
        model = Etudiant

class EmployeSerializer(serializers.HyperlinkedModelSerializer):
    laureats = LaureatSerializer(many=True, read_only=True)      
    class Meta(LaureatSerializer.Meta):
        model = Employe


class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    employes =  serializers.HyperlinkedIdentityField(many=True,view_name='employe-detail')           
    class Meta:
        model = Profession
        fields = ['employes','libelle']

class ContactSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    emails_list = serializers.ListField()

