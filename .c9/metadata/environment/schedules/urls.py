{"filter":false,"title":"urls.py","tooltip":"/schedules/urls.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["from django.conf.urls import url","from django.urls import path","from . import views","","from locations.views import *","","from django.conf.urls import url","from django.urls import path","from . import views","","urlpatterns = [","    url(r'^$', views.location_list, name='locations'),","    path('create/', views.location_create, name='location_create'),","    path('<int:pk>/update/', views.location_update, name='location_update'),","    path('<int:pk>/delete/', views.location_delete, name='location_delete'),","    path('export_locations/',views.export_locations, name='export_locations'),","]"],"id":1}],[{"start":{"row":13,"column":3},"end":{"row":15,"column":78},"action":"remove","lines":[" path('<int:pk>/update/', views.location_update, name='location_update'),","    path('<int:pk>/delete/', views.location_delete, name='location_delete'),","    path('export_locations/',views.export_locations, name='export_locations'),"],"id":2},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":[" "],"id":3},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":[" "]},{"start":{"row":12,"column":67},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":6},"action":"insert","lines":["# "],"id":4}],[{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"remove","lines":["n"],"id":5},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"remove","lines":["o"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"remove","lines":["i"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":["t"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"remove","lines":["a"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["c"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["o"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["l"]}],[{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["s"],"id":6},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["c"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["h"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["e"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["d"]},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["u"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["l"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":42},"end":{"row":11,"column":51},"action":"remove","lines":["locations"],"id":7},{"start":{"row":11,"column":42},"end":{"row":11,"column":43},"action":"insert","lines":["s"]},{"start":{"row":11,"column":43},"end":{"row":11,"column":44},"action":"insert","lines":["c"]},{"start":{"row":11,"column":44},"end":{"row":11,"column":45},"action":"insert","lines":["h"]},{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"insert","lines":["e"]},{"start":{"row":11,"column":46},"end":{"row":11,"column":47},"action":"insert","lines":["d"]},{"start":{"row":11,"column":47},"end":{"row":11,"column":48},"action":"insert","lines":["u"]},{"start":{"row":11,"column":48},"end":{"row":11,"column":49},"action":"insert","lines":["l"]},{"start":{"row":11,"column":49},"end":{"row":11,"column":50},"action":"insert","lines":["e"]},{"start":{"row":11,"column":50},"end":{"row":11,"column":51},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":1},"end":{"row":13,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1533835273790,"hash":"8cced85a05f2a64ab84eafbaa79815acf4009c08"}