from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .forms import *
from .models import *
from events.models import Event
from employees.models import Employee

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# class LocationList(ListView):
#     model = Location

# class PositionCreate(CreateView):
#     model = Location
#     fields = ['code']
#     # success_url = reverse_lazy('profile-list')
    
#     def get_context_data(self, **kwargs):
#         data = super(PositionCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['codes'] = PositionFormSet(self.request.POST)
#         else:
#             data['codes'] = PositionFormSet()
#         return data
    
#     def form_valid(self, form):
#         context = self.get_context_data()
#         codes = context['codes']
#         with transaction.atomic():
#             self.object = form.save()

#             if codes.is_valid():
#                 codes.instance = self.object
#                 codes.save()
#         return super(PositionCreate, self).form_valid(form)

    
    


def location_list_view(request):
    if request.method == "POST":
        location_form = LocationForm(request.POST)
        # PositionFormSet = inlineformset_factory(Location, Position, fields=('code',))
        if location_form.is_valid():
            created_location = location_form.save(commit=False)
            formset = PositionFormSet(request.POST, instance=created_location)
            if formset.is_valid():
                formset.save()
                created_location.save()
        
    form = LocationForm()
    context = {
        'employees':Employee.objects.all(),
        'events':Event.objects.all(),
        'locations':Location.objects.all().order_by('location_id'),
        'form':form,
    }
    return render(request, './locations/location_list.html', context)


# def location_list_view(request)
#     model = Profile
#     fields = ['first_name', 'last_name']
#     success_url = reverse_lazy('profile-list')

#     def get_context_data(self, **kwargs):
#         data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['familymembers'] = FamilyMemberFormSet(self.request.POST)
#         else:
#             data['familymembers'] = FamilyMemberFormSet()
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         familymembers = context['familymembers']
#         with transaction.atomic():
#             self.object = form.save()

#             if familymembers.is_valid():
#                 familymembers.instance = self.object
#                 familymembers.save()
#         return super(ProfileFamilyMemberCreate, self).form_valid(form)