from django.contrib import admin

# Register your models here.
from crud.models import StockMarket


@admin.register(StockMarket)
class StockAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__All__'
