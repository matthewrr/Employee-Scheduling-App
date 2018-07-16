from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views.generic import View
from django.views.generic import TemplateView, ListView



def redirect_root(request):
    return HttpResponseRedirect('/events/')

class ObjectList(ListView):
    template_name = 'objects/list.html'


class ObjectCreate(View):
    #pass form
    def post(self, request):
        return save_object_form(request, form, 'objects/create.html')
        

# def save_location_form(request, form, template_name):
class ObjectSave(View):
    # obj = ''
    template_name = ''
    form = ''
    all_objs = ''
    
    def post(self, request):
        data = dict()
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            # locations = Location.objects.all().order_by('location_id')
            data['html_object_list'] = render_to_string(template_name, {
                objs: all_objs,
            })
        else:
            data['form_is_valid'] = False
        context = {'form': form, 'obj':'location'}
        data['html_form'] = render_to_string(template_name, context, request=request)
        return JsonResponse(data)   




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



# def location_create(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#     else:
#         form = LocationForm()
#     return save_location_form(request, form, 'objects/create.html')