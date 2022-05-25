from django.contrib import admin
from django.urls import path
from main.views import register_client, detail_client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_client, name='register'),
    path('<int:id>/', detail_client, name="client")

]
