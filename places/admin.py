from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('img', 'get_preview')
    readonly_fields = ['get_preview']

    def get_preview(self, image):
        return mark_safe('<img src="{url}" height="200px" />'.format(url=image.img.url))


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

