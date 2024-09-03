from django.contrib import admin
# from auth_app_user import models
from models_app import models
from models_app.models import PickUpWarehouseLocation
# Register your models here.

@admin.register(models.PickUpWarehouseLocation)
class PickuplocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plot_no', 'location_name', 'created_at', 'updated_at')
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']
    search_fields = ('id', 'user__user_uuid')


@admin.register(models.Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'slug')
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

@admin.register(models.ProductType)
class ProdutTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'product_quality', 'slug')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_type', 'category', 'product_tittle')

@admin.register(models.PriceStructure)
class PriceStrcutreAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'hsn_code', 'sale_price', 'mrp')

@admin.register(models.ShippingDetails)
class ProductBelongDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_weight', 'return_policy')

@admin.register(models.DropLocation)
class DropLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location_name', 'area', 'street')





# ==============================================================>>>>>>

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'bio')

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_author', 'publication_date')

    def get_author(self,obj):
        return obj.author
    
    get_author.short_description = "Author"

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id', 'website', "get_author")

    def get_author(self, obj):
        return obj.author

    get_author.short_description = "Author"

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'get_book', 'list_of_name','is_genre_book')

    def get_book(self, obj):
        return " =, ".join([book.title for book in obj.books.all()])
    
    get_book.short_description = 'Books' # This sets the column header in the admin list view to "Books."

