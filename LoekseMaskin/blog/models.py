from django.db import models

class blog(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=20, default="Tittel", null=False)
    leadParagraph = models.TextField(max_length=200, default="Ingress", null=False)
    article = models.TextField(max_length=2000, default="Artikkel", null=False)
    publishedDate = models.DateField(null=False)

    class Meta:
        verbose_name_plural = "Bloggartikler"
    def __str__(self):
        return self.headline
