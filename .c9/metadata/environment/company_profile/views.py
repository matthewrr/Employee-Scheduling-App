{"filter":false,"title":"views.py","tooltip":"/company_profile/views.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":43},"end":{"row":17,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"7e6f7110a1c634d74adacf8eb3defbf01508513d","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":4,"column":33},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]},{"start":{"row":5,"column":4},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":40,"column":65},"action":"insert","lines":["from django.shortcuts import render","from django.http import HttpResponse","from django.forms import inlineformset_factory","","from .forms import *","from .models import *","from events.models import Event","from employees.models import Employee","","def location_list_view(request):","    if request.method == \"POST\":","        location_form = LocationForm(request.POST)","        if location_form.is_valid():","            created_location = location_form.save(commit=False)","            formset = PositionFormSet(request.POST, instance=created_location)","            if formset.is_valid():","                formset.save()","                created_location.save()","    ","    d = {}","    all_locations = Location.objects.all()","    for location in all_locations:","        positions = list(location.position_set.values_list('position'))","        d[location] = positions","        ","    form = LocationForm()","    context = {","        'employees':Employee.objects.all(),","        'events':Event.objects.all(),","        'locations':Location.objects.all().order_by('location_id'),","        'form':form,","        'obj':'location',","        'myd':d","    }","    return render(request, './objects/object_list.html', context)"],"id":15}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":22},"action":"remove","lines":["location_list_view"],"id":16},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["c"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["o"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["m"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["p"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["a"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["n"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["y"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["_"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["p"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["r"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["o"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["f"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["i"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["l"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":4},"end":{"row":29,"column":31},"action":"remove","lines":["if request.method == \"POST\":","        location_form = LocationForm(request.POST)","        if location_form.is_valid():","            created_location = location_form.save(commit=False)","            formset = PositionFormSet(request.POST, instance=created_location)","            if formset.is_valid():","                formset.save()","                created_location.save()","    ","    d = {}","    all_locations = Location.objects.all()","    for location in all_locations:","        positions = list(location.position_set.values_list('position'))","        d[location] = positions"],"id":17}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":25},"action":"remove","lines":["        ","    form = LocationForm()"],"id":18},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"remove","lines":["",""]},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["        'employees':Employee.objects.all(),",""],"id":19}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["        'events':Event.objects.all(),",""],"id":20}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["        'locations':Location.objects.all().order_by('location_id'),",""],"id":21}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["        'form':form,",""],"id":22}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["        'myd':d",""],"id":23}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":3,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["def company_profile(request):","    return HttpResponse('Hello!')","    "],"id":25},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "],"id":26}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["n"],"id":27},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["o"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["i"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["t"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["a"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["c"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["o"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["l"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["P"],"id":28},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["o"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["f"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["i"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["l"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":54},"action":"remove","lines":["objects/object_list.html"],"id":29}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["p"],"id":30},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["r"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["o"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["f"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["i"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["l"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["."],"id":31}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["t"],"id":32}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["t"],"id":33}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["/"],"id":34}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["c"],"id":35},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["o"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["m"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["a"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["p"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["n"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["y"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["_"]}],[{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"insert","lines":["."],"id":36},{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"insert","lines":["h"]},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"insert","lines":["t"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"insert","lines":["m"]},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"remove","lines":["p"],"id":37},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"remove","lines":["a"]}],[{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["p"],"id":38},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["a"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["."],"id":39},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["/"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["."],"id":40}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["c"],"id":41},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["o"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["m"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["p"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["a"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["n"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["y"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["_"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["p"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["r"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["o"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["f"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["i"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["l"]},{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"insert","lines":["e"]}]]},"timestamp":1531338261672}