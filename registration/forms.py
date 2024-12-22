from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1',
                                                                  'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2',
                                                                  'placeholder': 'Confirmation Password'}),
                                required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',
                                                          'id': 'email'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'id': 'name'}),
                           required=True)
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname',
                                                            'id': 'surname'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'id': 'phone_number',
                                                          'placeholder': '577-777-777'}))

    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('name', 'email', 'surname', 'phone')

    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': "form-control",
                                                                          'id': 'email',
                                                                          "placeholder": "email",
                                                                          "type": "email",
                                                                          "name": "email"}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'surname',
                                                            'placeholder': 'Surname'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'phone_number',
                                                          'minlength': '9', 'maxlength': '9', 'placeholder': '577-777-777'}))


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': "form-control mb-4",
                                                                          'id': 'email',
                                                                          "placeholder": "",
                                                                          "type": "email",
                                                                          "name": "email"}))

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                                   'id': 'password',
                                                                                   "type": "password",
                                                                                   "name": "password",
                                                                                   'placeholder': ''}))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        non_field_errors() because it doesn't apply to a single
        field.

        """
        if 'email' not in self.cleaned_data and 'password' not in self.cleaneddata:
            raise forms.ValidationError("please fill the forms")
        return self.cleaned_data
