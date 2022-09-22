from django.db.models import fields
from rest_framework import serializers
from .models import Personas


# definir una clase con la tabla a serializar y los
# campos
class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ["id","nombre","apellido","edad"]