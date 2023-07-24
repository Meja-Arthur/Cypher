from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Product, Category
from.serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view



class LatestProductsList(APIView):
    
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    


class ProductDetail(APIView): 
    # we are using the get_object function that 
    def get_object(self, category_slug, product_slug): 
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
              
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    
class CategoryDetail(APIView):
    def get_object(self, category_slug): 
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug,format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)    
        
        
@api_view(['POST'])# since the method is post  and since we want to use simple fucntion views 
def search(request):
    query = request.data.get('query', '')        
    
    if query:
        # Q allow us to do some advanced searching in our objects 
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serilizer = ProductSerializer(products, many=True)
        return Response(serilizer.data)
    else:
        # if the query is empty we return an empty product list 
        return Response({"products": []})
    