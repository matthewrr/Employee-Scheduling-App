{"filter":false,"title":"forms.py","tooltip":"/employees/forms.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":18},"action":"insert","lines":["from django.forms import ModelForm","from .models import Event","","class EventForm(ModelForm):","    class Meta:","        model = Event","        fields = ['event_id', 'title', 'date', 'doors_open','alcohol','slug']","","form = EventForm()"],"id":1}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["t"],"id":2},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["n"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["e"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["v"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["E"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["E"],"id":3},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["m"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["p"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["l"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["o"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["y"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["t"],"id":4},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["n"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["e"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["v"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["E"],"id":5},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["M"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["p"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["l"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["o"],"id":6},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["l"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["p"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["M"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["m"],"id":7},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["p"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["l"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["y"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["e"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["t"],"id":8},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["n"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["e"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"remove","lines":["v"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["E"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["E"],"id":9},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["m"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["p"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["l"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["o"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["y"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["e"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":18},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":29,"column":31},"action":"insert","lines":["class Employee(models.Model):","    first_name = models.CharField(max_length=64, default='')","    last_name = models.CharField(max_length=64, default='')","    employee_id = models.CharField(max_length=8, default='')","    phone_regex = RegexValidator(regex=r'^\\+?1?\\d{9,15}$', message=\"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.\")","    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)","    active = models.BooleanField(default=True)","    food_permit = models.BooleanField(default=False)","    alcohol_permit = models.BooleanField(default=False)","    admin = models.BooleanField(default=False)","    ","    def name(self):","        return self.first_name + ' ' + self.last_name","        ","    def phone(self):","        p = self.phone_number","        return '({}) {}-{}'.format(p[:3],p[3:6],p[6:])","        ","    def __str__(self):","        return self.employee_id"],"id":11}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["t"],"id":12},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["n"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["e"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["v"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["E"]}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["E"],"id":13},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["m"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["p"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["l"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["o"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["y"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["e"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"remove","lines":["d"],"id":14},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"remove","lines":["i"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"remove","lines":["_"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["t"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["n"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["e"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["v"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["e"]}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["f"],"id":15},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["i"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["r"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["s"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["t"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["_"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["n"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["a"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["m"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"remove","lines":["e"],"id":16},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["l"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["t"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["i"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["t"]}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["l"],"id":17},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["a"]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["s"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["t"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["_"]},{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["n"]},{"start":{"row":6,"column":39},"end":{"row":6,"column":40},"action":"insert","lines":["a"]},{"start":{"row":6,"column":40},"end":{"row":6,"column":41},"action":"insert","lines":["m"]},{"start":{"row":6,"column":41},"end":{"row":6,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"remove","lines":["e"],"id":18},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"remove","lines":["t"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"remove","lines":["a"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"remove","lines":["d"]}],[{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["e"],"id":19},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["m"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"insert","lines":["p"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"insert","lines":["l"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"insert","lines":["o"]},{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"insert","lines":["y"]},{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"insert","lines":["e"]},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":["e"]},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"insert","lines":["_"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"insert","lines":["i"]},{"start":{"row":6,"column":56},"end":{"row":6,"column":57},"action":"insert","lines":["d"]}],[{"start":{"row":6,"column":70},"end":{"row":6,"column":71},"action":"remove","lines":["n"],"id":20},{"start":{"row":6,"column":69},"end":{"row":6,"column":70},"action":"remove","lines":["e"]},{"start":{"row":6,"column":68},"end":{"row":6,"column":69},"action":"remove","lines":["p"]},{"start":{"row":6,"column":67},"end":{"row":6,"column":68},"action":"remove","lines":["o"]},{"start":{"row":6,"column":66},"end":{"row":6,"column":67},"action":"remove","lines":["_"]},{"start":{"row":6,"column":65},"end":{"row":6,"column":66},"action":"remove","lines":["s"]},{"start":{"row":6,"column":64},"end":{"row":6,"column":65},"action":"remove","lines":["r"]},{"start":{"row":6,"column":63},"end":{"row":6,"column":64},"action":"remove","lines":["o"]},{"start":{"row":6,"column":62},"end":{"row":6,"column":63},"action":"remove","lines":["o"]},{"start":{"row":6,"column":61},"end":{"row":6,"column":62},"action":"remove","lines":["d"]}],[{"start":{"row":6,"column":61},"end":{"row":6,"column":62},"action":"insert","lines":["p"],"id":21},{"start":{"row":6,"column":62},"end":{"row":6,"column":63},"action":"insert","lines":["h"]},{"start":{"row":6,"column":63},"end":{"row":6,"column":64},"action":"insert","lines":["o"]},{"start":{"row":6,"column":64},"end":{"row":6,"column":65},"action":"insert","lines":["n"]},{"start":{"row":6,"column":65},"end":{"row":6,"column":66},"action":"insert","lines":["e"]},{"start":{"row":6,"column":66},"end":{"row":6,"column":67},"action":"insert","lines":["_"]},{"start":{"row":6,"column":67},"end":{"row":6,"column":68},"action":"insert","lines":["n"]},{"start":{"row":6,"column":68},"end":{"row":6,"column":69},"action":"insert","lines":["u"]},{"start":{"row":6,"column":69},"end":{"row":6,"column":70},"action":"insert","lines":["m"]},{"start":{"row":6,"column":70},"end":{"row":6,"column":71},"action":"insert","lines":["b"]},{"start":{"row":6,"column":71},"end":{"row":6,"column":72},"action":"insert","lines":["e"]},{"start":{"row":6,"column":72},"end":{"row":6,"column":73},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":82},"end":{"row":6,"column":83},"action":"remove","lines":["l"],"id":22},{"start":{"row":6,"column":81},"end":{"row":6,"column":82},"action":"remove","lines":["o"]},{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"remove","lines":["h"]},{"start":{"row":6,"column":79},"end":{"row":6,"column":80},"action":"remove","lines":["o"]},{"start":{"row":6,"column":78},"end":{"row":6,"column":79},"action":"remove","lines":["c"]},{"start":{"row":6,"column":77},"end":{"row":6,"column":78},"action":"remove","lines":["l"]},{"start":{"row":6,"column":76},"end":{"row":6,"column":77},"action":"remove","lines":["a"]}],[{"start":{"row":6,"column":76},"end":{"row":6,"column":77},"action":"insert","lines":["f"],"id":23},{"start":{"row":6,"column":77},"end":{"row":6,"column":78},"action":"insert","lines":["o"]},{"start":{"row":6,"column":78},"end":{"row":6,"column":79},"action":"insert","lines":["o"]},{"start":{"row":6,"column":79},"end":{"row":6,"column":80},"action":"insert","lines":["d"]},{"start":{"row":6,"column":80},"end":{"row":6,"column":81},"action":"insert","lines":["_"]},{"start":{"row":6,"column":81},"end":{"row":6,"column":82},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":81},"end":{"row":6,"column":82},"action":"remove","lines":["e"],"id":24}],[{"start":{"row":6,"column":81},"end":{"row":6,"column":82},"action":"insert","lines":["p"],"id":25},{"start":{"row":6,"column":82},"end":{"row":6,"column":83},"action":"insert","lines":["e"]},{"start":{"row":6,"column":83},"end":{"row":6,"column":84},"action":"insert","lines":["r"]},{"start":{"row":6,"column":84},"end":{"row":6,"column":85},"action":"insert","lines":["m"]},{"start":{"row":6,"column":85},"end":{"row":6,"column":86},"action":"insert","lines":["i"]},{"start":{"row":6,"column":86},"end":{"row":6,"column":87},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":93},"end":{"row":6,"column":94},"action":"remove","lines":["g"],"id":26},{"start":{"row":6,"column":92},"end":{"row":6,"column":93},"action":"remove","lines":["u"]},{"start":{"row":6,"column":91},"end":{"row":6,"column":92},"action":"remove","lines":["l"]},{"start":{"row":6,"column":90},"end":{"row":6,"column":91},"action":"remove","lines":["s"]}],[{"start":{"row":6,"column":90},"end":{"row":6,"column":91},"action":"insert","lines":["a"],"id":27},{"start":{"row":6,"column":91},"end":{"row":6,"column":92},"action":"insert","lines":["l"]},{"start":{"row":6,"column":92},"end":{"row":6,"column":93},"action":"insert","lines":["s"]},{"start":{"row":6,"column":93},"end":{"row":6,"column":94},"action":"insert","lines":["o"]}],[{"start":{"row":6,"column":93},"end":{"row":6,"column":94},"action":"remove","lines":["o"],"id":28},{"start":{"row":6,"column":92},"end":{"row":6,"column":93},"action":"remove","lines":["s"]}],[{"start":{"row":6,"column":92},"end":{"row":6,"column":93},"action":"insert","lines":["c"],"id":29},{"start":{"row":6,"column":93},"end":{"row":6,"column":94},"action":"insert","lines":["o"]},{"start":{"row":6,"column":94},"end":{"row":6,"column":95},"action":"insert","lines":["h"]},{"start":{"row":6,"column":95},"end":{"row":6,"column":96},"action":"insert","lines":["o"]},{"start":{"row":6,"column":96},"end":{"row":6,"column":97},"action":"insert","lines":["l"]},{"start":{"row":6,"column":97},"end":{"row":6,"column":98},"action":"insert","lines":["_"]},{"start":{"row":6,"column":98},"end":{"row":6,"column":99},"action":"insert","lines":["p"]},{"start":{"row":6,"column":99},"end":{"row":6,"column":100},"action":"insert","lines":["e"]},{"start":{"row":6,"column":100},"end":{"row":6,"column":101},"action":"insert","lines":["r"]},{"start":{"row":6,"column":101},"end":{"row":6,"column":102},"action":"insert","lines":["m"]},{"start":{"row":6,"column":102},"end":{"row":6,"column":103},"action":"insert","lines":["i"]},{"start":{"row":6,"column":103},"end":{"row":6,"column":104},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":105},"end":{"row":6,"column":106},"action":"insert","lines":[","],"id":30}],[{"start":{"row":6,"column":106},"end":{"row":6,"column":108},"action":"insert","lines":["''"],"id":31}],[{"start":{"row":6,"column":107},"end":{"row":6,"column":108},"action":"insert","lines":["a"],"id":32},{"start":{"row":6,"column":108},"end":{"row":6,"column":109},"action":"insert","lines":["c"]},{"start":{"row":6,"column":109},"end":{"row":6,"column":110},"action":"insert","lines":["t"]},{"start":{"row":6,"column":110},"end":{"row":6,"column":111},"action":"insert","lines":["i"]},{"start":{"row":6,"column":111},"end":{"row":6,"column":112},"action":"insert","lines":["v"]},{"start":{"row":6,"column":112},"end":{"row":6,"column":113},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":114},"end":{"row":6,"column":115},"action":"insert","lines":[","],"id":33}],[{"start":{"row":6,"column":115},"end":{"row":6,"column":117},"action":"insert","lines":["''"],"id":34}],[{"start":{"row":6,"column":116},"end":{"row":6,"column":117},"action":"insert","lines":["a"],"id":35},{"start":{"row":6,"column":117},"end":{"row":6,"column":118},"action":"insert","lines":["d"]},{"start":{"row":6,"column":118},"end":{"row":6,"column":119},"action":"insert","lines":["m"]},{"start":{"row":6,"column":119},"end":{"row":6,"column":120},"action":"insert","lines":["i"]},{"start":{"row":6,"column":120},"end":{"row":6,"column":121},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":0},"end":{"row":29,"column":31},"action":"remove","lines":["","class Employee(models.Model):","    first_name = models.CharField(max_length=64, default='')","    last_name = models.CharField(max_length=64, default='')","    employee_id = models.CharField(max_length=8, default='')","    phone_regex = RegexValidator(regex=r'^\\+?1?\\d{9,15}$', message=\"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.\")","    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)","    active = models.BooleanField(default=True)","    food_permit = models.BooleanField(default=False)","    alcohol_permit = models.BooleanField(default=False)","    admin = models.BooleanField(default=False)","    ","    def name(self):","        return self.first_name + ' ' + self.last_name","        ","    def phone(self):","        p = self.phone_number","        return '({}) {}-{}'.format(p[:3],p[3:6],p[6:])","        ","    def __str__(self):","        return self.employee_id"],"id":36},{"start":{"row":8,"column":21},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":9},"end":{"row":6,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":15,"mode":"ace/mode/python"}},"timestamp":1531101303766,"hash":"5f9f327303cf22c427dea8c33cab3e6965823738"}