from rest_framework import serializers

from apps.ielts import models as ielts_models
from .ielts_test import IeltsTestSerializer


class IeltsSubModuleDetailSerializer(serializers.ModelSerializer):
    tests = IeltsTestSerializer(many=True)

    class Meta:
        model = ielts_models.IeltsSubModule
        fields = (
            "id",
            "title",
            "difficulty",
            "tests",
            "order",
        )
