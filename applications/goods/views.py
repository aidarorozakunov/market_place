from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.models import Profile
from applications.goods.models import Goods
from applications.goods.serializers import GoodsSerializer


class GoodsPriceFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='lte')

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
    # filterset_fields = ['category', 'price', ]
    search_fields = ['title', 'description', ]


    def get_serializer_context(self):
        return {'request': self.request}


class GoodsDetailView(generics.RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        profile = Profile.objects.get(user=request.user.id)
        if profile.favorite.filter(id=pk).exists():
            profile.favorite.set(profile.favorite.exclude(id=pk))
            msg = 'Goods was deleted from favorites!'
        else:
            profile.favorite.add(pk)
            profile.save()
            msg = 'Goods added to favorite successfully!'
        return Response(msg, status=status.HTTP_200_OK)



