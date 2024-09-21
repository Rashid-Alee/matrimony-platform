from django import forms

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .models import Profile
from django.forms import ModelForm


def my_email_validator(email):
    if email.split("@")[1].split(".")[0].lower() == "hotmail":
        raise ValidationError("Email Not Acceptable")


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        initial="",  # Ensure no default value
        widget=forms.TextInput(attrs={"placeholder": ""}),  # No placeholder text
    )
    email = forms.EmailField(
        validators=[EmailValidator(), my_email_validator],
        initial="",
        widget=forms.EmailInput(attrs={"placeholder": ""}),
    )
    verify_email = forms.EmailField(
        initial="", widget=forms.EmailInput(attrs={"placeholder": ""})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": ""}), initial=""
    )

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        verify_email = cleaned_data.get("verify_email")
        message = cleaned_data.get("message")

        # Check if both email and verify_email exist before calling .lower()
        if email:
            cleaned_data["email"] = email.lower()
        if verify_email:
            cleaned_data["verify_email"] = verify_email.lower()

        # Check for email mismatch only if both email fields are present
        if email and verify_email:
            if cleaned_data["email"] != cleaned_data["verify_email"]:
                raise forms.ValidationError("Emails do not match")

        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
