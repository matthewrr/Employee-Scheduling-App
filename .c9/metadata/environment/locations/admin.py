{"filter":false,"title":"admin.py","tooltip":"/locations/admin.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":20,"column":92},"action":"insert","lines":["class Event(models.Model):","    title = models.CharField(max_length=256)","    date = models.DateField(blank=False)","    doors_open = models.CharField(max_length=256,verbose_name=\"Doors Open\")","    alcohol = models.BooleanField(default=True)","    slug = models.SlugField()","    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE,null=True,blank=True)"],"id":3}],[{"start":{"row":12,"column":44},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":44},"end":{"row":12,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1532459777271,"hash":"60bd5d5d6e5727a39aa2d4ece3d40e20af6fce82"}