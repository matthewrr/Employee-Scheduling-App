import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import LocationForm
from .models import *

from . import views
from django.views.generic import TemplateView, ListView, CreateView
from scheduling_app.views import ObjectSave, AjaxableResponseMixin

from scheduling_app.views import *

class LocationList(ObjectList, ListView):
    print('list')
    model = Location
    context_object_name = 'locations'
    extra_context = {'obj':'location','objs':'locations'}

class LocationCreate(AjaxableResponseMixin, CreateView):
    print('create')
    model = Location
    template_name = 'objects/create.html'
    extra_contest = {'obj':'location','objs':'locations'}
    fields = ['location_id', 'title', 'bar',]


# def location_create(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#     else:
#         form = LocationForm()
#     return save_location_form(request, form, 'objects/create.html')

def save_location_form(request, form, template_name):
    data = dict()
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locations = Location.objects.all().order_by('location_id')
            data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
                'locations': locations,
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'obj':'location'}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
    else:
        form = LocationForm(instance=location)
    return save_location_form(request, form, 'objects/update.html')

def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    data = dict()
    if request.method == 'POST':
        location.delete()
        data['form_is_valid'] = True
        locations = Location.objects.all().order_by('location_id')
        data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
            'locations': locations,
        })
    else:
        context = {'object': location, 'obj': 'location',}
        data['html_form'] = render_to_string('objects/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def export_locations(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_locations.csv"'

    writer = csv.writer(response)
    writer.writerow(['location_id','title','bar'])

    locations = Location.objects.all().values_list('location_id', 'title', 'bar')
    for location in locations:
        writer.writerow(location)

    return response



class SaveLocation(ObjectSave, TemplateView):
    obj = 'location'
    objs = 'locations'
    all_objs = Location.objects.all().order_by('location_id')
    template_name = 'locations/location_list_ajax.html'
    pass
    
    def get_context_data(self, **kwargs):
        context = super(SaveLocation, self).get_context_data(**kwargs)
        context.update({
            'foodata': 'bardata',
        })
        return context

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})




# def location_list(request):
#     locations = Location.objects.all().order_by('location_id')
#     return render(request, 'objects/list.html', {'locations': locations, 'obj':'location', 'objs':'locations'})

