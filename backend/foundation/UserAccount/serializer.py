from rest_framework import serializers
from .models import User
from .Entity.userSearch import SearchParameter

class DynamicSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        search_param = args[0] if args else kwargs.get('instance', None)
        if search_param:
            hints = search_param.__annotations__
            for field_name, field_type in hints.items():
                serializer_field = self.get_serializer_field(field_type)
                self.fields[field_name] = serializer_field

    def get_serializer_field(self, field_type):
        if field_type == str:
            return serializers.CharField(required=False)
        elif field_type == bool:
            return serializers.BooleanField(required=False)
        elif field_type == int:
            return serializers.IntegerField(required=False)
        elif field_type == float:
            return serializers.FloatField(required=False)
        else:
            return serializers.CharField(required=False)


class SearchParameterSerializer(serializers.Serializer):
    attributes = DynamicSerializer(source='*')

    def to_internal_value(self, data):
        return SearchParameter(**data)

    def to_representation(self, instance):
        return instance.__dict__


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