from django.urls import path
from .views import producthomepage


urlpatterns = [
    path("all/", producthomepage, name="products"),
    # path("all2/", ProductHomePage.as_view(), name="clas-products"),
    # path("all/<slug:slug>/", productdetailpage, name="products-detail")
]