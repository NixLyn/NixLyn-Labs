from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    ('purple','PURPLE'),
    ('white','WHITE'),
)

CURRENT_COURSE = (
    ('RedTeam', 'Red_Team'),
    ('BlueTeam', 'Blue_Team'),
    ('DevOps', 'Dev_Ops'),
    ('FrontEnd', 'Front_End'),
    ('BackEnd', 'Back_End'),
    ('PyData', 'PyData'),
    ('Q-Sec', 'Quantum_Security'),
    ("Lab Rat", "Frankie's Course"),
)

PERMS_C = (
    ('0', 'free'),
    ('1', 'paid'),
    ('2', 'promo')
)


class SignUpForm(UserCreationForm):
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',}))
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)


    class meta:
        model   = User
        fields  = ('username', 'first_name', 'last_name',  'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'forms-control'
        self.fields['password1'].widget.attrs['class'] = 'forms-control'
        self.fields['password2'].widget.attrs['class'] = 'forms-control'


class EditProfileForm(UserChangeForm):
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type':'optional',}))
    first_name      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',}))
    username        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', }))


    class meta:
        model   = User
        fields  = ('username', 'first_name', 'last_name', 'email')
