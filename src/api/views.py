# coding: utf-8

from api.models import *
from api.serializers import *

from rest_framework import generics
from rest_framework import filters


# Categorie
class ListCreate_Categorie(generics.ListCreateAPIView):
    serializer_class = CategorieSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = Categorie.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_Categorie(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorieSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = Categorie.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Article
class ListCreate_Article(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_Article(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = Article.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Reduction
class ListCreate_Reduction(generics.ListCreateAPIView):
    serializer_class = ReductionSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = Reduction.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_Reduction(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReductionSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = Reduction.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Fournisseur
class ListCreate_Fournisseur(generics.ListCreateAPIView):
    serializer_class = FournisseurSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = Fournisseur.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_Fournisseur(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FournisseurSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = Fournisseur.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Prix
class ListCreate_Prix(generics.ListCreateAPIView):
    serializer_class = PrixSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = Prix.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_Prix(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrixSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = Prix.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# LigneCatalogue
class ListCreate_LigneCatalogue(generics.ListCreateAPIView):
    serializer_class = LigneCatalogueSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    queryset = LigneCatalogue.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroy_LigneCatalogue(
        generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LigneCatalogueSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filter_fields = ['id']
    lookup_url_kwarg = "pk"
    queryset = LigneCatalogue.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
