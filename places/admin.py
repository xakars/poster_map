from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('img', 'get_preview')
    readonly_fields = ['get_preview']

    def get_preview(self, image):
        return mark_safe(f'<img src="{image.img.url}" height="200px" />')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):  # ключевое исправление здесь
    inlines = [ImageInline]
