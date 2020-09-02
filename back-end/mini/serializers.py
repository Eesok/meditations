from rest_framework import serializers
from .models import Meditation, Benefit


class MeditationSerializer(serializers.HyperlinkedModelSerializer):
    benefits = serializers.HyperlinkedRelatedField(
        view_name='benefit_detail',
        many=True,
        read_only=True
    )
    meditation_url = serializers.ModelSerializer.serializer_url_field(
        view_name='meditation_detail'
    )

    class Meta:
        model = Meditation
        fields = ('id', 'description', 'photo_url',
                  'practice', 'origin', 'benefits', 'meditation_url',)


class BenefitSerializer(serializers.HyperlinkedModelSerializer):
    meditation = serializers.HyperlinkedRelatedField(
        view_name='meditation_detail',
        read_only=True
    )
    meditation_id = serializers.PrimaryKeyRelatedField(
        queryset=Meditation.objects.all(),
        source='meditation'
    )

    class Meta:
        model = Benefit
        fields = ('id', 'meditation_id', 'benefit',
                  'meditation',)
