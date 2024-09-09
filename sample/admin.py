from django.contrib import admin

from sample.models import SampleUserProfileModel


@admin.register(SampleUserProfileModel)
class SampleUserProfileModelAdmin(admin.ModelAdmin):
    pass
