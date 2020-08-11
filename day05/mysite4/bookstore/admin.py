from django.contrib import admin

# Register your models here.
from bookstore.models import Book
class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price']
    list_display_links=['title','pub']
    search_fields = ['title','pub']
    list_editable=['market_price']
    list_filter=['pub','price']
admin.site.register(Book,BookManager)

