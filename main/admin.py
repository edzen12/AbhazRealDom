from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import City, PostRentSale, ImageShots, Reviews


class ImageShotsInline(admin.TabularInline):
    model = ImageShots
    extra = 3
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class PostRentSaleAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'rent_sale', 'status', 'type_property', 'areas', 'price', 'vip']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    readonly_fields = ("get_image",)
    inlines = [ImageShotsInline, ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="220" height="180"')

    get_image.short_description = "Изображение"


admin.site.register(PostRentSale, PostRentSaleAdmin)
admin.site.register(City)
admin.site.register(Reviews)


@admin.register(ImageShots)
class ImageShotsAdmin(admin.ModelAdmin):
    list_display = ("rs_objects", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="60"')

    get_image.short_description = "Изображение"
