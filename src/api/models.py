from django.db import models
from django.core import validators


class Categorie(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    nom = models.CharField(
        max_length=50,
        verbose_name='nom',
        null=False,
        blank=False
    )

    def __str__(self):
        return "{}".format(self.nom)


class Article(models.Model):

    class Meta:
        verbose_name_plural = 'articles'

    nom = models.CharField(
        max_length=50,
        verbose_name='nom',
        null=False,
        blank=False
    )

    ACTIF = 'ACTIF'
    INACTIF = 'INACTIF'
    NON_FACTURABLE = 'NON_FACTURABLE'
    TYPE_CHOICES = (
        (ACTIF, 'actif'),
        (INACTIF, 'inactif'),
        (NON_FACTURABLE, 'non-facturable'),
    )
    _type = models.CharField(
        max_length=10,
        verbose_name='type',
        choices=TYPE_CHOICES,
        default=ACTIF,
        null=False,
        blank=False
    )

    categorie = models.ForeignKey(
        Categorie,
    )

    def __str__(self):
        return "{} {} {}".format(
            self.nom,
            self._type,
            self.categorie
        )


class Fournisseur(models.Model):

    class Meta:
        verbose_name_plural = 'fournisseurs'

    nom = models.CharField(
        max_length=50,
        verbose_name='nom',
        null=False,
        blank=False
    )

    adresse = models.CharField(
        max_length=100,
        verbose_name='adresse',
        null=False,
        blank=False
    )

    telephone = models.CharField(
        max_length=13,
        verbose_name='telephone',
        null=False,
        blank=False
    )

    def __str__(self):
        return "{} {} {}".format(
            self.nom,
            self.adresse,
            self.telephone
        )


class Reduction(models.Model):

    class Meta:
        verbose_name_plural = 'reductions'

    pourcentage = models.PositiveSmallIntegerField(
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(100)],
        default=0
    )

    montant_minimum = models.FloatField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    quantite_minimum = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    chiffre_d_affaire_minimum = models.BigIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    categorie = models.ForeignKey(
        Categorie,
    )

    fournisseur = models.ForeignKey(
        Fournisseur,
    )

    def __str__(self):
        return "{} {} {} {} {} {}".format(
            self.pourcentage,
            self.montant_minimum,
            self.quantite_minimum,
            self.chiffre_d_affaire_minimum,
            self.categorie,
            self.fournisseur
        )


class LigneCatalogue(models.Model):

    class Meta:
        verbose_name_plural = 'ligneCatalogues'

    temps_de_livraison = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    article = models.ForeignKey(
        Article,
    )

    fournisseur = models.ForeignKey(
        Fournisseur,
    )

    def __str__(self):
        return "{} {} {}".format(
            self.temps_de_livraison,
            self.article,
            self.fournisseur
        )


class Prix(models.Model):

    class Meta:
        verbose_name_plural = 'prix'

    montant_minimum = models.FloatField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    quantite_minimum = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    chiffre_d_affaire_minimum = models.BigIntegerField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    prix = models.FloatField(
        validators=[validators.MinValueValidator(0)],
        default=0
    )

    ligneCatalogue = models.ForeignKey(
        LigneCatalogue,
    )

    def __str__(self):
        return "{} {} {} {} {}".format(
            self.montant_minimum,
            self.quantite_minimum,
            self.chiffre_d_affaire_minimum,
            self.prix,
            self.ligneCatalogue
        )
