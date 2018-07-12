{"filter":false,"title":"models.py","tooltip":"/company_profile/models.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":0},"end":{"row":5,"column":20},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"93fae16d61dd08c8cf8225f25db0f840cb2f5863","undoManager":{"mark":31,"position":31,"stack":[[{"start":{"row":3,"column":0},"end":{"row":31,"column":25},"action":"insert","lines":["from django.db import models","from django.template.defaultfilters import slugify","from employees.models import Employee","from locations.models import Location","import datetime","","class Event(models.Model):","    event_id = models.IntegerField(blank=True)","    title = models.CharField(max_length=256)","    date = models.DateField(blank=False)","    doors_open = models.CharField(max_length=256)","    alcohol = models.BooleanField(default=True)","    locations = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)","    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)","    slug = models.SlugField()","    ","    def expired(self):","        return True if self.date < datetime.date.today() else False","    ","    def get_absolute_url(self):","        return ('blog_post_detail', None, {'slug' :self.slug,})","","    def save(self, *args, **kwargs):","        if not self.slug:","            self.slug = slugify(self.title)","        super(Event, self).save(*args, **kwargs)","    ","    def __str__(self):","        return self.title"],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":28},"action":"remove","lines":["from django.db import models"],"id":3},{"start":{"row":2,"column":26},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["t"],"id":4},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["n"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["e"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["v"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["C"],"id":5},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["o"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["m"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["p"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["a"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["y"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["P"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["r"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["f"],"id":6},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["i"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["l"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["c"],"id":8},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["o"]},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["m"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["a"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["p"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["n"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":["y"],"id":9},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["n"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":["p"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"remove","lines":["a"]}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["p"],"id":10},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["a"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["n"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["y"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["_"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["n"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["a"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["m"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":[" "],"id":11},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":[" "],"id":12},{"start":{"row":9,"column":19},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]},{"start":{"row":11,"column":4},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["c"],"id":13},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["o"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["m"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["a"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["p"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["n"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"remove","lines":["y"],"id":14},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"remove","lines":["n"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"remove","lines":["p"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"remove","lines":["a"]}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["p"],"id":15},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["a"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["n"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":[" "],"id":16},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["l"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["o"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["g"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":["o"],"id":17},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"remove","lines":["g"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"remove","lines":["o"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"remove","lines":["l"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["_"],"id":18},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["l"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["o"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["g"]},{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":[" "],"id":19},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":9,"column":19},"end":{"row":9,"column":51},"action":"insert","lines":["models.CharField(max_length=256)"],"id":21}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["p"],"id":22},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["a"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["s"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":6},"action":"insert","lines":["# "],"id":23}],[{"start":{"row":10,"column":25},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["#"],"id":25},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["a"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["d"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["m"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["i"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":[" "],"id":26},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["u"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["s"],"id":27},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["u"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":[" "]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["n"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":["i"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"remove","lines":["m"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"remove","lines":["d"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"remove","lines":["a"]}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":[" "],"id":28},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["f"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["k"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":[" "],"id":29},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["a"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["d"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["m"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["i"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":[" "],"id":30},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["u"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["s"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["e"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["r"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":0},"end":{"row":32,"column":48},"action":"remove","lines":["    ","    event_id = models.IntegerField(blank=True)","    title = models.CharField(max_length=256)","    date = models.DateField(blank=False)","    doors_open = models.CharField(max_length=256)","    alcohol = models.BooleanField(default=True)","    locations = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)","    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)","    slug = models.SlugField()","    ","    def expired(self):","        return True if self.date < datetime.date.today() else False","    ","    def get_absolute_url(self):","        return ('blog_post_detail', None, {'slug' :self.slug,})","","    def save(self, *args, **kwargs):","        if not self.slug:","            self.slug = slugify(self.title)","        super(Event, self).save(*args, **kwargs)"],"id":31},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"remove","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":20},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":15},"action":"remove","lines":["from django.template.defaultfilters import slugify","from employees.models import Employee","from locations.models import Location","import datetime"],"id":32},{"start":{"row":2,"column":26},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["","# Create your models here."],"id":33},{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"timestamp":1531272211696}