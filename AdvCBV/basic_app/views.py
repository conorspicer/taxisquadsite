from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView,DeleteView,UpdateView)
import datetime

# Remeber this TemplateView is what our class will inherit from, not a parameter of a function
# If we use app subfolders in the template dir we would need to include that in the path here

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # will generate "modelname_list" itself (all in lower case ).
    #  To avoid confusion later on we can define this ourselves

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('team', 'player', 'added_time', 'roster', 'change')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('team', 'player', 'added_time', 'roster', 'change')
    model = models.School
    success_url = reverse_lazy("basic_app:list")
    
    def get_initial(self):
        return { 'added_time': datetime.datetime.now}

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class RosterListView(ListView):
    context_object_name = 'rosters'
    model = models.School
    template_name = 'basic_app/roster_list.html'

    # def filter_user(self, team):
    #     return super(RosterListView, self).get_query_set().filter(team=team)

    # def get_queryset(self):
        # return School.object.order_by('-pub_date')[:5]
