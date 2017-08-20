from django.forms import ModelForm, widgets, HiddenInput
from main.models import Lecturer
class Lecturerform(ModelForm):
    user = HiddenInput()        
    class Meta:
        model = Lecturer
        fields = '__all__'
        widgets = {
            'user':HiddenInput()

            }
    
