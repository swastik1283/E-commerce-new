from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from product.models import customerdetail

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True' ,'class':'form-control'}))
    password = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class registrationform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True' ,'class':'form-control'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password" ,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class password_change_1(PasswordChangeForm):
    old_password = forms.CharField(label='old Password' ,widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))   

# class mysetpassword(SetPasswordForm):
#     new_password11 = forms.CharField(label='New Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))  
#     new_password12 = forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))   

# class passwordresetform(PasswordResetForm):
#     email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}))
    

class customerprofile(forms.ModelForm):
    class Meta:
        model = customerdetail
        fields = ['name','locality','city','mobile','pincode','state']
        widgets = {
        'name':forms.TextInput(attrs={'autofocus':'True' ,'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'mobile':forms.NumberInput(attrs={'class':'form-control'}),
        'pincode':forms.NumberInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'})
    }
        # name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True' ,'class':'form-control'}))
        # locality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        # city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        # mobile = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        # pincode = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
        # state = forms.ChoiceField(widget=forms.Select( attrs={'class':'form-control'}))
        