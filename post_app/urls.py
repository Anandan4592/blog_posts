from django.urls import path
from .views import Bloglist, Addblog, Updateblog

urlpatterns = [
    path('', Bloglist.as_view(), name='bloglist'),  # Main blog list view
    path('addblog', Addblog.as_view(), name='addblog'),  # View to add a new blog post
    path('update/<int:id>/', Updateblog.as_view(), name='updateblog'),  # View to update an existing blog post
]
