{"filter":false,"title":"models.py","tooltip":"/locations/models.py","undoManager":{"mark":37,"position":37,"stack":[[{"start":{"row":2,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["# Create your models here."],"id":2},{"start":{"row":2,"column":0},"end":{"row":9,"column":25},"action":"insert","lines":["class Event(models.Model):","    event_id = models.IntegerField(blank=True)","    title = models.CharField(max_length=256)","    doors_open = models.CharField(max_length=256)","    # employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)","    ","    def __str__(self):","        return self.title"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["t"],"id":3},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["n"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["e"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["v"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["E"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["L"],"id":4},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["o"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["c"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["a"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["t"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["i"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["o"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":9},"action":"remove","lines":["event"],"id":8},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["l"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["o"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["c"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["t"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["i"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":94},"action":"remove","lines":["    doors_open = models.CharField(max_length=256)","    # employees = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)"],"id":9},{"start":{"row":4,"column":44},"end":{"row":5,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":10}],[{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":8,"column":0},"end":{"row":8,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "],"id":12},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":25},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":49},"action":"remove","lines":["models.IntegerField(blank=True)"],"id":13},{"start":{"row":3,"column":18},"end":{"row":3,"column":50},"action":"insert","lines":["models.CharField(max_length=256)"]}],[{"start":{"row":4,"column":44},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["d"],"id":15},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["e"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["f"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["a"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["u"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["l"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":["t"],"id":16},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["l"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["u"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["a"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":["f"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"remove","lines":["e"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"remove","lines":["d"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["p"],"id":17},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["o"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["s"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["i"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["t"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["i"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["o"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["n"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":[" "],"id":18},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":[" "],"id":19},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["m"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["o"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["d"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["e"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["."]}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"remove","lines":["."],"id":20}],[{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["l"],"id":21},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["s"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["."]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["I"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["n"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["e"],"id":22},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["g"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["e"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["r"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["F"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["i"]},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["e"]},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["l"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":37},"action":"insert","lines":["()"],"id":23}],[{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["d"],"id":24},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["e"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["f"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["a"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["u"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["l"]},{"start":{"row":5,"column":42},"end":{"row":5,"column":43},"action":"insert","lines":["t"]},{"start":{"row":5,"column":43},"end":{"row":5,"column":44},"action":"insert","lines":["="]}],[{"start":{"row":5,"column":44},"end":{"row":5,"column":45},"action":"insert","lines":["6"],"id":25}],[{"start":{"row":5,"column":46},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["m"],"id":27},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["a"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["n"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["a"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["g"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[" "],"id":28},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["_"],"id":30},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["r"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["o"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["l"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":[" "],"id":31}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":[" "],"id":32},{"start":{"row":6,"column":19},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"remove","lines":["e"],"id":33},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"remove","lines":["l"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"remove","lines":["o"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["r"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["p"],"id":34},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["o"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["s"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["i"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["t"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["i"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["o"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":23},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["p"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["r"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["e"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["p"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["_"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["p"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["o"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["i"],"id":36},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["t"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["i"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["o"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":[" "],"id":37},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"],"id":39},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["o"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["t"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["a"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["l"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["_"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":57},"action":"insert","lines":["models.BooleanField(default=False)"],"id":40}],[{"start":{"row":7,"column":20},"end":{"row":7,"column":54},"action":"insert","lines":["models.BooleanField(default=False)"],"id":41}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":42},{"start":{"row":7,"column":54},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":54},"end":{"row":7,"column":54},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1530636073258,"hash":"4df1753590d46d6487d6f9aaf175fac12aed4b17"}