from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy
from ckeditor.widgets import CKEditorWidget

from places.models import Place, Image


class PlaceAdmminForm(forms.ModelForm):
    description_long = forms.CharField(
        widget=CKEditorWidget(), label=gettext_lazy('Полное описание')
    )

    class Meta:
        model = Place
        fields = '__all__'


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px;" />', obj.image.url
            )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdmminForm
    inlines = [ImageInline]
