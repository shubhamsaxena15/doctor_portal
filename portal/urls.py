from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings  

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('signup',views.signup,name='signup'),
    
    
    
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
