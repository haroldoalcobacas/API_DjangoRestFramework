
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from app.permissions import GlobalDefaultPermission
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# utilizando função
# @csrf_exempt
# def genre_detail_view(request, pk):
#    genre = get_object_or_404(Genre, pk=pk)
#    if request.method == 'GET':
#        data = {'id': genre.id, 'name':genre.name}
#        return JsonResponse(data)
#    elif request.method == 'PUT':
#        data = json.loads(request.body.decode('utf-8'))
#        genre.name = data['name']
#        genre.save()
#        return JsonResponse(
#            {'id': genre.id,'name': genre.name},
#            status=200,
#        )
#    elif request.method == 'DELETE':
#        genre.delete()
#        return JsonResponse(
#            {'message': 'Gênero excluído com sucesso!.'},
#            status=204,
#       )
