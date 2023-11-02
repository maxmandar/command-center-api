
from django.contrib import admin
from .models import Rocket, Stage
from simple_history.admin import SimpleHistoryAdmin

@admin.register(Rocket)
class RocketAdmin(SimpleHistoryAdmin):
    pass

@admin.register(Stage)
class StageAdmin(SimpleHistoryAdmin):
    pass
    
