from django.urls import path
from .import views


from django.conf import settings
from django.conf.urls.static import static




urlpatterns =[
    path('form/', views.formpage, name='form'),
    path('', views.homepage,name='home'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('details/<int:pk>', views.details, name='details'),
    path('update/<int:pk>', views.update, name='update'),
   # path('Comment/<int:pk>', views.Comment, name='Comment'),
    path('category', views.category, name='category'),
    path('search',views.search_blog, name='search'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)