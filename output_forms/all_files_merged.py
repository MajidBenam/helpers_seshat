from .models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real, Gdp_total, Gdp_growth_rate, Shares_of_world_gdp, Gdp_per_capita, Rate_of_gdp_per_capita_growth, Wages, Annual_wages, Rate_of_return, Famine_event, Disease_event, Jinshi_degrees_awarded, Examination, Taiping_rebellion, Worker_wage
import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

commonlabels = {
    'year_from': 'Start Year',
    'year_to': 'End Year',
    'tag': 'Certainty',
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3', 'placeholder':'Ex: 1897, -24, +100'}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', 'placeholder':'Ex: 1897, -24, +100'}),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px', 'placeholder':'Add a meaningful description (optional)'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': ' mb-3', 'checked': True, }),
}

class PopulationForm(forms.ModelForm):
    class Meta:
        model = Population
        fields = commonfields.copy()
        fields.append('total_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_population'] = forms.NumberInputwidgets['total_population'] = forms.NumberInput
        
class Land_taxes_collectedForm(forms.ModelForm):
    class Meta:
        model = Land_taxes_collected
        fields = commonfields.copy()
        fields.append('land_taxes_collected')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['land_taxes_collected'] = forms.NumberInputwidgets['land_taxes_collected'] = forms.NumberInput
        
class Land_yieldForm(forms.ModelForm):
    class Meta:
        model = Land_yield
        fields = commonfields.copy()
        fields.append('land_yield')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['land_yield'] = forms.NumberInputwidgets['land_yield'] = forms.NumberInput
        
class Total_taxForm(forms.ModelForm):
    class Meta:
        model = Total_tax
        fields = commonfields.copy()
        fields.append('total_amount_of_taxes_collected')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_amount_of_taxes_collected'] = forms.NumberInputwidgets['total_amount_of_taxes_collected'] = forms.NumberInput
        
class Total_economic_outputForm(forms.ModelForm):
    class Meta:
        model = Total_economic_output
        fields = commonfields.copy()
        fields.append('total_economic_output')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_economic_output'] = forms.NumberInputwidgets['total_economic_output'] = forms.NumberInput
        
class Total_revenueForm(forms.ModelForm):
    class Meta:
        model = Total_revenue
        fields = commonfields.copy()
        fields.append('total_revenue')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_revenue'] = forms.NumberInputwidgets['total_revenue'] = forms.NumberInput
        
class Diding_taxesForm(forms.ModelForm):
    class Meta:
        model = Diding_taxes
        fields = commonfields.copy()
        fields.append('diding_taxes')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['diding_taxes'] = forms.NumberInputwidgets['diding_taxes'] = forms.NumberInput
        
class Salt_taxForm(forms.ModelForm):
    class Meta:
        model = Salt_tax
        fields = commonfields.copy()
        fields.append('salt_tax')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['salt_tax'] = forms.NumberInputwidgets['salt_tax'] = forms.NumberInput
        
class Tariff_and_transitForm(forms.ModelForm):
    class Meta:
        model = Tariff_and_transit
        fields = commonfields.copy()
        fields.append('tariff_and_transit')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['tariff_and_transit'] = forms.NumberInputwidgets['tariff_and_transit'] = forms.NumberInput
        
class Misc_incomesForm(forms.ModelForm):
    class Meta:
        model = Misc_incomes
        fields = commonfields.copy()
        fields.append('misc_incomes')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['misc_incomes'] = forms.NumberInputwidgets['misc_incomes'] = forms.NumberInput
        
class Total_expenditureForm(forms.ModelForm):
    class Meta:
        model = Total_expenditure
        fields = commonfields.copy()
        fields.append('total_expenditure')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_expenditure'] = forms.NumberInputwidgets['total_expenditure'] = forms.NumberInput
        
class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = commonfields.copy()
        fields.append('balance')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['balance'] = forms.NumberInputwidgets['balance'] = forms.NumberInput
        
class LijinForm(forms.ModelForm):
    class Meta:
        model = Lijin
        fields = commonfields.copy()
        fields.append('lijin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['lijin'] = forms.NumberInputwidgets['lijin'] = forms.NumberInput
        
class Maritime_customForm(forms.ModelForm):
    class Meta:
        model = Maritime_custom
        fields = commonfields.copy()
        fields.append('maritime_custom')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['maritime_custom'] = forms.NumberInputwidgets['maritime_custom'] = forms.NumberInput
        
class Other_incomesForm(forms.ModelForm):
    class Meta:
        model = Other_incomes
        fields = commonfields.copy()
        fields.append('other_incomes')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['other_incomes'] = forms.NumberInputwidgets['other_incomes'] = forms.NumberInput
        
class Revenue_officialForm(forms.ModelForm):
    class Meta:
        model = Revenue_official
        fields = commonfields.copy()
        fields.append('revenue_official')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['revenue_official'] = forms.NumberInputwidgets['revenue_official'] = forms.NumberInput
        
class Revenue_realForm(forms.ModelForm):
    class Meta:
        model = Revenue_real
        fields = commonfields.copy()
        fields.append('revenue_real')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['revenue_real'] = forms.NumberInputwidgets['revenue_real'] = forms.NumberInput
        
class Gdp_totalForm(forms.ModelForm):
    class Meta:
        model = Gdp_total
        fields = commonfields.copy()
        fields.append('gdp_total')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_total'] = forms.NumberInputwidgets['gdp_total'] = forms.NumberInput
        
class Gdp_growth_rateForm(forms.ModelForm):
    class Meta:
        model = Gdp_growth_rate
        fields = commonfields.copy()
        fields.append('gdp_growth_rate')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_growth_rate'] = forms.NumberInputwidgets['gdp_growth_rate'] = forms.NumberInput
        
class Shares_of_world_gdpForm(forms.ModelForm):
    class Meta:
        model = Shares_of_world_gdp
        fields = commonfields.copy()
        fields.append('shares_of_world_gdp')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['shares_of_world_gdp'] = forms.NumberInputwidgets['shares_of_world_gdp'] = forms.NumberInput
        
class Gdp_per_capitaForm(forms.ModelForm):
    class Meta:
        model = Gdp_per_capita
        fields = commonfields.copy()
        fields.append('gdp_per_capita')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_per_capita'] = forms.NumberInputwidgets['gdp_per_capita'] = forms.NumberInput
        
class Rate_of_gdp_per_capita_growthForm(forms.ModelForm):
    class Meta:
        model = Rate_of_gdp_per_capita_growth
        fields = commonfields.copy()
        fields.append('rate_of_gdp_per_capita_growth')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['rate_of_gdp_per_capita_growth'] = forms.NumberInputwidgets['rate_of_gdp_per_capita_growth'] = forms.NumberInput
        
class WagesForm(forms.ModelForm):
    class Meta:
        model = Wages
        fields = commonfields.copy()
        fields.append('wages')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['wages'] = forms.NumberInputwidgets['wages'] = forms.NumberInput
        
class Annual_wagesForm(forms.ModelForm):
    class Meta:
        model = Annual_wages
        fields = commonfields.copy()
        fields.append('annual_wages')
        fields.append('job_category')
        fields.append('job_description')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['annual_wages'] = forms.NumberInputwidgets['annual_wages'] = forms.NumberInput
        widgets['job_category'] = forms.Selectwidgets['job_category'] = forms.Select
        widgets['job_description'] = forms.Selectwidgets['job_description'] = forms.Select
        
class Rate_of_returnForm(forms.ModelForm):
    class Meta:
        model = Rate_of_return
        fields = commonfields.copy()
        fields.append('rate_of_return')
        fields.append('job_category')
        fields.append('job_description')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['rate_of_return'] = forms.NumberInputwidgets['rate_of_return'] = forms.NumberInput
        widgets['job_category'] = forms.Selectwidgets['job_category'] = forms.Select
        widgets['job_description'] = forms.Selectwidgets['job_description'] = forms.Select
        
class Famine_eventForm(forms.ModelForm):
    class Meta:
        model = Famine_event
        fields = commonfields.copy()
        fields.append('famine_event')
        fields.append('latitude')
        fields.append('longitude')
        fields.append('elevation')
        fields.append('sub_category')
        fields.append('magnitude')
        fields.append('duration')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['famine_event'] = forms.NumberInputwidgets['famine_event'] = forms.NumberInput
        widgets['latitude'] = forms.NumberInputwidgets['latitude'] = forms.NumberInput
        widgets['longitude'] = forms.NumberInputwidgets['longitude'] = forms.NumberInput
        widgets['elevation'] = forms.NumberInputwidgets['elevation'] = forms.NumberInput
        widgets['sub_category'] = forms.Selectwidgets['sub_category'] = forms.Select
        widgets['magnitude'] = forms.Selectwidgets['magnitude'] = forms.Select
        widgets['duration'] = forms.Selectwidgets['duration'] = forms.Select
        
class Disease_eventForm(forms.ModelForm):
    class Meta:
        model = Disease_event
        fields = commonfields.copy()
        fields.append('disease_event')
        fields.append('latitude')
        fields.append('longitude')
        fields.append('elevation')
        fields.append('sub_category')
        fields.append('magnitude')
        fields.append('duration')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['disease_event'] = forms.NumberInputwidgets['disease_event'] = forms.NumberInput
        widgets['latitude'] = forms.NumberInputwidgets['latitude'] = forms.NumberInput
        widgets['longitude'] = forms.NumberInputwidgets['longitude'] = forms.NumberInput
        widgets['elevation'] = forms.NumberInputwidgets['elevation'] = forms.NumberInput
        widgets['sub_category'] = forms.Selectwidgets['sub_category'] = forms.Select
        widgets['magnitude'] = forms.Selectwidgets['magnitude'] = forms.Select
        widgets['duration'] = forms.Selectwidgets['duration'] = forms.Select
        
class Jinshi_degrees_awardedForm(forms.ModelForm):
    class Meta:
        model = Jinshi_degrees_awarded
        fields = commonfields.copy()
        fields.append('jinshi_degrees_awarded')
        fields.append('emperor')
        fields.append('population_in_year_x')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['jinshi_degrees_awarded'] = forms.TextInputwidgets['jinshi_degrees_awarded'] = forms.TextInput
        widgets['emperor'] = forms.NumberInputwidgets['emperor'] = forms.NumberInput
        widgets['population_in_year_x'] = forms.NumberInputwidgets['population_in_year_x'] = forms.NumberInput
        
class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = commonfields.copy()
        fields.append('examination')
        fields.append('no_of_participants')
        fields.append('degrees_awarded')
        fields.append('passing_ratio')
        fields.append('place')
        fields.append('ratio_examiner_per_candidate')
        fields.append('no_of_examiners')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['examination'] = forms.TextInputwidgets['examination'] = forms.TextInput
        widgets['no_of_participants'] = forms.NumberInputwidgets['no_of_participants'] = forms.NumberInput
        widgets['degrees_awarded'] = forms.NumberInputwidgets['degrees_awarded'] = forms.NumberInput
        widgets['passing_ratio'] = forms.NumberInputwidgets['passing_ratio'] = forms.NumberInput
        widgets['place'] = forms.TextInputwidgets['place'] = forms.TextInput
        widgets['ratio_examiner_per_candidate'] = forms.NumberInputwidgets['ratio_examiner_per_candidate'] = forms.NumberInput
        widgets['no_of_examiners'] = forms.NumberInputwidgets['no_of_examiners'] = forms.NumberInput
        
class Taiping_rebellionForm(forms.ModelForm):
    class Meta:
        model = Taiping_rebellion
        fields = commonfields.copy()
        fields.append('taiping_rebellion')
        fields.append('rebel')
        fields.append('place')
        fields.append('ethnic_composition')
        fields.append('family_background')
        fields.append('role')
        fields.append('rank')
        fields.append('civil_examination')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['taiping_rebellion'] = forms.TextInputwidgets['taiping_rebellion'] = forms.TextInput
        widgets['rebel'] = forms.TextInputwidgets['rebel'] = forms.TextInput
        widgets['place'] = forms.TextInputwidgets['place'] = forms.TextInput
        widgets['ethnic_composition'] = forms.TextInputwidgets['ethnic_composition'] = forms.TextInput
        widgets['family_background'] = forms.TextInputwidgets['family_background'] = forms.TextInput
        widgets['role'] = forms.TextInputwidgets['role'] = forms.TextInput
        widgets['rank'] = forms.TextInputwidgets['rank'] = forms.TextInput
        widgets['civil_examination'] = forms.TextInputwidgets['civil_examination'] = forms.TextInput
        
class Worker_wageForm(forms.ModelForm):
    class Meta:
        model = Worker_wage
        fields = commonfields.copy()
        fields.append('worker_wage')
        fields.append('area')
        fields.append('unskilled_construction')
        fields.append('skilled_construction')
        fields.append('number_of_districts_with_available_data')
        fields.append('unskilled_arms_manufacturer')
        fields.append('population_in_millions_in_1787')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['worker_wage'] = forms.TextInputwidgets['worker_wage'] = forms.TextInput
        widgets['area'] = forms.TextInputwidgets['area'] = forms.TextInput
        widgets['unskilled_construction'] = forms.NumberInputwidgets['unskilled_construction'] = forms.NumberInput
        widgets['skilled_construction'] = forms.NumberInputwidgets['skilled_construction'] = forms.NumberInput
        widgets['number_of_districts_with_available_data'] = forms.NumberInputwidgets['number_of_districts_with_available_data'] = forms.NumberInput
        widgets['unskilled_arms_manufacturer'] = forms.NumberInputwidgets['unskilled_arms_manufacturer'] = forms.NumberInput
        widgets['population_in_millions_in_1787'] = forms.NumberInputwidgets['population_in_millions_in_1787'] = forms.NumberInput
        