from django import forms
import datetime

from . import maker_logo

# maker select
choiceMaker = [("select maker", "select maker")]
for maker in maker_logo.makers:
    choiceMaker.append((maker, maker))


#model select
choiceModel = [("select Model", "select Model"), ("", "Any")]

#minYear
minYear = 1886

#current Year
currentYear = datetime.datetime.now().year

class SearchFrom(forms.Form):
    maker = forms.ChoiceField(
        choices=choiceMaker,
        required=True,
        widget=forms.widgets.Select
    )
    model = forms.ChoiceField(initial=choiceModel[0], choices=choiceModel)
    minYear = forms.IntegerField(initial=currentYear, min_value=minYear, max_value=currentYear)
    maxYear = forms.IntegerField(initial=currentYear, min_value=minYear, max_value=currentYear)