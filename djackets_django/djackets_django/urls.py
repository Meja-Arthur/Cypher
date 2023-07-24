from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),# path to our app urls in django application
    # the authtoken is used for log in purposes in frontend section 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# using the media in the frontend section
# that's how we do this 
