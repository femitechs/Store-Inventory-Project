from tkinter.tix import Select
from turtle import textinput
from typing_extensions import Required

from django.db.models import fields
from .models import Inventories
from django import forms

class CreateInventoryForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'error'

    class Meta:
        model = Inventories
        fields = ('seq_number', 'equipment_name', 'serial_number', 'tag_number', 'status')
        widgets = {
            'seq_number':forms.TextInput(attrs={
                'class':'form-control in1',
                'placeholder':'Sequence number'
            }),

            'equipment_name':forms.TextInput(attrs={
                'class':'form-control in2',
                'placeholder':'Equipment name'
            }),

            'serial_number':forms.TextInput(attrs={
                'class':'form-control in2',
                'placeholder':'Serial number'
            }),

            'tag_number':forms.TextInput(attrs={
                'class':'form-control in2',
                'placeholder':'Tag number'
            }),

            'status':forms.Select(attrs={
                'class':'form-controls in2',
                'id':'dropdown'
            }),

        }


class UpdateInventoryForm(forms.ModelForm):

    class Meta:
        model = Inventories
        fields = ('seq_number', 'equipment_name', 'serial_number', 'tag_number', 'status')
        widgets = {
            'seq_number':forms.TextInput(attrs={
                'class':'form-control in1'
            }),

            'equipment_name':forms.TextInput(attrs={
                'class':'form-control in2'
            }),

            'serial_number':forms.TextInput(attrs={
                'class':'form-control in2'
            }),

            'tag_number':forms.TextInput(attrs={
                'class':'form-control in2'
            }),

            'status':forms.Select(attrs={
                'class':'form-controls in2',
                'id':'dropdown'
            }),

        }
