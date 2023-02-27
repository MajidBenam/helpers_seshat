################ Beginning of Serializers Imports (TODO: Make them automatic too)

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.crisisdb.models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real, Gdp_total, Gdp_growth_rate, Shares_of_world_gdp, Gdp_per_capita, Rate_of_gdp_per_capita_growth, Wages, Annual_wages, Rate_of_return, Famine_event, Disease_event, Jinshi_degrees_awarded, Examination, Taiping_rebellion, Worker_wage

from ..core.models import Polity, Reference, Section, Subsection, Variablehierarchy

################ End of Serializers Imports
