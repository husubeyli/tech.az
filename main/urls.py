from django.urls import path, include


app_name = 'main'

urlpatterns = [
    path('auth/', include('main.api.urls'))
]