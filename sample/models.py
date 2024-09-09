from django.db import models

from models.GyazoImageField import GyazoImageField


class SampleUserProfileModel(models.Model):
    class Meta:
        verbose_name = "SampleUserProfileModel"
        verbose_name_plural = "SampleUserProfileModels"

    name = models.CharField(max_length=255)

    age = models.PositiveIntegerField()

    profile_image = GyazoImageField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
