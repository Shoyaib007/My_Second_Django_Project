from django.conf.urls import url
from django.urls import path
from first_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
app_name="first_app"

urlpatterns=[
    path('',views.index.as_view(),name="index"),
    path('addmusician/',views.addmusician.as_view(),name="addmusician"),
    path('addalbum/',views.addalbum.as_view(),name="addalbum"),
    path('Musiciandetails/<pk>/',views.Musiciandetails.as_view(),name="Musiciandetails"),
    path('updatemusician/<pk>/',views.updatemusician.as_view(),name="updatemusician"),
    path('updatealbum/<pk>/',views.updatealbum.as_view(),name="updatealbum"),
    path('musiciandelete/<pk>/',views.musiciandelete.as_view(),name="musiciandelete"),
    # path('albumdelete/<pk>/',views.albumdelete.as_view(),name="albumdelete"),



]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_DIR,document_root=settings.MEDIA_ROOT)
