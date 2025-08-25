from .models import Author, Book
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .serializer import AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @extend_schema(
        summary="Список книг",
        description="Возвращает полный список книг",
        tags=['Books']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Создание книги",
        description="Создаёт новую книгу и возвращает созданный объект",
        tags=['Books']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Конкретная книга",
        description="Возвращает информацию о конкретной книге",
        tags=['Books']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление книги",
        description="Обновляет данные книги",
        tags=['Books']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление книги",
        description="Частично обновляет данные книги",
        tags=['Books']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление книги",
        description="Удаляет книгу",
        tags=['Books']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @extend_schema(
        summary="Список авторов",
        description="Возвращает список всех авторов",
        tags=['Authors'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Создание автора",
        description="Создаёт нового автора и возвращает созданный объект",
        tags=['Authors'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Конкретный автор",
        description="Возвращает информацию о конкретном авторе",
        tags=['Authors'],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновление автора",
        description="Обновляет данные автора ",
        tags=['Authors'],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление автора",
        description="Частично обновляет данные автора",
        tags=['Authors'],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление автора",
        description="Удаляет автора",
        tags=['Authors'],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)