"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

def homepage(request):
    art = r"""
   ░██    ░██                      ░██████████                                                                                                               ░███    ░█████████  ░██████
   ░██    ░██                      ░██                                                                                                                      ░██░██   ░██     ░██   ░██  
░████████ ░████████   ░███████     ░██                  ░███████   ░███████  ░█████████████  ░█████████████   ░███████  ░██░████  ░███████   ░███████      ░██  ░██  ░██     ░██   ░██  
   ░██    ░██    ░██ ░██    ░██    ░█████████  ░██████ ░██    ░██ ░██    ░██ ░██   ░██   ░██ ░██   ░██   ░██ ░██    ░██ ░███     ░██    ░██ ░██    ░██    ░█████████ ░█████████    ░██  
   ░██    ░██    ░██ ░█████████    ░██                 ░██        ░██    ░██ ░██   ░██   ░██ ░██   ░██   ░██ ░█████████ ░██      ░██        ░█████████    ░██    ░██ ░██           ░██  
   ░██    ░██    ░██ ░██           ░██                 ░██    ░██ ░██    ░██ ░██   ░██   ░██ ░██   ░██   ░██ ░██        ░██      ░██    ░██ ░██           ░██    ░██ ░██           ░██  
    ░████ ░██    ░██  ░███████     ░██████████          ░███████   ░███████  ░██   ░██   ░██ ░██   ░██   ░██  ░███████  ░██       ░███████   ░███████     ░██    ░██ ░██         ░██████
                                                                                                                                                                                         
                                                                                                                                                                                         
                                                                                                                                                                                         
    """

    message = """
    <div style="color:#0f0; font-size:16px; margin-top:10px;">
        🚀 <b>E-commerce API deployed successfully on Render!</b><br>
        Access endpoints at <code style="color:#39ff14;">/api/products/</code> and others.
        <b>Built by Zachary K. Mohamed XO</b><br>
    </div>
    """

    html = f"""
    <div style="background:#0a0a0a; color:#0f0; min-height:100vh; display:flex; align-items:center; justify-content:center;">
        <div style="
            border:2px solid #0f0;
            border-radius:10px;
            padding:30px;
            max-width:90%;
            overflow-x:auto;
            text-align:center;
            font-family: monospace;
            background:#000;
            box-shadow: 0 0 20px #0f0a;
        ">
            <pre style="white-space: pre; font-size:11px; line-height:1.1;">{art}</pre>
            {message}
        </div>
    </div>
    """

    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', homepage, name='homepage'),
]
