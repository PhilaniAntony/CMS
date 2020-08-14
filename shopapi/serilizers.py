from accounts.models import  Customer,Product,Tag,Order
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customer
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tag
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Order
        fields = '__all__'