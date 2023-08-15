from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly, IsAdminUser])
def producthomepage(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            message = {"Success": "Product has been created successful"}
            message.update(new_product.data)
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(new_product.errors, status=status.HTTP_400_BAD_REQUEST)
    


# # @api_view(["GET", "PUT", "DELETE"])
# # def productdetailpage(request, slug):
# #     if request.method == "GET":
# #         product = Product.objects.get(slug=slug)
# #         serialized_product = ProductSerializer(product)
# #         return Response(serialized_product.data, status=status.HTTP_200_OK)
    
# #     elif request.method == "PUT":
# #         product = Product.objects.get(slug=slug)
# #         serialized_product = ProductSerializer(product, data=request.data, partial=True)
# #         return Response(serialized_product.data, status=status.HTTP_202_ACCEPTED)
    
# #     elif request.method == "DELETE":
# #         product = Product.objects.get(slug=slug)
# #         product.delete()
# #         return Response("post deletion successful", status=status.HTTP_204_NO_CONTENT)
    


# class productdetailpage(APIView):
#     def get(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         serialized_product = ProductSerializer(product)
#         return Response(serialized_product.data, status=status.HTTP_200_OK)
    
#     def put(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         serialized_product = ProductSerializer(product, data=request.data, partial=True)
#         return Response(serialized_product.data, status=status.HTTP_202_ACCEPTED)
    
#     def delete(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         product.delete()
#         return Response("post deletion successful", status=status.HTTP_204_NO_CONTENT)

class producthomepage(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    
    def get(self,request):
        all_products = Product.objects.all()
        serialized_products = ProductSerializer(all_products, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        new_product = ProductSerializer(data=request.data)
        if new_product.is_valid():
            new_product.save()
            message = {"Success": "Product has been created successful"}
            message.update(new_product.data)
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(new_product.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        new_product = ProductSerializer(data=request.data)
        new_product.is_valid(raise_exception=True)
        new_product.save()
        message = {"Success": "Product has been created successful"}
        message.update(new_product.data)
        return Response(message, status=status.HTTP_201_CREATED)


    

class ProductHomePage(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    

# # class ProductDetailPage(RetrieveUpdateDestroyAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer

    
