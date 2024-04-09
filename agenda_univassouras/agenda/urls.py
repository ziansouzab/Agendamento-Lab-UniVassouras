from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = {
    path(r'^$', CreateView.as_view(), name="agenda"),    
    path(r'^(?P<pk>[0-9]+)$',
        DetailsView.as_view(), name="details_genda"),      
}

urlpatterns = format_suffix_patterns(urlpatterns)