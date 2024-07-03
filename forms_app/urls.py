from django.urls import path
from .views import contact_us

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('contactUs', contact_us),

]
