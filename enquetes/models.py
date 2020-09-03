from django.db import models

class Enquete(models.Model):
    texto = models.CharField(max_length=50)
    data_publicacao = models.DateField(auto_now=True)