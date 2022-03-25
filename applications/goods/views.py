from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination

from applications.goods.models import Goods
from applications.goods.serializers import GoodsSerializer


class GoodsPriceFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = [
            'min_price',
            'max_price',
            'category',
        ]


class GoodsListView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = GoodsPriceFilter

    search_fields = ['title', 'description', ]

    def get_serializer_context(self):
        return {'request': self.request}

class GoodsDetailView(generics.RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

