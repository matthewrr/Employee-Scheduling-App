{"filter":false,"title":"views.py","tooltip":"/locations/views.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":18,"column":0},"end":{"row":24,"column":8},"action":"remove","lines":["    ","    d = {}","    all_locations = Location.objects.all()","    for location in all_locations:","        positions = list(location.position_set.values_list('position'))","        d[location] = positions","        "],"id":384}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["        'myd':d",""],"id":385}],[{"start":{"row":0,"column":0},"end":{"row":27,"column":65},"action":"remove","lines":["from django.shortcuts import render","from django.http import HttpResponse","from django.forms import inlineformset_factory","","from .forms import *","from .models import *","from events.models import Event","from employees.models import Employee","","def location_list_view(request):","    if request.method == \"POST\":","        location_form = LocationForm(request.POST)","        if location_form.is_valid():","            created_location = location_form.save(commit=False)","            formset = PositionFormSet(request.POST, instance=created_location)","            if formset.is_valid():","                formset.save()","                created_location.save()","","    form = LocationForm()","    context = {","        'employees':Employee.objects.all(),","        'events':Event.objects.all(),","        'locations':Location.objects.all().order_by('location_id'),","        'form':form,","        'obj':'location',","    }","    return render(request, './objects/object_list.html', context)"],"id":387},{"start":{"row":0,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["from django.shortcuts import render","from django.http import HttpResponse","","from .forms import EmployeeForm","from .models import *","from events.models import Event","from locations.models import Location","","from django.contrib import messages","from django.http import JsonResponse","from django.shortcuts import render, get_object_or_404","from django.template.loader import render_to_string","","def employee_list(request):","    employees = Employee.objects.all().order_by('first_name')","    return render(request, 'objects/list.html', {'employees': employees, 'obj':'employee', 'objs':'employees'})","","def employee_create(request):","    if request.method == 'POST':","        form = EmployeeForm(request.POST)","    else:","        form = EmployeeForm()","    return save_employee_form(request, form, 'objects/create.html')","","def save_employee_form(request, form, template_name):","    data = dict()","    ","    if request.method == 'POST':","        if form.is_valid():","            form.save()","            data['form_is_valid'] = True","            employees = Employee.objects.all().order_by('first_name')","            data['html_object_list'] = render_to_string('employees/employee_list_ajax.html', {","                'employees': employees,","            })","        else:","            data['form_is_valid'] = False","    context = {'form': form, 'obj':'employee'}","    data['html_form'] = render_to_string(template_name, context, request=request)","    return JsonResponse(data)","","def employee_update(request, pk):","    employee = get_object_or_404(Employee, pk=pk)","    if request.method == 'POST':","        form = EmployeeForm(request.POST, instance=employee)","    else:","        form = EmployeeForm(instance=employee)","    return save_employee_form(request, form, 'objects/update.html')","","def employee_delete(request, pk):","    employee = get_object_or_404(Employee, pk=pk)","    data = dict()","    if request.method == 'POST':","        employee.delete()","        data['form_is_valid'] = True","        employees = Employee.objects.all().order_by('first_name')","        data['html_object_list'] = render_to_string('employees/employee_list_ajax.html', {","            'employees': employees,","        })","    else:","        context = {'object': employee, 'obj': 'employee',}","        data['html_form'] = render_to_string('objects/delete.html',","            context,","            request=request,","        )","    return JsonResponse(data)",""]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":27},"action":"remove","lines":["Employee"],"id":393},{"start":{"row":3,"column":19},"end":{"row":3,"column":27},"action":"insert","lines":["Location"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":12},"action":"insert","lines":["location"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":12},"action":"insert","lines":["location"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":24},"action":"remove","lines":["Employee"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":24},"action":"insert","lines":["Location"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":58},"action":"remove","lines":["employee"]},{"start":{"row":15,"column":50},"end":{"row":15,"column":58},"action":"insert","lines":["location"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":70},"action":"remove","lines":["employee"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":70},"action":"insert","lines":["location"]},{"start":{"row":15,"column":80},"end":{"row":15,"column":88},"action":"remove","lines":["employee"]},{"start":{"row":15,"column":80},"end":{"row":15,"column":88},"action":"insert","lines":["location"]},{"start":{"row":15,"column":99},"end":{"row":15,"column":107},"action":"remove","lines":["employee"]},{"start":{"row":15,"column":99},"end":{"row":15,"column":107},"action":"insert","lines":["location"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":12},"action":"insert","lines":["location"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":23},"action":"remove","lines":["Employee"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":23},"action":"insert","lines":["Location"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":23},"action":"remove","lines":["Employee"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":23},"action":"insert","lines":["Location"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":24},"action":"remove","lines":["employee"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":24},"action":"insert","lines":["location"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":17},"action":"remove","lines":["employee"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":17},"action":"insert","lines":["location"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":20},"action":"remove","lines":["employee"]},{"start":{"row":31,"column":12},"end":{"row":31,"column":20},"action":"insert","lines":["location"]},{"start":{"row":31,"column":24},"end":{"row":31,"column":32},"action":"remove","lines":["Employee"]},{"start":{"row":31,"column":24},"end":{"row":31,"column":32},"action":"insert","lines":["Location"]},{"start":{"row":32,"column":57},"end":{"row":32,"column":65},"action":"remove","lines":["employee"]},{"start":{"row":32,"column":57},"end":{"row":32,"column":65},"action":"insert","lines":["location"]},{"start":{"row":32,"column":67},"end":{"row":32,"column":75},"action":"remove","lines":["employee"]},{"start":{"row":32,"column":67},"end":{"row":32,"column":75},"action":"insert","lines":["location"]},{"start":{"row":33,"column":17},"end":{"row":33,"column":25},"action":"remove","lines":["employee"]},{"start":{"row":33,"column":17},"end":{"row":33,"column":25},"action":"insert","lines":["location"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":37},"action":"remove","lines":["employee"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":37},"action":"insert","lines":["location"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":44},"action":"remove","lines":["employee"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":44},"action":"insert","lines":["location"]},{"start":{"row":41,"column":4},"end":{"row":41,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":41,"column":4},"end":{"row":41,"column":12},"action":"insert","lines":["location"]},{"start":{"row":42,"column":4},"end":{"row":42,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":42,"column":4},"end":{"row":42,"column":12},"action":"insert","lines":["location"]},{"start":{"row":42,"column":33},"end":{"row":42,"column":41},"action":"remove","lines":["Employee"]},{"start":{"row":42,"column":33},"end":{"row":42,"column":41},"action":"insert","lines":["Location"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":23},"action":"remove","lines":["Employee"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":23},"action":"insert","lines":["Location"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":59},"action":"remove","lines":["employee"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":59},"action":"insert","lines":["location"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":23},"action":"remove","lines":["Employee"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":23},"action":"insert","lines":["Location"]},{"start":{"row":46,"column":37},"end":{"row":46,"column":45},"action":"remove","lines":["employee"]},{"start":{"row":46,"column":37},"end":{"row":46,"column":45},"action":"insert","lines":["location"]},{"start":{"row":47,"column":16},"end":{"row":47,"column":24},"action":"remove","lines":["employee"]},{"start":{"row":47,"column":16},"end":{"row":47,"column":24},"action":"insert","lines":["location"]},{"start":{"row":49,"column":4},"end":{"row":49,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":49,"column":4},"end":{"row":49,"column":12},"action":"insert","lines":["location"]},{"start":{"row":50,"column":4},"end":{"row":50,"column":12},"action":"remove","lines":["employee"]},{"start":{"row":50,"column":4},"end":{"row":50,"column":12},"action":"insert","lines":["location"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":41},"action":"remove","lines":["Employee"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":41},"action":"insert","lines":["Location"]},{"start":{"row":53,"column":8},"end":{"row":53,"column":16},"action":"remove","lines":["employee"]},{"start":{"row":53,"column":8},"end":{"row":53,"column":16},"action":"insert","lines":["location"]},{"start":{"row":55,"column":8},"end":{"row":55,"column":16},"action":"remove","lines":["employee"]},{"start":{"row":55,"column":8},"end":{"row":55,"column":16},"action":"insert","lines":["location"]},{"start":{"row":55,"column":20},"end":{"row":55,"column":28},"action":"remove","lines":["Employee"]},{"start":{"row":55,"column":20},"end":{"row":55,"column":28},"action":"insert","lines":["Location"]},{"start":{"row":56,"column":53},"end":{"row":56,"column":61},"action":"remove","lines":["employee"]},{"start":{"row":56,"column":53},"end":{"row":56,"column":61},"action":"insert","lines":["location"]},{"start":{"row":56,"column":63},"end":{"row":56,"column":71},"action":"remove","lines":["employee"]},{"start":{"row":56,"column":63},"end":{"row":56,"column":71},"action":"insert","lines":["location"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":21},"action":"remove","lines":["employee"]},{"start":{"row":57,"column":13},"end":{"row":57,"column":21},"action":"insert","lines":["location"]},{"start":{"row":57,"column":25},"end":{"row":57,"column":33},"action":"remove","lines":["employee"]},{"start":{"row":57,"column":25},"end":{"row":57,"column":33},"action":"insert","lines":["location"]},{"start":{"row":60,"column":29},"end":{"row":60,"column":37},"action":"remove","lines":["employee"]},{"start":{"row":60,"column":29},"end":{"row":60,"column":37},"action":"insert","lines":["location"]},{"start":{"row":60,"column":47},"end":{"row":60,"column":55},"action":"remove","lines":["employee"]},{"start":{"row":60,"column":47},"end":{"row":60,"column":55},"action":"insert","lines":["location"]}],[{"start":{"row":55,"column":62},"end":{"row":55,"column":63},"action":"remove","lines":["e"],"id":394},{"start":{"row":55,"column":61},"end":{"row":55,"column":62},"action":"remove","lines":["m"]},{"start":{"row":55,"column":60},"end":{"row":55,"column":61},"action":"remove","lines":["a"]},{"start":{"row":55,"column":59},"end":{"row":55,"column":60},"action":"remove","lines":["n"]},{"start":{"row":55,"column":58},"end":{"row":55,"column":59},"action":"remove","lines":["_"]},{"start":{"row":55,"column":57},"end":{"row":55,"column":58},"action":"remove","lines":["t"]},{"start":{"row":55,"column":56},"end":{"row":55,"column":57},"action":"remove","lines":["s"]},{"start":{"row":55,"column":55},"end":{"row":55,"column":56},"action":"remove","lines":["r"]},{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"remove","lines":["i"]},{"start":{"row":55,"column":53},"end":{"row":55,"column":54},"action":"remove","lines":["f"]}],[{"start":{"row":55,"column":53},"end":{"row":55,"column":54},"action":"insert","lines":["l"],"id":395},{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"insert","lines":["o"]},{"start":{"row":55,"column":55},"end":{"row":55,"column":56},"action":"insert","lines":["c"]},{"start":{"row":55,"column":56},"end":{"row":55,"column":57},"action":"insert","lines":["a"]},{"start":{"row":55,"column":57},"end":{"row":55,"column":58},"action":"insert","lines":["t"]},{"start":{"row":55,"column":58},"end":{"row":55,"column":59},"action":"insert","lines":["i"]},{"start":{"row":55,"column":59},"end":{"row":55,"column":60},"action":"insert","lines":["o"]},{"start":{"row":55,"column":60},"end":{"row":55,"column":61},"action":"insert","lines":["n"]},{"start":{"row":55,"column":61},"end":{"row":55,"column":62},"action":"insert","lines":["_"]},{"start":{"row":55,"column":62},"end":{"row":55,"column":63},"action":"insert","lines":["i"]},{"start":{"row":55,"column":63},"end":{"row":55,"column":64},"action":"insert","lines":["d"]}],[{"start":{"row":31,"column":57},"end":{"row":31,"column":67},"action":"remove","lines":["first_name"],"id":396},{"start":{"row":31,"column":57},"end":{"row":31,"column":58},"action":"insert","lines":["l"]},{"start":{"row":31,"column":58},"end":{"row":31,"column":59},"action":"insert","lines":["o"]},{"start":{"row":31,"column":59},"end":{"row":31,"column":60},"action":"insert","lines":["c"]},{"start":{"row":31,"column":60},"end":{"row":31,"column":61},"action":"insert","lines":["a"]},{"start":{"row":31,"column":61},"end":{"row":31,"column":62},"action":"insert","lines":["t"]},{"start":{"row":31,"column":62},"end":{"row":31,"column":63},"action":"insert","lines":["i"]},{"start":{"row":31,"column":63},"end":{"row":31,"column":64},"action":"insert","lines":["o"]},{"start":{"row":31,"column":64},"end":{"row":31,"column":65},"action":"insert","lines":["n"]},{"start":{"row":31,"column":65},"end":{"row":31,"column":66},"action":"insert","lines":["_"]},{"start":{"row":31,"column":66},"end":{"row":31,"column":67},"action":"insert","lines":["i"]},{"start":{"row":31,"column":67},"end":{"row":31,"column":68},"action":"insert","lines":["d"]}],[{"start":{"row":14,"column":55},"end":{"row":14,"column":59},"action":"remove","lines":["name"],"id":397},{"start":{"row":14,"column":49},"end":{"row":14,"column":53},"action":"insert","lines":["name"]}],[{"start":{"row":14,"column":49},"end":{"row":14,"column":53},"action":"remove","lines":["name"],"id":398}],[{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"remove","lines":["_"],"id":399},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"remove","lines":["t"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"remove","lines":["s"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["r"]},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"remove","lines":["i"]},{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"remove","lines":["f"]}],[{"start":{"row":14,"column":49},"end":{"row":14,"column":50},"action":"insert","lines":["l"],"id":400},{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":["o"]},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["c"]},{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":["a"]},{"start":{"row":14,"column":53},"end":{"row":14,"column":54},"action":"insert","lines":["t"]},{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"insert","lines":["i"]},{"start":{"row":14,"column":55},"end":{"row":14,"column":56},"action":"insert","lines":["o"]},{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"insert","lines":["n"]},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":["_"]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["i"]},{"start":{"row":14,"column":59},"end":{"row":14,"column":60},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":[","],"id":401}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":[" "],"id":402}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":50},"action":"insert","lines":["JsonResponse"],"id":403}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":36},"action":"remove","lines":["from django.http import JsonResponse"],"id":404},{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":[","],"id":405}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":53},"action":"insert","lines":["get_object_or_404"],"id":406}],[{"start":{"row":0,"column":36},"end":{"row":0,"column":37},"action":"insert","lines":[" "],"id":407}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":54},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404"],"id":408},{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":35},"action":"remove","lines":["from django.contrib import messages"],"id":410},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":31},"action":"remove","lines":["from events.models import Event"],"id":411},{"start":{"row":4,"column":21},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":37},"action":"remove","lines":["from locations.models import Location"],"id":412},{"start":{"row":4,"column":21},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":51},"action":"remove","lines":["from django.template.loader import render_to_string"],"id":413}],[{"start":{"row":1,"column":50},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":414}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":51},"action":"insert","lines":["from django.template.loader import render_to_string"],"id":415}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":54},"action":"remove","lines":["from django.shortcuts import render, get_object_or_404"],"id":416}],[{"start":{"row":1,"column":50},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":417}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":54},"action":"insert","lines":["from django.shortcuts import render, get_object_or_404"],"id":418}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":419}],[{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":420},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":24},"end":{"row":0,"column":38},"action":"remove","lines":["HttpResponse, "],"id":421}],[{"start":{"row":1,"column":37},"end":{"row":1,"column":54},"action":"remove","lines":["get_object_or_404"],"id":422}],[{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":[" "],"id":423},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":[","]}],[{"start":{"row":1,"column":29},"end":{"row":1,"column":46},"action":"insert","lines":["get_object_or_404"],"id":424}],[{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":[","],"id":425}],[{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":[" "],"id":426}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":48},"end":{"row":1,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1531624634799,"hash":"e2ead1d1b55e4dd383b2636c6e3e4b4d60d5fae7"}