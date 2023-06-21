import django.contrib.admin
from rest_framework import serializers

from . import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = django.contrib.admin.ModelAdmin
        fields = '__all_'

