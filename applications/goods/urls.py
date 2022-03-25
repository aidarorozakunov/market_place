from django.urls import path

from applications.goods.views import GoodsListView, GoodsDetailView, FavoriteView

urlpatterns = [
    path('', GoodsListView.as_view()),
    path('<int:pk>/', GoodsDetailView.as_view()),
    path('<int:pk>/favorite/', FavoriteView.as_view()),
]