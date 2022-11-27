from django.contrib import admin

from goals.models.board import Board
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal


class BaseAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")


class CategoryAdmin(BaseAdmin):
    pass


class GoalAdmin(BaseAdmin):
    list_display = ("title", "user", "category", "created", "updated")
    search_fields = ("title", "user", "category")


class CommentAdmin(BaseAdmin):
    list_display = ("goal", "user", "created", "updated")
    search_fields = ("goal", "user", "text")


class BoardAdmin(BaseAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Board, BoardAdmin)