# choices

job_category_rate_of_return_choices = [("jobs requiring jinshi or juren examinations","jobs requiring jinshi or juren examinations"),
("jobs requiring shengyuan examination", "jobs requiring shengyuan examination"),
("jobs with less than shengyuan education", "jobs with less than shengyuan education"),]

job_category_annual_wages_choices = ("jobs requiring jinshi or juren examinations",
"jobs requiring shengyuan examination",
"jobs with less than shengyuan education",
"jobs requiring no education")

job_description_rate_of_return_choices = ("official service in central government or local government",
"secretarial assistants to high provincial officials",
"lecturer in large shuyuan",
"secretarial assistants to prefects and counties",
"scholar doctor in local community",
"service as gentry functions",
"teacher in local school",
"other services",
"skilled labour in silk-reel industry",
"teacher in local primary school")

job_description_annual_wages_choices = ("official service in central government or local government",
"secretarial assistants to high provincial officials",
"lecturer in large shuyuan",
"secretarial assistants to prefects and counties",
"scholar doctor in local community",
"service as gentry functions",
"teacher in local school",
"other services",
"skilled labour in silk-reel industry",
"teacher in local primary school",
"general unskilled labour in big city",
"general unskilled labour in small town or village",)


sub_category_famine_event_choices = ["Famine", "Human-Eating"]

magnitude_famine_event_choices = ["Uncertain", "Heavy", "Light", "Heavy- Multiple Times", 
                            "No Happening", "No description","Nonspecified",
                           ]

duration_famine_event_choices = ["1 to 10 Days", # or 1 to 20 days???
"20 to 30 Days",
"30 to 60 Days",
"60 to 90 Days",
"Over 90 Days",
"No description",
"Uncertain",
]

sub_category_disease_event_choices = ['Peculiar Epidemics', 'Pestilence', 'Miasm', 'Pox',
       'Uncertain Pestilence', 'Dysentery', 'Malaria', 'Cholera',
       'Influenza', 'Diptheria', 'Plague']

magnitude_disease_event_choices = ['No description', 'Over 90 Days', 'Uncertain', 
        '30-60 Days', '1-10 Days', '60-90 Days', 'Influenza']

duration_disease_event_choices = ["1 to 10 Days", # or 1 to 20 days???
"20 to 30 Days",
"30 to 60 Days",
"60 to 90 Days",
"Over 90 Days",
"No description",
"Uncertain",
]


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
        'dtype': MYINT,
        'varname': 'total_population',
        },
    'land_taxes_collected': {
        'dtype': MYINT,
        'varname': 'land_taxes_collected',
        'section': 'Fiscal Helath',
        },
    'land_yield': {
        'dtype': MYINT,
        'varname': 'land_yield',
        'section': 'Fiscal Helath',
        },
    'total_tax': {
        'dtype': MYINT,
        'varname': 'total_amount_of_taxes_collected',
        'section': 'Fiscal Helath',
        },
    'total_economic_output': {
        'dtype': MYINT,
        'varname': 'total_economic_output',
        'section': 'Fiscal Helath',
        },
    'total_revenue': {
        'dtype': MYINT,
        'varname': 'total_revenue',
        'vardesc': 'Total Revenue (in 1,000 taels)',
        },
    'diding_taxes': {
        'dtype': MYINT,
        'varname': 'total_revenue',
        'vardesc': 'Diding Taxes (in 1,000 taels)',
        'section': 'Fiscal Helath',

        },
    'salt_tax': {
        'dtype': MYINT,
        'varname': 'salt_tax',
        'vardesc': 'Salt Tax (in 1,000 taels)',
        'section': 'Fiscal Helath',

        },
    'tariff_and_transit': {
        'dtype': MYINT,
        'varname': 'tariff_and_transit',
        'vardesc': 'Tariff and transit (in 1,000 taels)',
        'section': 'Fiscal Helath',

        },
    'misc_incomes': {
        'dtype': MYINT,
        'varname': 'misc_incomes',
        'vardesc': 'Misc. incomes (in 1,000 taels)',
        'section': 'Fiscal Helath',

        },
    'total_expenditure': {
        'dtype': MYINT,
        'varname': 'total_expenditure',
        'vardesc': 'Total Expenditure (in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'balance': {
        'dtype': MYINT,
        'varname': 'balance',
        'vardesc': 'Balance (in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'lijin': {
        'dtype': MYINT,
        'varname': 'lijin',
        'vardesc': '(in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'maritime_custom': {
        'dtype': MYINT,
        'varname': 'maritime_custom',
        'vardesc': '(in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'other_incomes': {
        'dtype': MYINT,
        'varname': 'other_incomes',
        'vardesc': '(in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'revenue_official': {
        'dtype': MYINT,
        'varname': 'revenue_official',
        'vardesc': '(in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'revenue_real': {
        'dtype': MYINT,
        'varname': 'revenue_real',
        'vardesc': '(in 1,000 taels)',
        'section': 'Fiscal Helath',
        },
    'GDP_total': {
        'dtype': MYINT,
        'varname': 'GDP_total',
        'vardesc': 'Total GDP (in Million Dollars)',
        'section': 'Aggregate Wealth',
    },
    'GDP_growth_rate': {
        'dtype': MYDEC,
        'varname': 'GDP_growth_rate',
        'vardesc': '',
        'section': 'Aggregate Wealth',
    },
    'shares_of_world_GDP': {
        'dtype': MYDEC,
        'varname': 'shares_of_world_GDP',
        'vardesc': 'Percentage',
        'section': 'Aggregate Wealth',
    },
    'GDP_per_capita': {
        'dtype': MYINT,
        'varname': 'GDP_per_capita',
        'vardesc': 'GDP (per capita 1990 $)',
        'section': 'Aggregate Wealth',
    },
    'rate_of_GDP_per_capita_growth': {
        'dtype': MYDEC,
        'varname': 'rate_of_GDP_per_capita_growth',
        'vardesc': '',
        'section': 'Aggregate Wealth',
    },
    'wages': {
        'dtype': MYDEC,
        'varname': 'wages',
        'vardesc': """These are real wages, i.e. "Daily building labourers' wage divided by a daily subsistence basket" for China compiled by Pim de Zwart, Bas van Leeuwen and Jieli van Leeuwen-Li. They comment: "The wage and price series shown in this chapter are taken from three sources: (A) a variety of studies on historical real wages that appeared in academic journals and books; (B) the British Colonial Blue Books (circa 1840-1912); and (C) the October Enquiries of the International Labour Organisation (1924-2008). These data were then converted into subsistence ratios, which indicate how many times the daily wage of a male unskilled construction labourer can buy the daily subsistence basket. This methodology has the advantage of providing an absolute yardstick to compare welfare across countries and time periods and, hence, is conceptually close (but not identical) to purchasing power parities. Finally, in order to fill gaps in the data, interpolations were made (D) on the basis of real wages indices from the (older) literature.""",
        'section': 'Aggregate Wealth',
    },
    'annual_wages': {
        'cols': 3,
        'col1': {
            'dtype': MYINT,
            'varname': 'annual_wages',
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
        #'vardesc': '(in 1,000 taels)',
        'section': 'Institutional variables',
        'notes': 'in silver liang by level of education'
    },
    'rate_of_return': {
        'cols': 3,
        'col1': {
            'dtype': MYINT,
            'varname': 'rate_of_return',
        },
        'col2': {
            'dtype': MYTXT_CH,
            'varname': 'job_category',
            'choices': job_category_rate_of_return_choices,
        },
        'col3': {
            'dtype': MYTXT_CH,
            'varname': 'job_description',
            'choices': job_description_rate_of_return_choices,
        },
        #'vardesc': '(in 1,000 taels)',
        'section': 'Wages',
        'notes': 'by level of education corrected for foregone wages and life expectancy, and the probability of successful examination'
    },
    'famine_event': {
        'col1': {
            'dtype': MYDEC,
            'varname': 'longitude',
        },
        'col2': {
            'dtype': MYDEC,
            'varname': 'latitude',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'famine_event',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'elevation',
        },
        'col5': {
            'dtype': MYTXT_CH,
            'varname': 'sub_category',
            'choices': sub_category_famine_event_choices,
        },
        'col6': {
            'dtype': MYTXT_CH,
            'varname': 'magnitude',
            'choices': magnitude_famine_event_choices,
        },
        'col7': {
            'dtype': MYTXT_CH,
            'varname': 'duration',
            'choices': duration_famine_event_choices,
        },
    
    },
    'disease_event': {
        'col1': {
            'dtype': MYDEC,
            'varname': 'longitude',
        },
        'col2': {
            'dtype': MYDEC,
            'varname': 'latitude',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'disease_event',
        },
        'col4': {
            'dtype': MYDEC,
            'varname': 'elevation',
        },
        'col5': {
            'dtype': MYTXT_CH,
            'varname': 'sub_category',
            'choices': sub_category_disease_event_choices,
        },
        'col6': {
            'dtype': MYTXT_CH,
            'varname': 'magnitude',
            'choices': magnitude_disease_event_choices,
        },
        'col7': {
            'dtype': MYTXT_CH,
            'varname': 'duration',
            'choices': duration_disease_event_choices,
        },
    
    },
    'jinshi_degrees_awarded': {
        'col1': {
            'dtype': MYTXT,
            'varname': 'emperor',
        },
        'col2': {
            'dtype': MYINT,
            'varname': 'jinshi_degrees_awarded',
        },
        'col3': {
            'dtype': MYINT,
            'varname': 'population_in_year_x',
        },
    
    },
    'examination': {
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

majid = 56