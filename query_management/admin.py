from django.contrib import admin
from .models import Query, Token, TimeSlot


class QueryAdmin(admin.ModelAdmin):
    list_display = ('student', 'query_type',
                    'created_at', 'modified_at', 'email',
                    'phone')
    list_filter = ('query_type', 'student', 'email',
                   'phone')
    search_fields = ('query_type', 'student', 'email',
                     'phone')
    ordering = ('created_at',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'token', 'slot_id')
    list_filter = ('student_id', 'token', 'slot_id')
    search_fields = ('token', 'student_id', 'slot_id')


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id',)
    list_filter = ('date', 'slot_id')
    search_fields = ('date', 'slot_id')


admin.site.register(Query, QueryAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)
