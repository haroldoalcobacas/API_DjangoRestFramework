from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import Review
from reviews.serializers import Reviewserializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = Reviewserializer


class MovieRetrieveUpdateDestroyView(
        generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = Reviewserializer
