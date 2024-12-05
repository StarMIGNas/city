# from django import forms
#
#
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=250)
#     slug = forms.SlugField(max_length=250)
#     content = forms.CharField(widget=forms.Textarea())
#     is_published = forms.BooleanField()

from django import forms
from .models import City  # Импортируйте вашу модель City

class AddPostForm(forms.ModelForm):
    class Meta:
        model = City  # Указываем модель, для которой создается форма
        fields = ['title', 'slug', 'content', 'is_published', 'image']  # Указываем поля, которые будут в форме
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Настройка виджета для поля content
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if City.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Этот слаг уже используется. Пожалуйста, выберите другой.")
        return slug