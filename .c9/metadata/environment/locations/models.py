{"filter":false,"title":"models.py","tooltip":"/locations/models.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":2,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["# Create your models here."],"id":2},{"start":{"row":2,"column":0},"end":{"row":9,"column":25},"action":"insert","lines":["class Event(models.Model):","    event_id = models.IntegerField(blank=True)","    title = models.CharField(max_length=256)","    doors_open = models.CharField(max_length=256)","    # employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)","    ","    def __str__(self):","        return self.title"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["t"],"id":3},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["n"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["e"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["v"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["L"],"id":4},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["o"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["c"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["a"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["t"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["i"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["o"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":9},"action":"remove","lines":["event"],"id":8},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["l"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["o"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["c"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["t"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["i"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":94},"action":"remove","lines":["    doors_open = models.CharField(max_length=256)","    # employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)"],"id":9},{"start":{"row":4,"column":44},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":10}],[{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":8,"column":0},"end":{"row":8,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "],"id":12},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":49},"action":"remove","lines":["models.IntegerField(blank=True)"],"id":13},{"start":{"row":3,"column":18},"end":{"row":3,"column":50},"action":"insert","lines":["models.CharField(max_length=256)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":50},"end":{"row":3,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1530550614380,"hash":"d60b590cc1855b94f29e67951774accf4b71a31b"}