
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views
from tracker_app.views import*


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('user/', UserAPIView.as_view(), name='user'),
     # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),

    # Device URLs
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('devices/<int:pk>/assign/', DeviceAssignView.as_view(), name='device-assign'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('employees/<int:pk>/assignments/', EmployeeAssignmentsListView.as_view(), name='employee-assignments-list'),

    # jwt-authentication
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # for api authentication
    path('api-auth/', include('rest_framework.urls')),
    # for swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Optional :
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    
]
