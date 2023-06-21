from rest_framework import viewsets

from . import models
from . import serializers


# Create your views here.
class QuestionView(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class ChoiceView(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer





