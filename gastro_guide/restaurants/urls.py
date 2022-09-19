from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RestaurantListCreateAPIView, ReviewAPIView

router = DefaultRouter()
router.register('all-restaurants', RestaurantListCreateAPIView,),
router.register('reviews', ReviewAPIView,)

urlpatterns = [
    path('', include(router.urls)),
]
