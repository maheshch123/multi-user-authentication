from django import forms
from accounts.models import marks

class stform(forms.ModelForm):
    class Meta:
        model = marks
        fields = "__all__"