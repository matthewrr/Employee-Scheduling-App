{"filter":false,"title":"admin.py","tooltip":"/locations/admin.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":12,"column":44},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":44},"action":"insert","lines":["admin.site.register(Location, LocationAdmin)"],"id":8}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":28},"action":"remove","lines":["Location"],"id":9},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["P"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["o"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["s"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["i"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["t"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["i"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["o"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":30},"end":{"row":13,"column":38},"action":"remove","lines":["Location"],"id":10},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["P"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["o"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"insert","lines":["s"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["i"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["t"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["i"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["o"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":30},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":12,"column":0},"end":{"row":15,"column":30},"action":"insert","lines":["class LocationAdmin(admin.ModelAdmin):","    list_display = ('title', 'location_id','bar',)","    fields = (('title','location_id','bar'),)","    inlines = [PositionInline]"],"id":13}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["    inlines = [PositionInline]",""],"id":14}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["    fields = (('title','location_id','bar'),)",""],"id":15}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":14},"action":"remove","lines":["Location"],"id":16},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["P"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["o"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["s"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["i"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["t"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["i"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["o"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["e"],"id":17},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["l"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["t"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"remove","lines":["i"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["l"],"id":18},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["o"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["c"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["a"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":["t"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["i"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":["o"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":43},"end":{"row":13,"column":44},"action":"remove","lines":["d"],"id":19},{"start":{"row":13,"column":42},"end":{"row":13,"column":43},"action":"remove","lines":["i"]},{"start":{"row":13,"column":41},"end":{"row":13,"column":42},"action":"remove","lines":["_"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"remove","lines":["n"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"remove","lines":["o"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":["i"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":["t"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["a"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"remove","lines":["c"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"remove","lines":["o"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"remove","lines":["l"]}],[{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"insert","lines":["p"],"id":20},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"insert","lines":["o"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"insert","lines":["s"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"insert","lines":["i"]},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"insert","lines":["t"]},{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"insert","lines":["i"]},{"start":{"row":13,"column":39},"end":{"row":13,"column":40},"action":"insert","lines":["o"]},{"start":{"row":13,"column":40},"end":{"row":13,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"remove","lines":["r"],"id":21},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"remove","lines":["a"]},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"remove","lines":["b"]}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["c"],"id":22},{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["o"]},{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["d"]},{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":44},"end":{"row":16,"column":44},"action":"remove","lines":["","admin.site.register(Position, PositionAdmin)"],"id":23}],[{"start":{"row":12,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["class PositionAdmin(admin.ModelAdmin):","    list_display = ('location', 'position','code',)",""],"id":24}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":25}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":0},"end":{"row":12,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1534539033089,"hash":"34c3e1e0dccb2e8d401947186c3086f63e5c8eb0"}