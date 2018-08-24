{"filter":false,"title":"admin.py","tooltip":"/schedules/admin.py","undoManager":{"mark":53,"position":53,"stack":[[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":17,"column":44},"action":"insert","lines":["from django.contrib import admin","from .models import Location, Position","","class PositionInline(admin.StackedInline):","    model = Position","    fields = (('position', 'code'),)","","class LocationAdmin(admin.ModelAdmin):","    list_display = ('title', 'location_id','bar',)","    fields = (('title','location_id','bar'),)","    inlines = [PositionInline]","","admin.site.register(Location, LocationAdmin)"],"id":3}],[{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["."]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["m"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["o"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["d"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["e"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["l"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":[" "],"id":5},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["i"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["m"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["p"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["r"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":18,"column":44},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":28,"column":25},"action":"insert","lines":["class Schedule(models.Model):","    title = models.CharField(max_length=256,blank=True,null=True)","    template = models.BooleanField(default=False)","    roster = JSONField(blank=True,null=True)","    # created_at = models.DateTimeField(auto_now_add=True)","    # updated_at = models.DateTimeField(auto_now=True)","    ","    def __str__(self):","        return self.title"],"id":9}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["S"],"id":10},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["c"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["h"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["e"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["d"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["u"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["l"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":0},"end":{"row":7,"column":38},"action":"remove","lines":["","from django.contrib import admin","from .models import Location, Position"],"id":11},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":28},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["."]}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["# Register your models here",""],"id":12}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["c"],"id":13},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["l"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["a"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["s"]},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":[" "],"id":14},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["S"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["h"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["e"],"id":15},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["h"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["c"],"id":16},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["h"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["e"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["d"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["u"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["e"],"id":17}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["l"],"id":18},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["A"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["d"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["m"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["i"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":19},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":21},"action":"insert","lines":["()"],"id":20}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"],"id":21},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["o"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["d"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["e"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["l"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["s"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["."]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["M"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["o"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["d"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["e"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["l"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["A"],"id":22},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["d"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["m"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["i"]},{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":38},"end":{"row":3,"column":39},"action":"insert","lines":[":"],"id":23}],[{"start":{"row":3,"column":39},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["s"],"id":25},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["l"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["e"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["d"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["o"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["m"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["a"],"id":26},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["d"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["m"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["i"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":50},"action":"insert","lines":["list_display = ('title', 'location_id','bar',)"],"id":27}],[{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"remove","lines":["d"],"id":28},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"remove","lines":["i"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"remove","lines":["_"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"remove","lines":["n"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"remove","lines":["o"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"remove","lines":["i"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"remove","lines":["t"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"remove","lines":["a"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"remove","lines":["c"]},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"remove","lines":["o"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"remove","lines":["l"]}],[{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":["t"],"id":29},{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":["e"]},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["m"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["p"]},{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":["l"]},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["a"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["t"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"remove","lines":["r"],"id":30},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"remove","lines":["a"]},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"remove","lines":["b"]}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["r"],"id":31},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["o"]},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"insert","lines":["s"]},{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"insert","lines":["t"]},{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"insert","lines":["e"]},{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":18,"column":0},"end":{"row":26,"column":25},"action":"remove","lines":["class Schedule(models.Model):","    title = models.CharField(max_length=256,blank=True,null=True)","    template = models.BooleanField(default=False)","    roster = JSONField(blank=True,null=True)","    # created_at = models.DateTimeField(auto_now_add=True)","    # updated_at = models.DateTimeField(auto_now=True)","    ","    def __str__(self):","        return self.title"],"id":33},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["",""]},{"start":{"row":16,"column":44},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":14,"column":30},"action":"remove","lines":["","class PositionInline(admin.StackedInline):","    model = Position","    fields = (('position', 'code'),)","","class LocationAdmin(admin.ModelAdmin):","    list_display = ('title', 'location_id','bar',)","    fields = (('title','location_id','bar'),)","    inlines = [PositionInline]"],"id":34},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":49},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":28},"action":"remove","lines":["Location"],"id":35},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["S"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["c"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["h"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["e"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["d"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["u"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["l"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["n"],"id":36},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["o"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["i"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["t"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["a"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["c"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["o"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["L"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["S"],"id":37},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["c"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["h"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["e"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["d"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["u"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["l"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":39},"end":{"row":4,"column":41},"action":"insert","lines":["''"],"id":38}],[{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":[","],"id":39}],[{"start":{"row":4,"column":42},"end":{"row":4,"column":44},"action":"insert","lines":["''"],"id":40}],[{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"insert","lines":[","],"id":41}],[{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["c"],"id":42},{"start":{"row":4,"column":41},"end":{"row":4,"column":42},"action":"insert","lines":["r"]},{"start":{"row":4,"column":42},"end":{"row":4,"column":43},"action":"insert","lines":["e"]},{"start":{"row":4,"column":43},"end":{"row":4,"column":44},"action":"insert","lines":["a"]},{"start":{"row":4,"column":44},"end":{"row":4,"column":45},"action":"insert","lines":["t"]},{"start":{"row":4,"column":45},"end":{"row":4,"column":46},"action":"insert","lines":["e"]},{"start":{"row":4,"column":46},"end":{"row":4,"column":47},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":50},"end":{"row":4,"column":51},"action":"insert","lines":["m"],"id":43},{"start":{"row":4,"column":51},"end":{"row":4,"column":52},"action":"insert","lines":["o"]},{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":["d"]},{"start":{"row":4,"column":53},"end":{"row":4,"column":54},"action":"insert","lines":["i"]},{"start":{"row":4,"column":54},"end":{"row":4,"column":55},"action":"insert","lines":["f"]},{"start":{"row":4,"column":55},"end":{"row":4,"column":56},"action":"insert","lines":["i"]},{"start":{"row":4,"column":56},"end":{"row":4,"column":57},"action":"insert","lines":["e"]},{"start":{"row":4,"column":57},"end":{"row":4,"column":58},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":69},"end":{"row":4,"column":71},"action":"insert","lines":["''"],"id":44}],[{"start":{"row":4,"column":70},"end":{"row":4,"column":71},"action":"insert","lines":["a"],"id":45},{"start":{"row":4,"column":71},"end":{"row":4,"column":72},"action":"insert","lines":["c"]},{"start":{"row":4,"column":72},"end":{"row":4,"column":73},"action":"insert","lines":["t"]},{"start":{"row":4,"column":73},"end":{"row":4,"column":74},"action":"insert","lines":["i"]},{"start":{"row":4,"column":74},"end":{"row":4,"column":75},"action":"insert","lines":["v"]},{"start":{"row":4,"column":75},"end":{"row":4,"column":76},"action":"insert","lines":["e"]},{"start":{"row":4,"column":76},"end":{"row":4,"column":77},"action":"insert","lines":["_"]},{"start":{"row":4,"column":77},"end":{"row":4,"column":78},"action":"insert","lines":["l"]},{"start":{"row":4,"column":78},"end":{"row":4,"column":79},"action":"insert","lines":["o"]},{"start":{"row":4,"column":79},"end":{"row":4,"column":80},"action":"insert","lines":["c"]},{"start":{"row":4,"column":80},"end":{"row":4,"column":81},"action":"insert","lines":["a"]},{"start":{"row":4,"column":81},"end":{"row":4,"column":82},"action":"insert","lines":["t"]},{"start":{"row":4,"column":82},"end":{"row":4,"column":83},"action":"insert","lines":["i"]},{"start":{"row":4,"column":83},"end":{"row":4,"column":84},"action":"insert","lines":["o"]},{"start":{"row":4,"column":84},"end":{"row":4,"column":85},"action":"insert","lines":["n"]},{"start":{"row":4,"column":85},"end":{"row":4,"column":86},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":87},"end":{"row":4,"column":88},"action":"insert","lines":[","],"id":46}],[{"start":{"row":4,"column":88},"end":{"row":4,"column":90},"action":"insert","lines":["''"],"id":47}],[{"start":{"row":4,"column":89},"end":{"row":4,"column":90},"action":"insert","lines":["s"],"id":48},{"start":{"row":4,"column":90},"end":{"row":4,"column":91},"action":"insert","lines":["c"]},{"start":{"row":4,"column":91},"end":{"row":4,"column":92},"action":"insert","lines":["h"]},{"start":{"row":4,"column":92},"end":{"row":4,"column":93},"action":"insert","lines":["e"]},{"start":{"row":4,"column":93},"end":{"row":4,"column":94},"action":"insert","lines":["d"]},{"start":{"row":4,"column":94},"end":{"row":4,"column":95},"action":"insert","lines":["u"]},{"start":{"row":4,"column":95},"end":{"row":4,"column":96},"action":"insert","lines":["l"]},{"start":{"row":4,"column":96},"end":{"row":4,"column":97},"action":"insert","lines":["e"]},{"start":{"row":4,"column":97},"end":{"row":4,"column":98},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":60},"end":{"row":4,"column":69},"action":"remove","lines":["'roster',"],"id":49}],[{"start":{"row":4,"column":28},"end":{"row":4,"column":39},"action":"remove","lines":["'template',"],"id":50}],[{"start":{"row":4,"column":79},"end":{"row":4,"column":80},"action":"insert","lines":[","],"id":51}],[{"start":{"row":4,"column":80},"end":{"row":4,"column":91},"action":"insert","lines":["'template',"],"id":52}],[{"start":{"row":4,"column":80},"end":{"row":4,"column":82},"action":"insert","lines":["''"],"id":53}],[{"start":{"row":4,"column":81},"end":{"row":4,"column":82},"action":"insert","lines":["s"],"id":54},{"start":{"row":4,"column":82},"end":{"row":4,"column":83},"action":"insert","lines":["h"]},{"start":{"row":4,"column":83},"end":{"row":4,"column":84},"action":"insert","lines":["i"]},{"start":{"row":4,"column":84},"end":{"row":4,"column":85},"action":"insert","lines":["f"]},{"start":{"row":4,"column":85},"end":{"row":4,"column":86},"action":"insert","lines":["t"]},{"start":{"row":4,"column":86},"end":{"row":4,"column":87},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":88},"end":{"row":4,"column":89},"action":"insert","lines":[","],"id":55}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":89},"end":{"row":4,"column":89},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1535064174931,"hash":"cfababd6c12c72eb4f7c7a8dcde4b84d4ce7e356"}