from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            #first name
            self.fields["first_name"].widget.attrs.update({
                'name' : '',
                'class' : "form-control" ,
                'type' : "text"
            })
            #last name
            self.fields['last_name'].widget.attrs.update({
                'name' : '',
                'class' : "form-control" ,
                'type' : "text"
            })
            #email
            self.fields['email'].widget.attrs.update({
                'name':'',
                "class":"form-control",
                "type":"email"
            })
            #user Name
            self.fields['note'].widget.attrs.update({
                'name' : '',
                'class' : "form-control" ,
                'type' : "number"
            })
            #number
            self.fields['number'].widget.attrs.update({
                'name' : '',
                'class' : "form-control" ,
                'type' : "number"
            })
            #password2
            self.fields['photo'].widget.attrs.update({
                'name' : '',
                'class' : "form-control" ,
                'type' : "image"
                
            })
    class Meta:
        model=Student
        fields=["number","first_name","last_name","email","note","photo"]
        labels={
            'number':"Number",
            "first_name":"First Name",
            "last_name":"Last Name",
            "email":"Email",
            "note":"Note",
            "photo":"Photo"
        }
        # Widgets={
        #     'number':forms.NumberInput(attrs={'class':'form-control'}),
        #     "first_name":forms.TextInput(attrs={'class':'form-control'}),
        #     "last_name":forms.TextInput(attrs={'class':'form-control'}),
        #     "email":forms.EmailField(),
        #     "note":forms.TextInput(attrs={'class':'form-control'}),
        #     "photo":forms.ImageField()
        # }
                
        