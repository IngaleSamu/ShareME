from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Car
from .serializer import ModelSerializer
# from ..utility.serializer import create_serializer_class


def home(request):
    return HttpResponse("Hi, It's the creater !")

class CarInfo(APIView):
    model = Car
    def get(self, request):
        products = self.model.objects.all()
        # serializer = create_serializer_class(products, many=True)

        serializer = ModelSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # serializer = create_serializer_class(self.model).serializer_class(data=request.data)
        serializer = ModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_products(request):
    products = Car.objects.all()
    serializer = ModelSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# class ProductDetailAPIView(APIView):
#     def get(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response(status=204)
def add_user():
    return None

def get_user():
    return None