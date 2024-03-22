from django import forms

class addBook(forms.Form):

    name=forms.CharField(max_length=255)
    price=forms.IntegerField()
