from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError

from .models import Restaurant, Reviews
from .permissions import IsConfirmedOrReadOnly, IsOwnerOrReadOnly
from .serializers import RestaurantSerializer, ReviewSerializer


class RestaurantListCreateAPIView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class ReviewAPIView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permisssion_class = [IsConfirmedOrReadOnly]
