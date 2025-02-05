
from django.contrib import admin
from django.urls import path
from authentification.views import UserLoginView, UserRegistrationView
from Blog.views import BlogCreateView , CategoryCreateView , CategoryListView , GetCategoryByID , CryptoBlog , BlogList , DeleteBlog , DeleteCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login'  ,  UserLoginView.as_view() ,  name='user-login'),
    path('auth/register' , UserRegistrationView.as_view() , name='userregistration'),
    path('blog/add' , BlogCreateView.as_view() , name='blogpost'),
    path('category/add' , CategoryCreateView.as_view() , name='addcategory'),
    path('category/get' , CategoryListView.as_view() , name='categorylist'),
    path('category/get/<int:pk>' , GetCategoryByID.as_view() , name='categoryID'),
    path('blog/get/crypto' , CryptoBlog.as_view() , name="get crypto blog "),
    path('category/get/<int:pk>/delete' , DeleteCategory.as_view() , name='categorydelete'),
    path('blog/get' , BlogList.as_view() , name="listblog"),
    path('blog/<int:pk>/delete' , DeleteBlog.as_view() , name="deleteblog"),
]
