from django.db import models


class AptMap(models.Model):
    complex_name = models.CharField(max_length=30)
    complex_address = models.CharField(max_length=40)
    complex_map = models.ImageField(upload_to='maps')

    class Meta:
        ordering = ['complex_name']

    def __str__(self):
        return f"{self.complex_name}"

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)