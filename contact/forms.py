from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=20, required=True)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
    placeholders = {
        'name': 'name',
        'email': 'email',
        'message': 'message',
    }
