from django.db import models

# Create your models here.
class PaperInfo(models.Model):
    paperID = models.IntegerField(primary_key=True)
    title = models.TextField()
    arxiv_num = models.CharField(max_length=20)
    pdf_url = models.CharField(max_length=50)
    publicationYear = models.CharField(max_length=4)
    publicationMonth = models.CharField(max_length=2)

class AbstractInfo(models.Model):
    paperID = models.ForeignKey('PaperInfo', on_delete=models.CASCADE)
    abstract = models.TextField()

class AuthorsInfo(models.Model):
    paperID = models.ForeignKey('PaperInfo', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)

class ThemeInfo(models.Model):
    paperID = models.ForeignKey('PaperInfo', on_delete=models.CASCADE)
    theme = models.CharField(max_length=100)