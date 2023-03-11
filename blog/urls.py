from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('get-blog/<id>', get_blog, name='get_blog'),
    path('login/', login_attempt, name='login'),
    path('register/', register_attempt, name='register'),
    path('logout/', logout_attempt, name='logout'),
    path('create-blog/', create_blog, name='create_blog'),
    path('update-blog/<id>', update_blog, name='update_blog'),
    path('delete-blog/<id>/', delete_blog, name='delete_blog'),
    path('show-all-blogs/', show_all_blogs, name='show_all_blogs'),
]
