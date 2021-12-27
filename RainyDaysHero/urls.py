from django.urls import path

#home page and utils
from .app_views.index import index

#raininsurance views
from .app_views.raininsurance.quotation import quotation
from .app_views.raininsurance.retrospective import retrospective


app_name = 'rdh'
urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    path('quotation/', quotation, name='quotation'),
    path('retrospective/', retrospective, name='retrospective'),
]