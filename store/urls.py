from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')

router.register('collections', views.CollectionViewSet, basename='collection')
router.register('carts', views.CartViewSet, basename='cart')
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('orders', views.OrderViewSet, basename='order')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images',views.ProductImageViewSet, basename='product-image')
products_router.register('review', views.ReviewViewSet, basename='product-review')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart' )
carts_router.register('items',views.CartItemViewSet, basename="cart-item")

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
