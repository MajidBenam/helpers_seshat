from choices_lists import *
from long_descriptions_dic import *

# IMPORTS:
# 1: CHOICES as in choices_lists.py


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
        # 'vardesc': '(in 1,000 taels)',
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


{"agricultural_population": {"notes": "Notes for the Variable agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "agricultural_population", "var_exp": "No Explanations.", "units": "People", "min": 0, "max": None, "scale": 1000, "var_exp_source": None}}, "arable_land": {"notes": "Notes for the Variable arable_land are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "arable_land", "var_exp": "No Explanations.", "units": "mu?", "min": None, "max": None, "scale": 1000, "var_exp_source": None}}, "arable_land_per_farmer": {"notes": "Notes for the Variable arable_land_per_farmer are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "arable_land_per_farmer", "var_exp": "No Explanations.", "units": "mu?", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "gross_grain_shared_per_agricultural_population": {"notes": "Notes for the Variable gross_grain_shared_per_agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "gross_grain_shared_per_agricultural_population", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "net_grain_shared_per_agricultural_population": {"notes": "Notes for the Variable net_grain_shared_per_agricultural_population are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "net_grain_shared_per_agricultural_population", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "surplus": {"notes": "Notes for the Variable surplus are missing!", "main_desc": "No Explanations.", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "surplus", "var_exp": "No Explanations.", "units": "(catties per capita)", "min": None, "max": None, "scale": 1, "var_exp_source": None}}, "military_expense": {"notes": "Not sure about Section and Subsection.", "main_desc": "Main Descriptions for the Variable military_expense are missing!", "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak", "cols": 2, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["CharField", "TextInput"], "varname": "conflict", "var_exp": "The name of the conflict", "var_exp_source": None}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "expenditure", "var_exp": "The military expenses in millions silver taels.", "units": "millions silver taels", "min": None, "max": None, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}}, "silver_inflow": {"notes": "Needs suoervision on the units and scale.", "main_desc": "Silver inflow in Millions of silver taels??", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "silver_inflow", "var_exp": "Silver inflow in Millions of silver taels??", "units": "Millions of silver taels??", "min": None, "max": None, "scale": 1000000, "var_exp_source": None}}, "silver_stock": {"notes": "Needs suoervision on the units and scale.", "main_desc": "Silver stock in Millions of silver taels??", "main_desc_source": "", "cols": 1, "section": "Economy Variables", "subsection": "State Finances", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "silver_stock", "var_exp": "Silver stock in Millions of silver taels??", "units": "Millions of silver taels??", "min": None, "max": None, "scale": 1000000, "var_exp_source": None}}, "total_population": {"notes": "Note that the population values are scaled.", "main_desc": "Total population or simply population, of a given area is the total number of people in that area at a given time.", "main_desc_source": "", "cols": 1, "section": "Social Complexity Variables", "subsection": "Social Scale", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "total_population", "var_exp": "The total population of a country (or a polity).", "units": "People", "min": 0, "max": None, "scale": 1000, "var_exp_source": None}}, "gdp_per_capita": {"notes": "The exact year based on which the value of Dollar is taken into account is not clear.", "main_desc": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", "main_desc_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848", "cols": 1, "section": "Economy Variables", "subsection": "Productivity", "null_meaning": "The value is not available.", "col1": {
    "dtype": ["DecimalField", "NumberInput"], "varname": "gdp_per_capita", "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.", "units": "Dollars (in 2009?)", "min": None, "max": None, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848"}}, "drought_events": {"notes": "Notes for the Variable drought_events are missing!", "main_desc": "number of geographic sites indicating drought", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "drought_events", "var_exp": "number of geographic sites indicating drought", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "locust_events": {"notes": "Notes for the Variable locust_events are missing!", "main_desc": "number of geographic sites indicating locusts", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "locust_events", "var_exp": "number of geographic sites indicating locusts", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "socioeconomic_turmoil_events": {"notes": "Notes for the Variable socioeconomic_turmoil_events are missing!", "main_desc": "number of geographic sites indicating socioeconomic turmoil", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "socioeconomic_turmoil_events", "var_exp": "number of geographic sites indicating socioeconomic turmoil", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "crop_failure_events": {"notes": "Notes for the Variable crop_failure_events are missing!", "main_desc": "number of geographic sites indicating crop failure", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "crop_failure_events", "var_exp": "number of geographic sites indicating crop failure", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "famine_events": {"notes": "Notes for the Variable famine_events are missing!", "main_desc": "number of geographic sites indicating famine", "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt", "cols": 1, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["IntegerField", "NumberInput"], "varname": "famine_events", "var_exp": "number of geographic sites indicating famine", "units": "Numbers", "min": 0, "max": None, "scale": 1, "var_exp_source": None}}, "disease_outbreak": {"notes": "Notes for the Variable disease_outbreak are missing!", "main_desc": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.", "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak", "cols": 6, "section": "Well Being", "subsection": "Biological Well-Being", "null_meaning": "The value is not available.", "col1": {"dtype": ["DecimalField", "NumberInput"], "varname": "longitude", "var_exp": "The longitude (in degrees) of the place where the disease was spread.", "units": "Degrees", "min": -180, "max": 180, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col2": {"dtype": ["DecimalField", "NumberInput"], "varname": "latitude", "var_exp": "The latitude (in degrees) of the place where the disease was spread.", "units": "Degrees", "min": -180, "max": 180, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col3": {"dtype": ["DecimalField", "NumberInput"], "varname": "elevation", "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.", "units": "Meters", "min": 0, "max": 5000, "scale": 1, "decimal_places": 15, "max_digits": 20, "var_exp_source": None}, "col4": {"dtype": ["CharField", "Select"], "varname": "sub_category", "var_exp": "The category of the disease.", "var_exp_source": None, "choices": ["Peculiar Epidemics", "Pestilence", "Miasm", "Pox", "Uncertain Pestilence", "Dysentery", "Malaria", "Influenza", "Cholera", "Diptheria", "Plague"]}, "col5": {"dtype": ["CharField", "Select"], "varname": "magnitude", "var_exp": "How heavy the disease was.", "var_exp_source": None, "choices": ["Uncertain", "Light", "Heavy", "No description", "Heavy- Multiple Times", "No Happening", "Moderate"]}, "col6": {"dtype": ["CharField", "Select"], "varname": "duration", "var_exp": "How long the disease lasted.", "var_exp_source": None, "choices": ["No description", "Over 90 Days", "Uncertain", "30-60 Days", "1-10 Days", "60-90 Days"]}}}
