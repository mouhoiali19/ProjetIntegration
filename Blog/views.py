from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Blog.models import Blog , Categories , Blogs_Categories
from .serializers import BlogSerializer , CategorySerializer
from rest_framework import status

class BlogCreateView(APIView):
  def post(self , request):
    serializer  = BlogSerializer(data= request.data)
    if serializer.is_valid():
      blog = serializer.save()
      crypto_categories = Categories.objects.filter(name="crypto")

      for category in crypto_categories:
        Blogs_Categories.objects.create(category_id=category, blog_id=blog)
      return Response({
          "message": "Blog created successfully.",
          "data": serializer.data
      }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogList(APIView):
  def get(self , request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

class CryptoBlog(APIView):
  def get(self , request):
    blogs =[]
    blogs_cate = Blogs_Categories.objects.all()
    for blog_cate in blogs_cate:
      blog = blog_cate.blog_id 
      blogs.append(blog)
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)



class CategoryCreateView(APIView):
  def post(self , request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
          category = serializer.save()
          return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class CategoryListView(APIView):
  def get(self , request):
    categories = Categories.objects.all()
    serializer = CategorySerializer(categories , many=True)
    return Response(serializer.data)


class GetCategoryByID(APIView):
  def get(self , request , pk):
    category = Categories.objects.get(id=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


class DeleteCategory(APIView):
    def delete_category(request , pk):
      category = get_object_or_404(Categories,id=pk)
      if category:
        category.delete()
        return Response(status=204)
      return Response({"error": "ID is required to delete a category"}, status=400)


class DeleteBlog(APIView):
    def delete_category(request , pk):
      blog = get_object_or_404(Blog,id=pk)
      if blog:
        blog.delete()
        return Response(status=204)
      return Response({"error": "ID is required to delete a category"}, status=400)