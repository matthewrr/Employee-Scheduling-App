{"filter":false,"title":"admin.py","tooltip":"/locations/admin.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":3,"column":0},"end":{"row":10,"column":38},"action":"insert","lines":["from django.contrib import admin","from .models import Event","","class EventAdmin(admin.ModelAdmin):","    list_display = ('event_id','title','doors_open')","","# Register your models here.","admin.site.register(Event, EventAdmin)"],"id":2}],[{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":4},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["."]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["m"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["o"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["d"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["l"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":[" "],"id":5},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["i"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["m"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["p"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["o"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["r"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":[" "],"id":6},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["L"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["o"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["c"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["a"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["t"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["i"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["o"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":1},"end":{"row":6,"column":0},"action":"remove","lines":[" Register your models here.","from django.contrib import admin","from .models import Event",""],"id":7},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["#"]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["t"],"id":8},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["n"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["e"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["v"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["L"],"id":9},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["c"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["a"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["t"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["i"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["o"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":25},"action":"remove","lines":["Event"],"id":10},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["L"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["o"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["c"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["a"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["t"]},{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["i"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["o"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["t"],"id":11},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["n"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"remove","lines":["e"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"remove","lines":["v"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"remove","lines":["E"]}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["L"],"id":12},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["o"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["c"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["a"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["t"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["i"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["o"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":51},"action":"remove","lines":["event_id','title','doors_open'"],"id":13},{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":["t"]},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["i"]},{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":["t"]},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["l"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["e"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["'"]}],[{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":[","],"id":14}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":[" "],"id":15},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["l"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["o"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["c"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["a"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["t"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["i"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["o"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"remove","lines":["n"],"id":16},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"remove","lines":["o"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["i"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["t"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["a"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["c"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["o"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"remove","lines":["l"]}],[{"start":{"row":4,"column":29},"end":{"row":4,"column":31},"action":"insert","lines":["''"],"id":17}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["l"],"id":18},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["o"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["c"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["a"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["t"],"id":19}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["t"],"id":20},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["i"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["o"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["n"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["_"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["i"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":41},"end":{"row":4,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1530550553774,"hash":"ec5a58c738419fa304315de6488482aa1fd637d8"}