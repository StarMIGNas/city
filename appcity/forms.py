from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=250)
    slug = forms.SlugField(max_length=250)
    content = forms.CharField(widget=forms.Textarea())
    is_published = forms.BooleanField()
