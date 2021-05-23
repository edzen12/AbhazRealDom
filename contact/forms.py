from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = (
            'type_property',
            'own',
            'city',
            'areas',
            'floor',
            'price',
            'number',
        )
        TYPE_PROPERTY = (
            ('Квартира', 'Квартира'),
            ('Дом', 'Дом'),
            ('Участок', 'Участок'),
            ('Коммерческая недвижимость', 'Коммерческая недвижимость'),
        )
        OWN = (
            ('Собственность', 'Собственность'),
            ('Не оформлено', 'Не оформлено'),
        )
        widgets = {
            "type_property": forms.Select(
                choices=TYPE_PROPERTY,attrs={'class': 'form-control'}
            ),
            "own": forms.Select(
                choices=OWN,attrs={'class': 'form-control'}
            ),
            "city": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Например: г. Москва, ул. Ленина 21'}
            ),
            "areas": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Например: 60м²; 40 соток'}
            ),
            "floor": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Например: 7 / 11'}
            ),
            "price": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Например: 4 000 000.00 (Валюта - рубль)'}
            ),
            "number": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Например: +79407371717'}
            ),
        }
        labels = {
            'type_property': 'Ваш объект',
            'own': 'Собственность\ Не оформлено',
            'city': 'Город \ район',
            'areas': 'Площадь кв\м, сотки',
            'floor': 'Этаж\этажность',
            'price': 'Цена',
            'number': 'Номер телефона',
        }
