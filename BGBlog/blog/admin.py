from django.contrib import admin, messages
from django.utils.translation import ngettext
from .models import Article, Category

#Admin Header Change
admin.site.site_header = 'Weblog'


# Register your models here.
@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status="p")
    modeladmin.message_user(
            request,
            ngettext(
                "%d story was successfully marked as published.",
                "%d stories were successfully marked as published.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

@admin.action(description="Mark selected stories as drafted")
def make_drafted(modeladmin, request, queryset):
    updated = queryset.update(status="d")
    modeladmin.message_user(
            request,
            ngettext(
                "%d story was successfully marked as drafted.",
                "%d stories were successfully marked as drafted.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_tag", "author", "slug", "publish", "is_special", "status", "category_to_str")
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published, make_drafted]


admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", "title", "slug", "parent",  "status")
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
