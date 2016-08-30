from django.conf.urls import include
from django.conf.urls import url

from api import views

urlpatterns = [
    # Categorie
    url(
        r'^categories/$',
        views.ListCreate_Categorie.as_view(),
        name='ListCreate_Categorie_api'
    ),
    url(
        r'^categories/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_Categorie.as_view(),
        name='RetrieveUpdateDestroy_Categorie_api'
    ),
    # Article
    url(
        r'^articles/$',
        views.ListCreate_Article.as_view(),
        name='ListCreate_Article_api'
    ),
    url(
        r'^articles/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_Article.as_view(),
        name='RetrieveUpdateDestroy_Article_api'
    ),
    # Reduction
    url(
        r'^reductions/$',
        views.ListCreate_Reduction.as_view(),
        name='ListCreate_Reduction_api'
    ),
    url(
        r'^reductions/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_Reduction.as_view(),
        name='RetrieveUpdateDestroy_Reduction_api'
    ),
    # Fournisseur
    url(
        r'^fournisseurs/$',
        views.ListCreate_Fournisseur.as_view(),
        name='ListCreate_Fournisseur_api'
    ),
    url(
        r'^fournisseurs/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_Fournisseur.as_view(),
        name='RetrieveUpdateDestroy_Fournisseur_api'
    ),
    # Prix
    url(
        r'^prix/$',
        views.ListCreate_Prix.as_view(),
        name='ListCreate_Prix_api'
    ),
    url(
        r'^prix/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_Prix.as_view(),
        name='RetrieveUpdateDestroy_Prix_api'
    ),
    # LigneCatalogue
    url(
        r'^lignecatalogues/$',
        views.ListCreate_LigneCatalogue.as_view(),
        name='ListCreate_LigneCatalogue_api'
    ),
    url(
        r'^lignecatalogues/(?P<pk>\d+)$',
        views.RetrieveUpdateDestroy_LigneCatalogue.as_view(),
        name='RetrieveUpdateDestroy_LigneCatalogue_api'
    ),
]
