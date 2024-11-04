from django import forms 

from BlogApp.models import Blog, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'style': 'height: 70px;'  # Set the fixed height here
            }),
        }