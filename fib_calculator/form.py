from django import forms


class FibInputForm(forms.Form):
    num_field = forms.IntegerField(label='Fib Number', min_value=1)
