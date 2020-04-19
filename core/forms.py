from django import forms
from core.models import Deal,Category


class DealCreate(forms.ModelForm):
    # todo change it to datetime
    start_date = forms.DateField(
        input_formats=['%d/%m/%Y',],
        widget=forms.DateInput(),
    )
    end_date = forms.DateField(
        input_formats=['%d/%m/%Y',],
        widget=forms.DateInput(),
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Aucune Catégorie"
    )

    class Meta:
        model = Deal
        fields = ['title','link',
              'price','crossed_price','start_date', 'end_date','description','location','category','thumbnail']
