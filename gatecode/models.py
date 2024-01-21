from django.db import models


class addGate(models.Model):
    complex = models.CharField(max_length=30)
    code = models.CharField(max_length=7)
    address = models.CharField(max_length=30, blank=True, null=True)


    class Meta:
        ordering = ['complex']

    def __str__(self):
        return f"{self.complex}"

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    # @property
    # def fullname(self):
    #     return f"{self.complex}"
