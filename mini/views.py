from rest_framework import generics
from .serializers import MeditationSerializer, BenefitSerializer
from .models import Meditation, Benefit


class MeditationList(generics.ListCreateAPIView):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer


class MeditationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meditation.objects.all()
    serializer_class = MeditationSerializer


class BenefitList(generics.ListCreateAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class BenefitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
