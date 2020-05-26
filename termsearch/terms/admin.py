from django.contrib import admin

from .models import Term

class TermAdmin(admin.ModelAdmin):
    list_display = ("name", "bash", "mean")


admin.site.register(Term, TermAdmin)
#
# class SportTermAdmin(admin.ModelAdmin):
#     list_display = ("name", "bash", "mean")
# admin.site.register(SportTerm, SportTermAdmin)
