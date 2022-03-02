from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):

    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                count = count + 1
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    list_filter = ['published_at']
    inlines = [ArticleTagInline]