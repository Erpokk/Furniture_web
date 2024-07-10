from django.contrib import admin

from carts.admin import CartTabAdmin
from carts.models import Cart
from users.models import User

admin.site.unregister(User)


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    # Connect cart with user
    inlines = [
        CartTabAdmin,
    ]
