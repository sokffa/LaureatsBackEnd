from django.urls import include, path
from rest_framework import routers
from laureats import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'laureats', views.LaureatViewSet,basename='laureat')
router.register(r'promotions', views.PromotionViewSet)
router.register(r'adresses', views.AdresseViewSet)
router.register(r'filieres', views.FiliereViewSet)
router.register(r'etudiants', views.EtudiantViewSet)
router.register(r'employes', views.EmployeViewSet,basename='employe')
router.register(r'professions', views.ProfessionViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'events/', views.EventViewSet.as_view()),
    path(r'send_email/', views.SendEmailViewSet.as_view()),
]