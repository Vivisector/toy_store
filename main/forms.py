from django import forms
from .models import Buyer

class UserRegister(forms.ModelForm):
    repeat_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Повторите пароль",
    )

    class Meta:
        model = Buyer
        fields = ['username', 'password', 'age']
        widgets = {
            'password': forms.PasswordInput,
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields.move_to_end('repeat_password')  # Перемещаем repeat_password
    #     self.fields.move_to_end('age')
        # Валидация возраста
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError("Возраст должен быть не менее 18 лет")
        if age >= 100:
            raise forms.ValidationError("Возраст должен быть меньше 100 лет")
        return age

    # Общая валидация формы
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data
