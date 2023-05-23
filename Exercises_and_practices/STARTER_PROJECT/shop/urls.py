from django.urls import path, re_path, register_converter
from shop import  views
from shop.converter import FiveDigitConverter
#from  import views as _views
register_converter(FiveDigitConverter, 'yyyy') # 5 digit 20223

urlpatterns = [
    path ("", views.index),
    path("browse/", views.shop_list, name='_list'),
    path ("<int:item_id>/", views.shop_item, name="item"), 
    path("<str:term>/", views.shop_search),
    path("<slug:keyword>/", views.shop_slug),
   # path("<uuid:key_uuid>/", views.shop_uuid),
    path("articles/year/<yyyy:year>/", views.shop_article_list),
    path("articles/<int:month>/", views.shop_article_list_version_2, {'is_int': True}),
    path("articles/<str:month>/", views.shop_article_list_version_2, {'is_int': False}), # January-->jan, feb


    #re_path("/artiles/year/([0-9]{4})/", views.shop_artile_list) ,
    re_path("/validate/phone/([0-9]{8})/", views.shop_validate_phone),


]
