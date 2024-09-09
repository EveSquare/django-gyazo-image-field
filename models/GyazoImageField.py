import os
import re

import requests
from django.core.files import File
from django.db import models
from django.db.models import FileField
from django.utils.translation import gettext_lazy as _

from forms.fields import GyazoImageFile


def upload_new_file(image_data: bytes) -> GyazoImageFile:
    access_token = os.environ.get("GYAZO_ACCESS_TOKEN")
    if not access_token:
        raise Exception(_("GYAZO_ACCESS_TOKEN is not set."))
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.post(
        "https://upload.gyazo.com/api/upload",
        files={
            "imagedata": image_data,
        },
        headers=headers,
        # data={
        #     "metadata_is_public": False,
        # },
    )

    if response.status_code != 200:
        raise Exception(_("Failed to upload file to Gyazo."))
    return GyazoImageFile(**response.json())


class GyazoImageField(models.Field):
    default_error_messages = {
        "invalid": _("“%(value)s” is not a valid image file."),
    }
    description = _("File field on Gyazo.")
    empty_strings_allowed = False
    max_length = 512

    def __init__(
        self,
        verbose_name=None,
        **kwargs,
    ):
        kwargs["max_length"] = self.max_length
        super().__init__(verbose_name, **kwargs)

    def db_type(self, connection):
        return f"char({self.max_length})"

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def get_internal_type(self):
        return "GyazoImageField"

    def get_prep_value(self, value):
        if not value:
            return None
        if not (isinstance(value, File) or isinstance(value, GyazoImageFile)):
            raise Exception("Value is not valid file.")

        is_new_file = isinstance(value, File)
        if is_new_file:
            object_name = upload_new_file(
                image_data=value.read(),
            )
            return super().get_prep_value(object_name)

        return super().get_prep_value("hoge")

    def from_db_value(self, value, expression, connection):
        if not value:
            return None
        value = re.sub(r"\ *$", "", value)
        return GyazoImageFile(
            type="",
            thumb_url="",
            created_at="",
            image_id="",
            permalink_url="",
            url="",
        )

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": FileField,
                **kwargs,
            }
        )
