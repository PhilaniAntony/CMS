from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import  Customer,Tag,Product,Order
from .serilizers import CustomerSerializer,TagSerializer,ProductSerializer,OrderSerializer
from .form import CustomerForm,TagForm,ProductForm,OrderForm
from accounts import  models
# Create your views here.

@api_view(['GET'])
def home_view(request):
    api_urls = {
        'register' : '/register/',
        'login' : '/login/',
        'logout' : '/logout/',
        'view_customer': '/customer/<str:pk>/',
        
        'create_product': '/create_product/',
        'products_list': '/products_list/',
        'product_detail': '/product/<str:pk>/',
        
        'update_product': '/product/<str:pk>/',
        'delete_product' : '/product/<str:pk>/',
        
        'tags_list': '/tags/',
        'tag_detail': '/tag/<str:pk>/',
        'create_tag': '/tag/<str:pk>/',
        'update_tag': '/tag/<str:pk>/',
        'delete_tag' : '/tag/<str:pk>/',
        
        'createorder': '/createorder/<str:pk>/',
        'updateorder': '/updateorder/<str:pk>/',
        'deleteorder' : '/deleteorder/<str:pk>/',
        
    }
    return Response(api_urls)





@api_view([ 'POST'])
def createProduct_view(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return(serializer.data)

@api_view(['GET'])
def products_view(request):
    products = Product.objects.all()
    print(products)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def product_view(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view([ 'POST','GET'])
def updateProduct_view(request, pk):
    #try:
    product = Product.objects.get(id=pk)
    #except DoesNotExist:
        #return HttpResponse('product is not available in database yet')
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view([ 'DELETE'])
def deleteProduct_view(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product succesfully deleted')


    

  