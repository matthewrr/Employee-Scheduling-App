{"filter":false,"title":"views.py","tooltip":"/sms/views.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":31},"end":{"row":17,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"ee1bfd2e564261a01bfb27ea50e42cd29329a53f","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":4,"column":33},"action":"insert","lines":["from django.shortcuts import render","from django.http import HttpResponse","","def company_profile(request):","    return HttpResponse('Hello!')"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":19},"action":"remove","lines":["company_profile"],"id":3},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["t"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["e"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"remove","lines":["t"],"id":4}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["x"],"id":5},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["t"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["_"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["f"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["a"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["t"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["u"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["r"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":33},"action":"remove","lines":["from django.shortcuts import render","from django.http import HttpResponse","","def text_feature(request):","    return HttpResponse('Hello!')"],"id":6},{"start":{"row":0,"column":0},"end":{"row":17,"column":61},"action":"insert","lines":["from django.shortcuts import render","from django.http import HttpResponse","","from django.shortcuts import render","from django.http import HttpResponse","from django.forms import inlineformset_factory","","# from .forms import *","from .models import *","from events.models import Event","from employees.models import Employee","","def company_profile(request):","","    context = {","        'obj':'Profile',","    }","    return render(request, './company_profile.html', context)"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":19},"action":"remove","lines":["company_profile"],"id":7},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["s"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["m"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["s"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["-"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["t"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"remove","lines":["e"],"id":8},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"remove","lines":["t"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"remove","lines":["-"]}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["_"],"id":9},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["t"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["x"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["e"],"id":10},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["l"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["i"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["f"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["o"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["r"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["P"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["S"],"id":11},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["M"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["S"]}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":[" "],"id":12},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["T"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["e"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["x"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":45},"action":"remove","lines":["company_profile"],"id":13},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["s"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["m"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["s"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["_"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["t"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["e"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["x"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["."],"id":14}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["s"],"id":15},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["m"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["s"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["_"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"insert","lines":["t"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"insert","lines":["e"]},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":["x"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"remove","lines":["t"],"id":16},{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":["x"]},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":["e"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"remove","lines":["t"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"remove","lines":["_"]}]]},"timestamp":1531338251472}