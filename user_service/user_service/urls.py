from django.urls import path, include
from oauth2_provider.views import TokenView
from users.views import UserListCreate
from users import views
urlpatterns = [
     path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/', TokenView.as_view(), name='token'),
      path('users/', UserListCreate.as_view(), name='user-list-create'),
      path('', views.home, name='home'),  # Lien vers la vue home
      ]
