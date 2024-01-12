import self as self
from django import forms
from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    columns = 2  # Cambia esto según la cantidad de columnas que desees

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.generate_columns_layout()

    def generate_columns_layout(self):
        fields_per_column = len(self.fields) // self.columns if self.fields else 1
        layout = Layout()

        for i in range(0, fields_per_column):
            current_fields = list(self.fields.keys())[i::fields_per_column]
            layout.append(
                Row(*[Column(field, css_class=f'form-group col-md-{12//fields_per_column} mb-0') for field in current_fields], css_class='form-row')
            )

        layout.append('check_me_out')
        layout.append(Submit('submit', 'Sign in'))

        return layout


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['title', 'description', 'project']

