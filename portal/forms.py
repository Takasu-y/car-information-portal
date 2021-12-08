from django import forms
import datetime

from . import maker_logo

# maker select
choiceMaker = [("", "select maker")]
for i, maker in enumerate(maker_logo.makers):
    choiceMaker.append((i, maker))


#model select
choiceModel = [("", "select Model"), ("", "Any")]

class SearchFrom(forms.Form):
    maker = forms.ChoiceField(
        choices=choiceMaker,
        required=True,
        widget=forms.widgets.Select
    )
    model = forms.ChoiceField(choices=choiceModel)
    min_year = forms.IntegerField(initial=datetime.datetime.now().year, min_value=1886, max_value=datetime.datetime.now().year)
    max_year = forms.IntegerField(initial=datetime.datetime.now().year, min_value=1886, max_value=datetime.datetime.now().year)