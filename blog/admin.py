from django.contrib import admin
from blog.models import Artical
from django.utils.safestring import mark_safe
from django.core.exceptions import (ValidationError)

# Register your models here.


@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['title','summary','pushed']

    def get_object(self, request, object_id, from_field=None):
        """
        Return an instance matching the field and value provided, the primary
        key is used if no field is provided. Return ``None`` if no match is
        found or the object_id fails validation.
        """
        queryset = self.get_queryset(request)
        model = queryset.model
        field = model._meta.pk if from_field is None else model._meta.get_field(from_field)
        try:
            object_id = field.to_python(object_id)
            a = queryset.filter(**{field.name: object_id}).first()
            a.content = a.content_display
            return a
        except (model.DoesNotExist, ValidationError, ValueError):
            return None

    class Media:
        js = [
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh-CN.js',
            'js/kindeditor/config.js'
        ]