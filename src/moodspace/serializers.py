from rest_framework import serializers
from .models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('id', 'title', 'description', 'type_rec')

    #python manage.py dumpdata moodspace.Vibe moodspace.Recommendation --indent 4 > moodspace/fixtures/data.json