from django import forms

from application.models import Student, Login, MonthlyPackage, HalfPackage, \
    YearlyPackage, NewAdmin


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'enter your name'}),
            'phone_no':forms.TextInput(attrs={'class': 'form-control','placeholder':'enter your phone number'}),
            'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'enter your email'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder':'enter your password'}),
        }

class  LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'


#  classes objects


class  MonthlyPackageForm(forms.ModelForm):
    class Meta:
        model = MonthlyPackage
        fields = '__all__'

        # enter number you paid with
        widgets = {}



class HalfPackageForm(forms.ModelForm):
    class Meta:
        model = HalfPackage
        fields = '__all__'

        # enter number you paid with

        widgets = {}

class YearlyPackageForm(forms.ModelForm):
    class Meta:
        model = YearlyPackage
        fields = '__all__'

        widgets = {}

class NewAdminForm(forms.ModelForm):
    class Meta:
        model = NewAdmin
        fields = '__all__'

        widgets = {}