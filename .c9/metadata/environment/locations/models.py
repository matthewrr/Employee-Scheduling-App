{"filter":false,"title":"models.py","tooltip":"/locations/models.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":5,"column":44},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":15,"column":58},"action":"insert","lines":["created      = models.DateTimeField(editable=False,null=True)","    modified     = models.DateTimeField(null=True)","","    def save(self, *args, **kwargs):","        ''' On save, update timestamps '''","        if not self.id:","            self.created = timezone.now()","        self.modified = timezone.now()","        return super(Schedule, self).save(*args, **kwargs)"],"id":3}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["    ",""],"id":4}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["e"],"id":5},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["l"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["u"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["d"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["e"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["h"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["c"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["S"]}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["L"],"id":6},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["o"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["c"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["a"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["t"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["i"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["o"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":33},"action":"insert","lines":["from django.utils import timezone"],"id":8}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":33},"end":{"row":1,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1534908503270,"hash":"559c8affb9af4b4ccbc335521ed94ffbdc74a340"}