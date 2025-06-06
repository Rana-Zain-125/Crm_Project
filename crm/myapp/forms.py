from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Record  # Import your model if needed


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.' , widget=forms.TextInput(attrs={'placeholder': 'First Name' , 'class': 'form-control'  }))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.' , widget=forms.TextInput(attrs={'placeholder': 'Last Name' , 'class': 'form-control'  }))
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.' , widget=forms.EmailInput(attrs={'placeholder': 'Email' , 'class': 'form-control'  }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddRecordForm(forms.ModelForm):
    
    product_name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control'}) , label="")
    product_Price =forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Product Price ', 'class': 'form-control'}),label="")
    selling_price = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Selling Price', 'class': 'form-control'}),label="")
    perchase_price =forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Purchase Price', 'class': 'form-control'}),label="")
    quantity =forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Quantity', 'class': 'form-control'}),label="")
    warranty_period =forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Warranty Period', 'class': 'form-control'}),label="")
    brand =forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Brand', 'class': 'form-control'}),label="")

    class Meta:
        model = Record
        exclude = ['user'] 