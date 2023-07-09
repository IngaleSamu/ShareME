from rest_framework import serializers
from django.apps import apps

def create_serializer_class(model_name, many=False):
    entity = apps.get_model(app_label=apps.get_model, model_name=model_name)
    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = entity
            fields = '__all__'
    if many:
        return DynamicSerializer(many=True)
    else:
        return DynamicSerializer
