from django.contrib import admin
from django.urls import path, include
from signup.views import signaction
from login.views import loginaction
from bus_res.views import booking
from bus_res.views import ticket_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('bus_res.urls')),  # Include app URLs
    path('signup/',signaction),
    path('login/',loginaction),
     path('', include('bus_res.urls')),
   #path('booking/',booking),
  # path('ticket_view/',ticket_view),

]
