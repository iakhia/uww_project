from django.db import models


class Tournament(models.Model):
    name = models.CharField('Название', max_length = 50)
    image = models.FileField(upload_to='img/')
    address = models.CharField('Адрес', max_length = 100)
    date = models.CharField('Дата', max_length = 20)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"


