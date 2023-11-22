from django.contrib import admin

from phonemarket.models import Phones


@admin.register(Phones)
class AdminPhones(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date']
    list_filter = ['lte_exists']
    prepopulated_fields = {'slug': ('name',)}


