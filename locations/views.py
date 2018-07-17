import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import LocationForm
from .models import *

from . import views
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from scheduling_app.views import ObjectSave

from scheduling_app.views import *

from django.http import JsonResponse



class AjaxTemplateMixin(object):
 
    def dispatch(self, request, *args, **kwargs):
        # if not hasattr(self, 'ajax_template_name'):
        #     split = self.template_name.split('.html')
        #     split[-1] = '_inner'
        #     split.append('.html')
        #     self.ajax_template_name = ''.join(split)
        # if request.is_ajax():
        self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class LocationList(ObjectList, ListView):
    model = Location
    context_object_name = 'locations'
    extra_context = {'obj':'location','objs':'locations'}

class LocationCreate(CreateView):
    model = Location
    template_name = 'objects/create.html'
    extra_contest = {'obj':'location','objs':'locations'}
    fields = ['location_id', 'title', 'bar',]
    success_url = reverse_lazy('locations:location_list')
  
class LocationUpdate(UpdateView):
    model = Location
    fields = ['location_id', 'title', 'bar',]
    success_url = reverse_lazy('locations:location_list')

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations:location_list')






## 1. ListView
## 2. CreateView
# 3. DeleteView
# 4. UpdateView
# 5. FormView
# 6. SaveView





# class AjaxableResponseMixin:
#     """
#     Mixin to add AJAX support to a form.
#     Must be used with an object-based FormView (e.g. CreateView)
#     """
#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         # We make sure to call the parent's form_valid() method because
#         # it might do some processing (in the case of CreateView, it will
#         # call form.save() for example).
#         response = super().form_valid(form)
#         if self.request.is_ajax():
#             data = {
#                 'pk': self.object.pk,
#             }
#             return JsonResponse(data)
#         else:
#             return response







# def save_location_form(request, form, template_name):
#     data = dict()
    
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             locations = Location.objects.all().order_by('location_id')
#             data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
#                 'locations': locations,
#             })
#         else:
#             data['form_is_valid'] = False
#     context = {'form': form, 'obj':'location'}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)

# def location_update(request, pk):
#     location = get_object_or_404(Location, pk=pk)
#     if request.method == 'POST':
#         form = LocationForm(request.POST, instance=location)
#     else:
#         form = LocationForm(instance=location)
#     return save_location_form(request, form, 'objects/update.html')

# def location_delete(request, pk):
#     location = get_object_or_404(Location, pk=pk)
#     data = dict()
#     if request.method == 'POST':
#         location.delete()
#         data['form_is_valid'] = True
#         locations = Location.objects.all().order_by('location_id')
#         data['html_object_list'] = render_to_string('locations/location_list_ajax.html', {
#             'locations': locations,
#         })
#     else:
#         context = {'object': location, 'obj': 'location',}
#         data['html_form'] = render_to_string('objects/delete.html',
#             context,
#             request=request,
#         )
#     return JsonResponse(data)

# def export_locations(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="all_locations.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['location_id','title','bar'])

#     locations = Location.objects.all().values_list('location_id', 'title', 'bar')
#     for location in locations:
#         writer.writerow(location)

#     return response



# class LocationSave(ObjectSave, TemplateView):
#     obj = 'location'
#     objs = 'locations'
#     all_objs = Location.objects.all().order_by('location_id')
#     template_name = 'locations/location_list_ajax.html'
#     # pass
    
    # def get_context_data(self, **kwargs):
    #     context = super(SaveLocation, self).get_context_data(**kwargs)
    #     context.update({
    #         'foodata': 'bardata',
    #     })
    #     return context

# class MyFormView(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')

#         return render(request, self.template_name, {'form': form})

# def location_list(request):
#     locations = Location.objects.all().order_by('location_id')
#     return render(request, 'objects/list.html', {'locations': locations, 'obj':'location', 'objs':'locations'})