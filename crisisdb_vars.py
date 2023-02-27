from choices_lists import *
from long_descriptions_dic import *

##### IMPORTS:
# 1: CHOICES as in choices_lists.py


DISEASE_OUTBREAK_CHOICES = (
('Peculiar Epidemics', 'Peculiar Epidemics'),
('Pestilence', 'Pestilence'),
('Miasm', 'Miasm'),
('Pox', 'Pox'),
('Uncertain Pestilence', 'Uncertain Pestilence'),
('Dysentery', 'Dysentery'),
('Malaria', 'Malaria'),
('Influenza', 'Influenza'),
('Cholera', 'Cholera'),
('Diptheria', 'Diptheria'),
('Plague', 'Plague'),
)

# vars

# to_Form field converter
MYINT = ['IntegerField', 'NumberInput']
MYDEC = ['DecimalField', 'NumberInput']
MYTXT = ['CharField', 'TextInput']
# for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
MYTXT_CH = ['CharField', 'Select']


# the dictionary containing all the needed info for our code generators
vars_dic = {
    'population': {
        'section': 'xyz',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'total_population',
            },
        },
    'land_taxes_collected': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'land_taxes_collected',
            },        
        },
    'land_yield': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'land_yield',
            },
        },
    'total_tax': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'total_amount_of_taxes_collected',
            },
        },
    'total_economic_output': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'total_economic_output',
            },
        },
    'total_revenue': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'total_revenue',
            'vardesc': 'Total Revenue (in 1,000 taels)',
            },
        },
    'diding_taxes': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'diding_taxes',
            'vardesc': 'Diding Taxes (in 1,000 taels)',
            },
        },
    'salt_tax': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'salt_tax',
            'vardesc': 'Salt Tax (in 1,000 taels)',
            },
        },
    'tariff_and_transit': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'tariff_and_transit',
            'vardesc': 'Tariff and transit (in 1,000 taels)',
            },
        },
    'misc_incomes': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'misc_incomes',
            'vardesc': 'Miscellaneous incomes (in 1,000 taels)',
            'importance': 'HIGH',
            },
        },
    'total_expenditure': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'total_expenditure',
            'vardesc': 'Total Expenditure (in 1,000 taels)',
            },
        },
    'balance': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'balance',
            'vardesc': 'Balance (in 1,000 taels)',
            },
        },
    'lijin': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'lijin',
            'vardesc': '(in 1,000 taels)',
            },
        },
    'maritime_custom': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'maritime_custom',
            'vardesc': '(in 1,000 taels)',
            },
        },
    'other_incomes': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'other_incomes',
            'vardesc': '(in 1,000 taels)',
            },
        },
    'revenue_official': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'revenue_official',
            'vardesc': '(in 1,000 taels)',
            },
        },
    'revenue_real': {
        'section': 'Fiscal Helath',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'revenue_real',
            'vardesc': '(in 1,000 taels)',
            },
        },
    'gdp_total': {
        'section': 'Aggregate Wealth',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'gdp_total',
            'vardesc': 'Total GDP (in Million Dollars)',
            },
        },
    'gdp_growth_rate': {
        'section': 'Aggregate Wealth',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYDEC,
            'varname': 'gdp_growth_rate',
            },
        },
    'shares_of_world_gdp': {
        'section': 'Aggregate Wealth',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYDEC,
            'varname': 'shares_of_world_gdp',
            'vardesc': 'Percentage',
            },
        },
    'gdp_per_capita': {
        'section': 'Aggregate Wealth',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'gdp_per_capita',
            'vardesc': 'GDP (per capita 1990 $',
            },
        },
    'rate_of_gdp_per_capita_growth': {
        'section': 'Aggregate Wealth',
        'maindesc': 'nothing',
        'cols': 1,
        'col1': {
            'dtype': MYINT,
            'varname': 'rate_of_gdp_per_capita_growth',
            },
        },
    'wages': {
        'section': 'Aggregate Wealth',
        'maindesc': long_discriptions['wages'],
        'cols': 1,
        'col1': {
            'dtype': MYDEC,
            'varname': 'wages',
            'vardesc': """These are real wages, i.e. "Daily building labourers' wage divided by a daily subsistence basket" """,
            },
        },
    'annual_wages': {
        'section': 'Institutional variables',
        'maindesc': 'in silver liang by level of education',
        'cols': 3,
        'col1': {
            'dtype': MYINT,
            'varname': 'annual_wages',
            'vardesc': '(in 1,000 taels)',
        },
        'col2': {
            'dtype': MYTXT_CH,
            'varname': 'job_category',
            'choices': job_category_annual_wages_choices,
        },
        'col3': {
            'dtype': MYTXT_CH,
            'varname': 'job_description',
            'choices': job_description_annual_wages_choices,
        },

    },
    'rate_of_return': {
         #'vardesc': '(in 1,000 taels)',
        'section': 'Wages',
        'maindesc': 'by level of education corrected for foregone wages and life expectancy, and the probability of successful examination',
        'cols': 3,
        'col1': {
            'dtype': MYDEC,
            'varname': 'rate_of_return',
            'importance': 'HIGH',
        },
        'col2': {
            'dtype': MYTXT_CH,
            'varname': 'job_category',
            'choices': job_category_rate_of_return_choices,
            'importance': 'LOW',

        },
        'col3': {
            'dtype': MYTXT_CH,
            'varname': 'job_description',
            'choices': job_description_rate_of_return_choices,
            'importance': 'LOW',
        },

    },
    'famine_event': {
        'section': 'Famines Section',
        'subsection': 'Famines subsection',
        'maindesc': 'nothing',
        'cols': 7,
        'col1': {
            'dtype': MYDEC,
            'varname': 'famine_event',
        },
        'col2': {
            'dtype': MYDEC,
            'varname': 'latitude',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'longitude',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'elevation',
        },
        'col5': {
            'dtype': MYTXT_CH,
            'varname': 'sub_category',
            'choices': famine_sub_category_choices,
        },
        'col6': {
            'dtype': MYTXT_CH,
            'varname': 'magnitude',
            'choices': famine_magnitude_choices,
        },
        'col7': {
            'dtype': MYTXT_CH,
            'varname': 'duration',
            'choices': famine_duration_choices,
        },
    
    },
    'disease_event': {
        'section': 'Diseases Section',
        'maindesc': 'nothing',
        'cols': 7,
        'col1': {
            'dtype': MYDEC,
            'varname': 'disease_event',
        },
        'col2': {
            'dtype': MYDEC,
            'varname': 'latitude',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'longitude',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'elevation',
        },
        'col5': {
            'dtype': MYTXT_CH,
            'varname': 'sub_category',
            'choices': disease_sub_category_choices,
        },
        'col6': {
            'dtype': MYTXT_CH,
            'varname': 'magnitude',
            'choices': disease_magnitude_choices,
        },
        'col7': {
            'dtype': MYTXT_CH,
            'varname': 'duration',
            'choices': disease_duration_choices,
        },
    
    },
    'jinshi_degrees_awarded': {
        'section': 'xyz',
        'maindesc': 'nothing',
        'cols': 3,
        'col1': {
            'dtype': MYTXT,
            'varname': 'jinshi_degrees_awarded',
        },
        'col2': {
            'dtype': MYINT,
            'varname': 'emperor',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'population_in_year_x',
        },
    
    },
    'examination': {
        'section': 'xyz',
        'maindesc': 'nothing',
        'cols': 7,
        'col1': {
            'dtype': MYTXT,
            'varname': 'examination',
        },
        'col2': {
            'dtype': MYINT,
            'varname': 'no_of_participants',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'degrees_awarded',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'passing_ratio',
        },
        'col5': {
            'dtype': MYTXT,
            'varname': 'place',
        },
        'col6': {
            'dtype': MYDEC,
            'varname': 'ratio_examiner_per_candidate',
        },
        'col7': {
            'dtype': MYINT,
            'varname': 'no_of_examiners',
        },
    
    },
    'taiping_rebellion': {
        'section': 'xyz',
        'maindesc': 'nothing',
        'cols': 8,
        'col1': {
            'dtype': MYTXT,
            'varname': 'taiping_rebellion',
        },
        'col2': {
            'dtype': MYTXT,
            'varname': 'rebel',
        },
        'col3': {
            'dtype': MYTXT,
            'varname': 'place',
        },
        'col4': {
            'dtype': MYTXT,
            'varname': 'ethnic_composition',
        },
        'col5': {
            'dtype': MYTXT,
            'varname': 'family_background',
        },
        'col6': {
            'dtype': MYTXT,
            'varname': 'role',
        },
        'col7': {
            'dtype': MYTXT,
            'varname': 'rank',
        },
        'col8': {
            'dtype': MYTXT,
            'varname': 'civil_examination',
        },
    
    },
    'worker_wage': {
        'section': 'xyz',
        'maindesc': 'nothing',
        'cols': 7,
        'col1': {
            'dtype': MYTXT,
            'varname': 'worker_wage',
        },
        'col2': {
            'dtype': MYTXT,
            'varname': 'area',
        },
        'col3': {
            'dtype': MYDEC,
            'varname': 'unskilled_construction',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'skilled_construction',
        },
        'col5': {
            'dtype': MYINT,
            'varname': 'number_of_districts_with_available_data',
        },
        'col6': {
            'dtype': MYDEC,
            'varname': 'unskilled_arms_manufacturer',
        },
        'col7': {
            'dtype': MYDEC,
            'varname': 'population_in_millions_in_1787',
        },
    },
}
