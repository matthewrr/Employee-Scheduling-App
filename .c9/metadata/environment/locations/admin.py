{"filter":false,"title":"admin.py","tooltip":"/locations/admin.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":3,"column":0},"end":{"row":6,"column":30},"action":"insert","lines":["class LocationAdmin(admin.ModelAdmin):","    list_display = ('title', 'location_id','bar',)","    fields = (('title','location_id','bar'),)","    inlines = [PositionInline]"],"id":2}],[{"start":{"row":1,"column":38},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":1},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":38},"end":{"row":1,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"mode":"ace/mode/python"}},"timestamp":1532459777271,"hash":"60bd5d5d6e5727a39aa2d4ece3d40e20af6fce82"}