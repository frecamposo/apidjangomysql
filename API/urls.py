from django.urls import include, re_path
from rest_framework import urlpatterns
from API import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    re_path(r'^api/personas/$',csrf_exempt(views.PersonasViewSet.as_view())),
    re_path(r'^api/personas/(?P<id>.+)/$',csrf_exempt(views.PersonasBuscarViewSet.as_view())),
    re_path(r'^api/personas_eliminar/(?P<id>.+)/$',csrf_exempt(views.PersonasEliminarViewSet.as_view())),
]

urlpatterns=format_suffix_patterns(urlpatterns)