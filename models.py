

class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=150)
    image = models.FileField(upload_to='image_categorie',)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class Sous_categorie(models.Model):
    """Model definition for Sous_categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='categorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Sous_categorie."""

        verbose_name = 'Sous_categorie'
        verbose_name_plural = 'Sous_categories'

    def __str__(self):
        """Unicode representation of Sous_categorie."""
        return self.nom


class Entreprise(models.Model):
"""Model definition for Entreprise."""

    # TODO: Define fields here
    sous_categorie = models.ForeignKey(Sous_categorie, on_delete=models.CASCADE, related_name='sous_categorie')
    adresse_geo = models.CharField(max_length=255)
    adresse_postal = models.CharField(max_length=255)
    ville = models.CharField(max_length=50)
    tel = models.PositiveIntegerField()
    fax = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    site = models.URLField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_updt = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Entreprise."""

        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'
