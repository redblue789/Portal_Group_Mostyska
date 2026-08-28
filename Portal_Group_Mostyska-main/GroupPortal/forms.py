from django import forms
from .models import ForumTopic, ForumPost

class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title', 'description']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) < 2:
            raise forms.ValidationError("Повідомлення занадто коротке.")
        return content