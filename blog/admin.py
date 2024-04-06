from django.contrib import admin
from blog.models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class Postadmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('title','author','counted_views','status','login_required','published_date','created_date',)
    empty_value_display = '-empty-'
    list_filter=('status','author')
    summernote_fields = ('content',)
    #ordering=['-created_date']
    search_fields=['title','content']

class Commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display=('name','post','approwed','created_date',)
    empty_value_display = '-empty-'
    list_filter=('post','approwed')
    search_fields=['name','post']



admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Comment,Commentadmin)