from drf_yasg import openapi
from drf_yasg.inspectors import FieldInspector, swagger_settings
from dataclasses import dataclass
from typing import Type, get_type_hints


class DataclassInspector(FieldInspector):
    def field_to_swagger_object(self, field, swagger_object_type, use_references, **kwargs):
        if dataclass := self.get_dataclass(field):
            return self.probe_field(dataclass, use_references, **kwargs)
        return super().field_to_swagger_object(field, swagger_object_type, use_references, **kwargs)

    def get_dataclass(self, field):
        if hasattr(field, '__args__') and len(field.__args__) == 1:
            arg = field.__args__[0]
            if isinstance(arg, Type) and dataclass(arg):
                return arg
        return None

    def probe_field(self, dataclass, use_references, **kwargs):
        schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=self.probe_fields(dataclass),
            **kwargs
        )
        return schema