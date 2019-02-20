from django.contrib import admin
from acc.models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','body','active')
    list_filter=('active',)
    search_fields=('name','email','body')

admin.site.register(Comment,CommentAdmin)
