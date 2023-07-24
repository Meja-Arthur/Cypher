# serializer is the place where we turn the information into json so that we can use it in the frontend part of 
# of our webframework

from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )
        
        
class CategorySerializer(serializers.ModelSerializer):
    # getting all the product connected to this category here 
    products = ProductSerializer(many="True")
    
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )
               