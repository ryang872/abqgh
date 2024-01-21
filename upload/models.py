from django.db import models
from .validators import validate_file_size
from django.contrib.auth import get_user_model


class noTip(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=4)
    address = models.CharField(max_length=30, blank=True, null=True)
    screenshot = models.ImageField(upload_to='sc', validators=[validate_file_size], blank=True)
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


    class Meta:
        ordering = ['first']

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)

    def __str__(self):
        return f"{self.first} {self.last}"

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    @property
    def fullname(self):
        return f"{self.first} {self.last}"





