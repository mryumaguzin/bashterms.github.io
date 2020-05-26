from django.urls import path

from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('search/', SportResultsView.as_view(), name='sport_results'),
    path('', HomePageView.as_view(), name='home'),
]
