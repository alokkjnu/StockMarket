from django.urls import path
from . import views

app_name = "StockMarket"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('load-more', views.load_more, name='load-more'),
    path('<int:id>/<slug>/', views.stock_detail, name='stock_detail'),
    path('query/', views.query, name='query'),
    path('admin/query/<int:query_id>/',views.admin_query_detail, name='admin_query_detail')
]
