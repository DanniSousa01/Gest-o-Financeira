from django.forms import ModelForm, TextInput
from .models import Usuario, Despesas


class UsuarioForm(ModelForm):
    class Meta:    
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class':'form-control'}),
            'cpf': TextInput(attrs={'class':'form-control'}),
            'data_nasc': TextInput(attrs={'class':'form-control'}),
            'tel': TextInput(attrs={'class':'form-control'})
        }

class DespesasForm(ModelForm):
    class Meta:    
        model = Despesas
        fields = '__all__'
        widgets = {
            'nome_prod': TextInput(attrs={'class':'form-control'}),
            'quant_prod': TextInput(attrs={'class':'form-control'}),
            'valor': TextInput(attrs={'class':'form-control'}),
            'data_compra': TextInput(attrs={'class':'form-control'})
        }