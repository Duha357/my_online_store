from django import forms
# from products.models import Category


class CategoryForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-field__control'
            }
        )
    )
    snippet = forms.CharField(
        label='Description',
        required=False,
        widget=forms.widgets.Textarea(
            attrs={
                'class': 'form-field__control'
            }
        )
    )

# Более меньшая и сокращённая версия, чем выше
# class CategoryModelForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['title', 'snippet']
#         widgets = {
#             'title': forms.widgets.TextInput(
#                 attrs={
#                     'class': 'form-field__control'
#                 }
#             ),
#             'snippet': forms.widgets.Textarea(
#                 attrs={
#                     'class': 'form-field__control'
#                 }
#             )
#         }