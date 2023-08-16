from django.urls import path
from e_commerce.api.mis_api_views import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('inicio/',inicio),
    path('compras/',compras),
    path('productos/',productos),
    path('mas-comics/', get_comics),
    path('comprados/', purchased_item),
]
 