from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import(home, services, store, about,
                    contact, details)

app_name = 'myapp'

urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('store/', store, name='store'),
    path('contact', contact, name='contact'),
    path('details<str:pk>/', details, name = 'details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
