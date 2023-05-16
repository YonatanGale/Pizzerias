from rest_framework import serializers
from .models import Pizzeria
from rest_framework.reverse import reverse

class PizzeriaListSerializer (serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = [
                    'id', 
                    'logo_image', 
                    'pizzeria_name', 
                    'city', 
                    'zip_code',
                    'absolute_url',
                ]
        
    def get_absolute_url(self, obj):
        return reverse('pizzeria_detail', args=(obj.pk,))

class PizzeriaDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = ['id',
                  'pizzeria_name',
                  'street',
                  'city',
                  'state',
                  'zip_code',
                  'website',
                  'phone_number',
                  'description',
                  'logo_image',
                  'email',
                  'active',
                  'update',]
        
    def get_update(self, obj):
        return reverse('pizzeria_update', args=(obj.pk,))