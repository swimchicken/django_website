from django.db import models


class shop_item(models.Model):
    name = models.CharField(max_length=100)
    money = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
