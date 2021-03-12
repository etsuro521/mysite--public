from django import forms
from . models import Topic, Comment


class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=[
            'title',
            'category',
            'message',
        ]
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'hoge'}),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '選択して下さい'
    
    def save(self, user, commit=True, **kwargs):
        topic = super().save(commit=False)
        topic.user = user
        topic.user_name = user.username
        if commit:
            topic.save()
        return topic

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'message',
        ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    def save_with_topic(self, topic_id, user, commit=True, **kwargs):
        comment = self.save(commit=False)
        comment.topic = Topic.objects.get(id=topic_id)
        comment.no = Comment.objects.filter(topic_id=topic_id).count() + 1
        comment.user = user
        comment.user_name = user.username
        if commit:
            comment.save()
        return comment

