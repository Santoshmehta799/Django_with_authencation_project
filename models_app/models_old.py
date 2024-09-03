import uuid
from django.db import models
from django.db.models import TextChoices
from auth_app_user.models import ModelMixin, User
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

class ProductQualityEnums(TextChoices):
    GOOD = ('GOOD', 'good')
    BAD = ('BAD', 'bad')


# Create your models here.
class PickUpWarehouseLocation(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wearhouselocatoin")
    plot_no = models.CharField(max_length=100, null=True, blank=True)
    location_name = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    class Meta:
        verbose_name = _('App Model - pickupwearhouselocation')
        verbose_name_plural = _('App Model - pickupwearhouselocation')

    def __str__(self):
        return f"{self.location_name}"
    
    
class Category(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = _('App Model - Category')
        verbose_name_plural = _('App Model - Category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
    
    
class ProductType(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_type')
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    product_quality = models.CharField(max_length=255, choices=ProductQualityEnums.choices)

    class Meta:
        verbose_name = "Model App - ProductType"
        verbose_name_plural = 'Model App - ProductType'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductType,self).save(*args, **kwargs)

    def __str__(self) :
        return f"{self.id}"


class Product(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product_product_type')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    product_tittle = models.CharField(max_length=255, null=True, blank=True)
    about_the_brand = models.CharField(max_length=2000,blank=True,null=True)
    product_brand = models.CharField(max_length=2000,blank=True, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name = "Model App - Product"
        verbose_name_plural = 'Model App - Product'
        # unique_together = ('')
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.product_tittle}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_tittle)
        super(Product, self).save(*args, **kwargs)


class PriceStructure(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_price_structure')
    hsn_code = models.CharField(max_length=10, null=True, blank=True)
    sale_price = models.CharField(max_length=10, null=True, blank=True)
    mrp = models.CharField(max_length=10, null=True, blank=True)
    tax_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
    
    class Meta:
        verbose_name = "Model App - Price Structure"
        verbose_name_plural = 'Model App - Price Structure'


class ShippingDetails(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pick_up_location = models.ManyToManyField(PickUpWarehouseLocation, max_length=255, blank=True, related_name='shipping_detail')
    product_weight = models.CharField(max_length=125, blank=True,null=True)
    return_policy = models.CharField(max_length =555,default=True,blank=True, null=True)
    packed_box_dimensions_length = models.CharField(max_length=100,blank=True,null=True)
    packed_box_dimensions_height = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.pick_up_location}"
    
    class Meta:
        verbose_name = "Model App - Shipping Detail"
        verbose_name_plural = 'Model App - Shipping Detail'


class DropLocation(ModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pickup_location = models.ForeignKey(PickUpWarehouseLocation, on_delete=models.CASCADE, related_name='drop_location')
    location_name = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
    
    class Meta:
        verbose_name = "Model App - Drop Location"
        verbose_name_plural = 'Model App - Drop Location'









