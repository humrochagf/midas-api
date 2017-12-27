from rest_framework import viewsets

from .models import Board, Entry, Tag
from .serializers import BoardSerializer, EntrySerializer, TagSerializer


class BoardViewset(viewsets.ModelViewSet):

    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.visible_by(self.request.user)


class EntryViewset(viewsets.ModelViewSet):

    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.visible_by(self.request.user)


class TagViewset(viewsets.ModelViewSet):

    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.visible_by(self.request.user)
