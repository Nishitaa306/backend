from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

# Define a redirect view for the home page
def home(request):
    # Redirect to the desired URL
    return HttpResponseRedirect("http://localhost:5173/")

urlpatterns = [
    path('', home, name='home'),  # Root URL redirects to the frontend
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),
]