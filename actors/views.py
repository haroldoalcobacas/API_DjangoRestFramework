from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from actors.models import Actor
from actors.serializers import ActorsSerializer
from app.permissions import GlobalDefaultPermission


class ActorCreateListView(generics.ListCreateAPIView):
    # o permission_classe é utilizado para genrenciara as permissões
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer


class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer
