from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project import settings
from store.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('account/', include("accounts.urls")),
    path('store/', include("store.urls")),
    path('verification/', include('verify_email.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
