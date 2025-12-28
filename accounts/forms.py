from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg text-center',
            'placeholder': 'email@site.com',
            'id': 'signupSimpleLoginEmail',
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'js-toggle-password form-control form-control-lg text-center',
            'placeholder': '8+ characters required',
            'id': 'signupSimpleLoginPassword',
            'data-hs-toggle-password-options':'''{
                "target": "#changePassTarget",
                "defaultClass": "bi-eye-slash",
                "showClass": "bi-eye",
                "classChangeTarget": "#changePassIcon"
              }'''
        }), min_length=8,
    )