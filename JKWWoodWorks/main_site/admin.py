from django.contrib import admin

# Import the needed models.
from .models import Image, Product, Plan, Request, Video

# Register your models here.


class RequestAdmin(admin.ModelAdmin):
    """Request Admin
    The class controls how Requests will appear in the admin.
    """
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "comment",
        "sent_time",
    )


class ImageAdmin(admin.ModelAdmin):
    """Image Admin
    The class controls how images will appear in the admin field.
    """
    readonly_fields = (
        "date_created",
    )


class VideoAdmin(admin.ModelAdmin):
    """Video Admin
    The class controls how videos will appear in the admin field.
    """
    readonly_fields = (
        "date_created",
    )


# Register all the models that need to appear in admin.
admin.site.register(Product)
admin.site.register(Plan)
admin.site.register(Request, RequestAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)