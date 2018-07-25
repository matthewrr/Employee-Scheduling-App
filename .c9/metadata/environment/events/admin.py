{"filter":false,"title":"admin.py","tooltip":"/events/admin.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["l"],"id":402},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["o"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["c"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["a"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["t"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["i"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["o"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"remove","lines":[" "],"id":403},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"remove","lines":["#"]}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["E"],"id":404},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["v"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["e"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["n"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["    inlines = [EventScheduleInline]",""],"id":405}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":6},"action":"insert","lines":["# "],"id":406}],[{"start":{"row":23,"column":0},"end":{"row":26,"column":34},"action":"remove","lines":["class EventLocationInline(admin.StackedInline):","    model = EventLocation","    fields = ('locations',)","    # inlines = [EventShiftInline]"],"id":407}],[{"start":{"row":14,"column":53},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":408},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "],"id":409}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":410}],[{"start":{"row":16,"column":0},"end":{"row":19,"column":34},"action":"insert","lines":["class EventLocationInline(admin.StackedInline):","    model = EventLocation","    fields = ('locations',)","    # inlines = [EventShiftInline]"],"id":411}],[{"start":{"row":23,"column":32},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":412},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":413}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":414}],[{"start":{"row":25,"column":0},"end":{"row":27,"column":32},"action":"insert","lines":["class EventLocationAdmin(admin.ModelAdmin):","    list_display = ('location',)","    inlines = [EventShiftInline]"],"id":415}],[{"start":{"row":25,"column":11},"end":{"row":25,"column":19},"action":"remove","lines":["Location"],"id":416},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["S"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["c"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["h"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["e"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["d"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["u"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["l"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":32},"action":"remove","lines":["    list_display = ('location',)"],"id":417},{"start":{"row":26,"column":0},"end":{"row":26,"column":41},"action":"insert","lines":["fields = ('event','event_schedule_name',)"]}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "],"id":418}],[{"start":{"row":19,"column":34},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":419},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":24,"column":35},"action":"insert","lines":["class EventScheduleInline(admin.StackedInline):","    model = EventSchedule","    fields = ('event','event_schedule_name',)","    inlines = [EventLocationInline]"],"id":420}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":421}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":422}],[{"start":{"row":35,"column":0},"end":{"row":43,"column":35},"action":"remove","lines":["    ","    ","    ","","    ","class EventScheduleInline(admin.StackedInline):","    model = EventSchedule","    fields = ('event','event_schedule_name',)","    inlines = [EventLocationInline]"],"id":423},{"start":{"row":34,"column":4},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "],"id":424},{"start":{"row":33,"column":32},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":32},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":425},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":4},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":426},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":28,"column":0},"end":{"row":30,"column":32},"action":"insert","lines":["class EventLocationAdmin(admin.ModelAdmin):","    list_display = ('location',)","    inlines = [EventShiftInline]"],"id":427}],[{"start":{"row":28,"column":11},"end":{"row":28,"column":19},"action":"remove","lines":["Location"],"id":428},{"start":{"row":28,"column":11},"end":{"row":28,"column":12},"action":"insert","lines":["S"]},{"start":{"row":28,"column":12},"end":{"row":28,"column":13},"action":"insert","lines":["h"]},{"start":{"row":28,"column":13},"end":{"row":28,"column":14},"action":"insert","lines":["i"]},{"start":{"row":28,"column":14},"end":{"row":28,"column":15},"action":"insert","lines":["f"]},{"start":{"row":28,"column":15},"end":{"row":28,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":32},"action":"remove","lines":["    list_display = ('location',)"],"id":431},{"start":{"row":29,"column":0},"end":{"row":29,"column":49},"action":"insert","lines":["fields = ('location', 'employee', 'arrival_time')"]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":432}],[{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":433},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["m"],"id":434},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["o"]},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["d"]},{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["e"]},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":[" "],"id":435},{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["="]}],[{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":[" "],"id":436},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["E"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["v"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["e"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["n"]},{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["t"]},{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":["S"]},{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"insert","lines":["h"]}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["i"],"id":437},{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["f"]},{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["    inlines = [EventShiftInline]",""],"id":438}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":10},"action":"remove","lines":["fields"],"id":439},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"insert","lines":["l"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"insert","lines":["i"]},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"insert","lines":["s"]},{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["t"]},{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["_"]},{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["d"]},{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["i"]},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["s"]},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["p"]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["l"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["a"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["    model = EventShift",""],"id":440}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":10},"action":"remove","lines":["fields"],"id":441},{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["l"]},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["i"]},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["s"]},{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["t"]},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["_"]},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["d"]},{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["i"]},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["s"]},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["p"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["l"]},{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["a"]},{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "],"id":442},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":47,"column":38},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":443}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":38},"action":"insert","lines":["admin.site.register(Event, EventAdmin)"],"id":444}],[{"start":{"row":48,"column":38},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":445}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":38},"action":"insert","lines":["admin.site.register(Event, EventAdmin)"],"id":446}],[{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"insert","lines":["S"],"id":447},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["c"]},{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"insert","lines":["h"]},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"insert","lines":["e"]},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["d"]},{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"insert","lines":["u"]},{"start":{"row":48,"column":31},"end":{"row":48,"column":32},"action":"insert","lines":["l"]},{"start":{"row":48,"column":32},"end":{"row":48,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":49,"column":25},"end":{"row":49,"column":26},"action":"insert","lines":["L"],"id":448},{"start":{"row":49,"column":26},"end":{"row":49,"column":27},"action":"insert","lines":["o"]},{"start":{"row":49,"column":27},"end":{"row":49,"column":28},"action":"insert","lines":["c"]},{"start":{"row":49,"column":28},"end":{"row":49,"column":29},"action":"insert","lines":["a"]},{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"insert","lines":["t"]},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["i"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":["o"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":48,"column":40},"end":{"row":48,"column":41},"action":"insert","lines":["S"],"id":449},{"start":{"row":48,"column":41},"end":{"row":48,"column":42},"action":"insert","lines":["c"]},{"start":{"row":48,"column":42},"end":{"row":48,"column":43},"action":"insert","lines":["h"]},{"start":{"row":48,"column":43},"end":{"row":48,"column":44},"action":"insert","lines":["e"]},{"start":{"row":48,"column":44},"end":{"row":48,"column":45},"action":"insert","lines":["d"]},{"start":{"row":48,"column":45},"end":{"row":48,"column":46},"action":"insert","lines":["u"]},{"start":{"row":48,"column":46},"end":{"row":48,"column":47},"action":"insert","lines":["l"]},{"start":{"row":48,"column":47},"end":{"row":48,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":49,"column":40},"end":{"row":49,"column":41},"action":"insert","lines":["L"],"id":450},{"start":{"row":49,"column":41},"end":{"row":49,"column":42},"action":"insert","lines":["o"]},{"start":{"row":49,"column":42},"end":{"row":49,"column":43},"action":"insert","lines":["c"]},{"start":{"row":49,"column":43},"end":{"row":49,"column":44},"action":"insert","lines":["a"]},{"start":{"row":49,"column":44},"end":{"row":49,"column":45},"action":"insert","lines":["t"]},{"start":{"row":49,"column":45},"end":{"row":49,"column":46},"action":"insert","lines":["i"]},{"start":{"row":49,"column":46},"end":{"row":49,"column":47},"action":"insert","lines":["o"]},{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"insert","lines":["n"]}],[{"start":{"row":32,"column":29},"end":{"row":32,"column":30},"action":"insert","lines":["s"],"id":451}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["e"],"id":452},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["v"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["e"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["n"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["t"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["_"]}],[{"start":{"row":18,"column":14},"end":{"row":18,"column":16},"action":"insert","lines":["''"],"id":453}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["e"],"id":454},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["v"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["e"]},{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["n"]},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["t"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["_"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["s"]},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["c"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["h"]},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["e"]},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["d"]},{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["u"]},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["l"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":[","],"id":455}],[{"start":{"row":32,"column":19},"end":{"row":32,"column":33},"action":"remove","lines":["('locations',)"],"id":456},{"start":{"row":32,"column":19},"end":{"row":32,"column":50},"action":"insert","lines":["('event_schedule','locations',)"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"remove","lines":["# "],"id":457},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":49,"column":54},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":458}],[{"start":{"row":50,"column":0},"end":{"row":50,"column":54},"action":"insert","lines":["admin.site.register(EventLocation, EventLocationAdmin)"],"id":459}],[{"start":{"row":50,"column":40},"end":{"row":50,"column":48},"action":"remove","lines":["Location"],"id":460},{"start":{"row":50,"column":40},"end":{"row":50,"column":41},"action":"insert","lines":["S"]},{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"insert","lines":["h"]},{"start":{"row":50,"column":42},"end":{"row":50,"column":43},"action":"insert","lines":["i"]},{"start":{"row":50,"column":43},"end":{"row":50,"column":44},"action":"insert","lines":["f"]},{"start":{"row":50,"column":44},"end":{"row":50,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":50,"column":25},"end":{"row":50,"column":33},"action":"remove","lines":["Location"],"id":461},{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"insert","lines":["s"]},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"insert","lines":["h"]},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"insert","lines":["i"]},{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"insert","lines":["f"]},{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"remove","lines":["r"],"id":462},{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"remove","lines":["f"]},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"remove","lines":["i"]},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"remove","lines":["h"]},{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"remove","lines":["s"]}],[{"start":{"row":50,"column":25},"end":{"row":50,"column":26},"action":"insert","lines":["S"],"id":463},{"start":{"row":50,"column":26},"end":{"row":50,"column":27},"action":"insert","lines":["h"]},{"start":{"row":50,"column":27},"end":{"row":50,"column":28},"action":"insert","lines":["i"]},{"start":{"row":50,"column":28},"end":{"row":50,"column":29},"action":"insert","lines":["f"]},{"start":{"row":50,"column":29},"end":{"row":50,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":46,"column":0},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":464},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":48,"column":0},"end":{"row":48,"column":48},"action":"insert","lines":["admin.site.register(EventShift, EventShiftAdmin)"],"id":465}],[{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"remove","lines":["admin.site.register(EventShift, EventShiftAdmin)",""],"id":466}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":54},"action":"remove","lines":["admin.site.register(EventLocation, EventLocationAdmin)"],"id":467}],[{"start":{"row":48,"column":48},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":468}],[{"start":{"row":49,"column":0},"end":{"row":49,"column":54},"action":"insert","lines":["admin.site.register(EventLocation, EventLocationAdmin)"],"id":469}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":54},"action":"remove","lines":["admin.site.register(EventSchedule, EventScheduleAdmin)"],"id":470}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":471}],[{"start":{"row":50,"column":0},"end":{"row":50,"column":54},"action":"insert","lines":["admin.site.register(EventSchedule, EventScheduleAdmin)"],"id":472}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":6},"action":"remove","lines":["# "],"id":477}],[{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"remove","lines":["t"],"id":478},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"remove","lines":["f"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"remove","lines":["i"]},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"remove","lines":["h"]},{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"remove","lines":["S"]}],[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":["L"],"id":479},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["o"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["c"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["a"]},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["t"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["i"]},{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":["o"]},{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "],"id":480},{"start":{"row":39,"column":4},"end":{"row":40,"column":0},"action":"remove","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":74},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":482}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":19},"action":"insert","lines":["import nested_admin"],"id":483}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "],"id":484},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":42},"action":"remove","lines":["admin.StackedInline"],"id":486},{"start":{"row":13,"column":23},"end":{"row":13,"column":55},"action":"insert","lines":["nested_admin.NestedStackedInline"]}],[{"start":{"row":17,"column":26},"end":{"row":17,"column":45},"action":"remove","lines":["admin.StackedInline"],"id":487},{"start":{"row":17,"column":26},"end":{"row":17,"column":58},"action":"insert","lines":["nested_admin.NestedStackedInline"]}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":45},"action":"remove","lines":["admin.StackedInline"],"id":488},{"start":{"row":22,"column":26},"end":{"row":22,"column":58},"action":"insert","lines":["nested_admin.NestedStackedInline"]}],[{"start":{"row":40,"column":17},"end":{"row":40,"column":33},"action":"remove","lines":["admin.ModelAdmin"],"id":489},{"start":{"row":40,"column":17},"end":{"row":40,"column":46},"action":"insert","lines":["nested_admin.NestedModelAdmin"]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["# "],"id":490},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":13,"column":42},"end":{"row":13,"column":49},"action":"remove","lines":["Stacked"],"id":491},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"insert","lines":["T"]},{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"insert","lines":["a"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["b"]},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["u"]},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["l"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["a"]},{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["r"]}],[{"start":{"row":17,"column":45},"end":{"row":17,"column":52},"action":"remove","lines":["Stacked"],"id":492},{"start":{"row":17,"column":45},"end":{"row":17,"column":52},"action":"insert","lines":["Tabular"]}],[{"start":{"row":22,"column":45},"end":{"row":22,"column":52},"action":"remove","lines":["Stacked"],"id":493},{"start":{"row":22,"column":45},"end":{"row":22,"column":52},"action":"insert","lines":["Tabular"]}],[{"start":{"row":28,"column":0},"end":{"row":38,"column":37},"action":"remove","lines":["","# class EventShiftAdmin(admin.ModelAdmin):","#     list_display = ('location', 'employee', 'arrival_time')","","# class EventLocationAdmin(admin.ModelAdmin):","#     list_display = ('event_schedule','locations',)","#     inlines = [EventShiftInline]","","# class EventScheduleAdmin(admin.ModelAdmin):","#     list_display = ('event','event_schedule_name',)","#     inlines = [EventLocationInline]"],"id":494},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["",""]},{"start":{"row":25,"column":35},"end":{"row":26,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":0},"end":{"row":36,"column":56},"action":"remove","lines":["# admin.site.register(EventShift, EventShiftAdmin)","# admin.site.register(EventLocation, EventLocationAdmin)","# admin.site.register(EventSchedule, EventScheduleAdmin)"],"id":495},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""]},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":0},"end":{"row":48,"column":75},"action":"remove","lines":["","# admin.site.register(Schedule, ScheduleAdmin)","    ","# class EventSchedule(models.Model):","#     event = models.OneToOneField(Event, on_delete=models.CASCADE,null=True, blank=True)","  ","# class EventLocation(models.Model):","#     event_schedule = models.ForeignKey(EventSchedule, on_delete=models.CASCADE,null=True, blank=True)","#     locations = models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)","","# class EventShift(Position):","#     event_location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)","#     employee = models.OneToOneField(Employee, on_delete=models.CASCADE,null=True, blank=True)","#     arrival_time = models.CharField(max_length=256,null=True, blank=True)"],"id":496},{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["",""]},{"start":{"row":33,"column":38},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["# admin.site.unregister(Schedule)","","","# class ShiftInline(admin.StackedInline):","#     model = Shift","#     # fields = (('event','location','position','employee','arrival_time'),)","#     fields = (('locations','position','employees','start_time'),)","","",""],"id":497},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":498}],[{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":[" "],"id":499},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":[","]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["t"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["f"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["i"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["h"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["S"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":44},"action":"remove","lines":["'event_schedule_name',"],"id":500}],[{"start":{"row":6,"column":31},"end":{"row":6,"column":33},"action":"insert","lines":["''"],"id":501}],[{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["p"],"id":502},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["o"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["s"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["i"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["t"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["i"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["o"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":[","],"id":503}],[{"start":{"row":6,"column":43},"end":{"row":6,"column":54},"action":"remove","lines":["'employee',"],"id":505},{"start":{"row":6,"column":42},"end":{"row":6,"column":43},"action":"remove","lines":[" "]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":25},"action":"insert","lines":["'employee',"],"id":506}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":52},"action":"remove","lines":["Tabular"],"id":507},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["S"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["t"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["a"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["c"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["k"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["e"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["t"],"id":508},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["n"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["e"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["v"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["E"]}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["t"],"id":509},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["n"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":["e"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["v"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["t"],"id":510},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["n"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["e"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["v"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"remove","lines":["E"]}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"remove","lines":["t"],"id":511},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"remove","lines":["n"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"remove","lines":["e"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["v"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":["E"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":15},"end":{"row":11,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"mode":"ace/mode/python"}},"timestamp":1532550116314,"hash":"24872f26d4dee8313642c6d4a8c6dc2f83cb7f39"}