from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    ## VALIDAÇÕES PERSONALIZADAS NÃO FUNCIONAM COM O MODEL FORM ##  

    # def clean_value(self):
    #     value = self.cleaned_data.get('value')
    #     if value < 20000:
    #         self.add_error('value', 'O valor deve ser maior que R$20.000.')
    #     return value

    # def clean_factory_year(self):
    #     factory_year = self.cleaned_data.get('factory_year')
    #     if factory_year < 1999:
    #         self.add_error('factory_year', 'Não é possivél cadastrar carros fabricados antes de 1999.')
    #     return factory_year