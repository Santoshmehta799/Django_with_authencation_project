from django.urls import path
from models_app import views
from models_app.views import FilterApi, CreateApi


app_name = "models_app"

urlpatterns=[
    path('filters/',views.FilterApi.as_view(), name='filters'),
    path("create/api/", views.CreateApi.as_view(), name='create_api'),
    # path("update/product_type/api/",views.UpdateApi.as_view(), name='update_api'),
    path("update/product_type/api/<uuid:product_type_id>/",views.UpdateApi.as_view(), name='update_api'),
    path('create-price-structure/',views.CraetePriceStructure.as_view(), name="price_structure"),
    path('price_structure/api/<uuid:price_id>/',views.GetpriceStructure.as_view(), name="price_str"),


    # this is learnig url
    path('author-foreign/',views.foreign_get, name="foreign_get"),
    path('author-one/',views.one_get, name="one_get"),
    path('author-many/',views.many_get, name="many_get"),
    path('author-advance/',views.advance_get, name="advance_get"),
    path('image-upload/api/',views.ImageUpload.as_view(), name="advance_get"),
    # path('signals-api/',views.SignalApi.as_view(),name='signal_api'),
    path('signals-api/',views.signal_api,name='signal_api'),
    path('signals-books/api/',views.book_signal_genre, name='signals_book')

]