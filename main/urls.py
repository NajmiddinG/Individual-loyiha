from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from education.views import index, about, contact, course, detail, feature, team, request_to_training, request_to_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('attend/', request_to_training, name='request_to_training'),
    path('new/message/', request_to_message, name='request_to_message'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course/', course, name='course'),
    path('detail/<int:id>/', detail, name='detail'),
    path('feature/', feature, name='feature'),
    path('team/', team, name='team'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
