from django.shortcuts import render
from rest_framework import viewsets
from feedback.models import Reviews
from feedback.serializers import ReviewsSerializer
# Create your views here.
#---------api-----------

class RevewsApi(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    http_method_names = ['get','post']