from django import forms
from jitterbunkapp.models import Bunk,User
from datetime import datetime


class BunkForm(forms.ModelForm):
    from_user = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                       queryset=User.objects.all())
    time = forms.DateTimeField(widget=forms.HiddenInput())

    # An inline class to provide additional information on the form.
    class Meta:
        model = Bunk
