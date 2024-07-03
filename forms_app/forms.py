from django import forms
from .models import Feedback, Project

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestions'),
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField()
    sender = forms.EmailField(required=False)

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        num_words = len(message.split())

        if num_words < 4:
            raise forms.ValidationError("Not Enough Words!")

        return message


# feedback form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

    def clean_message(self):
        msg = self.cleaned_data.get('message')
        no_of_words = len(msg.split())

        if no_of_words < 4:
            raise forms.ValidationError('too short message')

        return msg
    
    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data


# Project form with widgets
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic', 'languages', 'duration']
        # widgets: these control the appearance and behaviour of form inputs
        widgets = {
            'languages': forms.TextInput(attrs={'placeholder': 'Comma-seperated list'})
        }
