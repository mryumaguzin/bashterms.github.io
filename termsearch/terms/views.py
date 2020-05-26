from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Term


class HomePageView(TemplateView):
    template_name = 'index.html'

class SearchResultsView(ListView):
    model = Term
    template_name = 'search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Term.objects.filter(
            Q(name__icontains=query) | Q(bash__icontains=query) |
            Q(mean__icontains=query)
        )
        return object_list

# class SportResultsView(ListView):
#     model = SportTerm
#     template_name = 'sport.html'
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         object_list = SportTerm.objects.filter(
#             Q(name__icontains=query) | Q(bash__icontains=query) |
#             Q(mean__icontains=query)
#         )
#         return object_list
