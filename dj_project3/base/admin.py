from django.contrib import admin
from base.models import Players
from base.models import PlayerStats
from base.models import PlayerSessions
from base.models import PlayerAchievements
from base.models import LogGameEvents
# Register your models here.
admin.site.register(Players)
admin.site.register(PlayerStats)
admin.site.register(PlayerSessions)
admin.site.register(PlayerAchievements)
admin.site.register(LogGameEvents)