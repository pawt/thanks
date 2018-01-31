from django import forms
from .models import Transaction, Employee

class TransactionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].empty_label = "Select the person"
        self.fields['points_given'].initial = 1  # selecting the first option (1 point) as a default

    class Meta:
        model = Transaction
        fields = ['receiver', 'description', 'points_given']
        labels = {
            'receiver': ('Who do you want to thank?'),
            'description': ('Why do you want to thank?'),
            'points_given': ('How many points do you want to give?'),
        }
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Enter description here'}),
            'points_given': forms.Select(attrs={'placeholder': 'Enter number of points (min. 1 / max. 3)'}),
        }
