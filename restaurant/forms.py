from django import forms

# creating a form  
class ReserveForm(forms.Form): 
   
    first_name = forms.CharField(label='First Name',max_length = 100) 
    last_name = forms.CharField(label='Last Name',max_length = 100) 
    email = forms.EmailField( label='Email Address',max_length = 200 )
    date= forms.DateField()
    persons = forms.IntegerField()

                     
    