from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Board, Entry, Tag


class BoardAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'owner')
    list_filter = ('owner', )
    filter_horizontal = ('users', )


class EntryAdmin(admin.ModelAdmin):

    list_display = ('description', 'value', 'type', 'date', 'board', 'tag')
    list_filter = ('date', 'board', 'tag')
    search_fields = ('description', )

    def type(self, obj):
        return _('Income') if obj.is_income else _('Outcome')

    type.short_description = _('Type')


class TagAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')


admin.site.register(Board, BoardAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag, TagAdmin)
