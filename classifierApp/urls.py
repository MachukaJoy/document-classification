from django.urls import path, re_path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from django.views.generic import TemplateView

app_name = 'classifierApp'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('upload/predictImage', views.predictImage, name='predict'),
    path('viewdatabase',  views.viewDB, name='viewdatabase'),
    path('upload/', views.imageupload, name='imageupload'),
    # path('galleryview/', views.gallery, name='gallery'),
    # path('upload/viewDataBase/', views.viewDataBase, name='view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)