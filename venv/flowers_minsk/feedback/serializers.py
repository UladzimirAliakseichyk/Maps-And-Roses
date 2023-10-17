from rest_framework import serializers

from .models import Reviews

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['review','shop','user','rating','date_time']