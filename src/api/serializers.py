from rest_framework import serializers
from api.serializers import *
from api.models import *


class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie

        fields = (
            'id',
            'nom',
        )

        read_only_fields = (
            'id',
        )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article

        fields = (
           'id',
           'nom',
           '_type',
           'categorie',
        )

        read_only_fields = (
            'id',
        )


class ReductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reduction

        fields = (
            'id',
            'pourcentage',
            'montant_minimum',
            'quantite_minimum',
            'chiffre_d_affaire_minimum',
            'categorie',
            'fournisseur',
        )

        read_only_fields = (
            'id',
        )


class FournisseurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fournisseur

        fields = (
            'id',
            'nom',
            'adresse',
            'telephone',
        )

        read_only_fields = (
            'id',
        )


class PrixSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prix

        fields = (
            'id',
            'montant_minimum',
            'quantite_minimum',
            'chiffre_d_affaire_minimum',
            'prix',
            'ligneCatalogue',
        )

        read_only_fields = (
            'id',
        )


class LigneCatalogueSerializer(serializers.ModelSerializer):

    class Meta:
        model = LigneCatalogue

        fields = (
            'id',
            'temps_de_livraison',
            'article',
            'fournisseur',
        )

        read_only_fields = (
            'id',
        )
