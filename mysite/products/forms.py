from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(
    widget=forms.TextInput(
            attrs={
                'placeholder': 'title'
            }
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs= {
                'placeholder': 'your description',
                'class': 'new-class-name two',
                'id': 'my-id-for-textarea',
                'rows': 5,
                'cols': 20
            }
        )
    )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs= {
                'placeholder': 'your description',
                'class': 'new-class-name two',
                'id': 'my-id-for-textarea',
                'rows': 5,
                'cols': 20
            }
        )
    )
    price = forms.DecimalField()