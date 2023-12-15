from django.contrib import admin

# Register your models here.
from .models import Manufactures, Categories, Products, Books, Posts, Comments

@admin.register(Manufactures)
class ManufacturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    list_filter = ('name', 'created_date')
    search_fields = ('name', 'created_date')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacture', 'created_date')
    list_filter = ('name', 'manufacture', 'created_date')
    search_fields = ('name', 'manufacture', 'created_date')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'manufacture', 'category', 'product_url', 'created_date')
    list_filter = ('name', 'sku', 'manufacture', 'category', 'product_url', 'created_date')
    search_fields = ('name', 'sku', 'manufacture', 'category', 'product_url', 'created_date')


class Posts(admin.TabularInline):
    model = Posts

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    inlines=[Posts]
    list_display = ('title', 'sub_title', 'author', 'description', 'language', 'product', 'book_image', 'book_file', 'created_date')
    # list_filter = ('title', 'sub_title', 'author', 'description', 'language', 'product', 'book_image', 'book_file', 'created_date')
    # search_fields = ('title', 'sub_title', 'author', 'description', 'language', 'product', 'book_image', 'book_file', 'created_date')

# @admin.register(Posts)
# class PostsAdmin(admin.ModelAdmin):
#     list_display = ('chapter_name', 'chapter_content', 'book', 'created_date', 'chapter_vorder', 'chapter_horder', 'chapter_type')
#     list_filter = ('chapter_name', 'chapter_content', 'book', 'created_date', 'chapter_vorder', 'chapter_horder', 'chapter_type')
#     search_fields = ('chapter_name', 'chapter_content', 'book', 'created_date', 'chapter_vorder', 'chapter_horder', 'chapter_type')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'created_date')
    list_filter = ('comment', 'post', 'created_date')
    search_fields = ('comment', 'post', 'created_date')
