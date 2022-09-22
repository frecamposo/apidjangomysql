from django.urls import include, re_path
from rest_framework import urlpatterns
from API import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^api/personas/$',views.PersonasViewSet.as_view()),
    re_path(r'^api/personas/(?P<id>.+)/$',views.PersonasBuscarViewSet.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)