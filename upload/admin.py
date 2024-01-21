from django.contrib import admin
from upload.models import noTip
from gatecode.models import addGate
from maps.models import AptMap

admin.site.register(noTip)
admin.site.register(addGate)
admin.site.register(AptMap)


# Register your models here.
