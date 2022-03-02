from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag


class RelationshipInlineFormset(BaseInlineFormSet):

    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                count = count + 1
                if count > 1:
                    raise ValidationError('Основным может быть только один раздел')
                else:
                    raise ValidationError('Укажите основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleTag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]