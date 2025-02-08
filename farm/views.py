from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from farm.models import Product,Order
from rest_framework import serializers
# Create your views here.
def home(request):
    return HttpResponse("Home page of farm")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def farmProduct(request,id=None):
    if request.method=='GET':
        products=Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method=="PUT" or request.method=="PATCH":
        product = get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product, data=request.data,partial=(request.method=="PATCH"))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors,status=400)
    if request.method=="DELETE":
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=204)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def manageOrder(request, id=None):
    if request.method=="GET":
        orders=Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method=="POST":
        if request.data["customer"]==request.user.id:
            serializer=OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors,status=400)
        else:
            return Response("Invalid user id")
    if request.method=="PUT" or request.method == "PATCH":
        order = get_object_or_404(Order,pk=id)
        serializer=OrderSerializer(order,data=request.data, partial=(request.method=="PATCH"))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    if request.method=="DELETE":
        order = get_object_or_404(Order,pk=id)
        order.delete()
        return Response({"message":"order deleted successfully"},status=204)
