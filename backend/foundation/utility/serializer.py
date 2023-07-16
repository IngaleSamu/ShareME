from rest_framework import serializers
from django.apps import apps

# def create_serializer_class(model_name, many=False):
#     entity = apps.get_model(app_label=apps.get_model, model_name=model_name)
#     class DynamicSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = entity
#             fields = '__all__'
#     if many:
#         return DynamicSerializer(many=True)
#     else:
#         return DynamicSerializer



def model_serializer(model_class, data=None, querySet=None):
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'

    if data is not None:
        serializer = ModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer

    if querySet is not None:
        serializer = ModelSerializer(querySet, many=True)
        serializedData = serializer.data
        return serializedData

    return ModelSerializer