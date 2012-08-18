from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from vet_site.course_info.models import UserProfile, InfoSetting
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    key = forms.CharField(required=True)

    def clean_key(self):
        data = self.cleaned_data['key']
        key = InfoSetting.objects.get(key="SECURE_KEY")
        if key.value not in data:
            raise forms.ValidationError("Your Key Didnt Match")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data    
    
    def clean_email(self):
        data = self.cleaned_data['email']
        emailsplit = data.split("@")
        print emailsplit[0]
        print emailsplit[1]
        if len(emailsplit) != 2:
            raise forms.ValidationError("Incorrect email format")

        if emailsplit[1] != "cam.ac.uk":
            raise forms.ValidationError("Your Email is not a cambridge university email")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data  
    
    class Meta:
        model = User
        fields = ( "username", "email" )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile