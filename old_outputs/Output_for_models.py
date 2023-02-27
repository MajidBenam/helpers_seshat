
class Population(SeshatCommon):
    name = models.CharField(max_length=100, default="Population")
    total_population = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Population'
        verbose_name_plural = 'Populations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('population-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Land_taxes_collected(SeshatCommon):
    name = models.CharField(max_length=100, default="Land_taxes_collected")
    land_taxes_collected = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Land_taxes_collected'
        verbose_name_plural = 'Land_taxes_collecteds'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('land_taxes_collected-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Land_yield(SeshatCommon):
    name = models.CharField(max_length=100, default="Land_yield")
    land_yield = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Land_yield'
        verbose_name_plural = 'Land_yields'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('land_yield-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_tax(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_tax")
    total_amount_of_taxes_collected = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Total_tax'
        verbose_name_plural = 'Total_taxes'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_tax-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_economic_output(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_economic_output")
    total_economic_output = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Total_economic_output'
        verbose_name_plural = 'Total_economic_outputs'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_economic_output-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_revenue(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_revenue")
    total_revenue = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Total_revenue'
        verbose_name_plural = 'Total_revenues'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_revenue-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Diding_taxes(SeshatCommon):
    name = models.CharField(max_length=100, default="Diding_taxes")
    total_revenue = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Diding_taxes'
        verbose_name_plural = 'Diding_taxes'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('diding_taxes-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Salt_tax(SeshatCommon):
    name = models.CharField(max_length=100, default="Salt_tax")
    salt_tax = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Salt_tax'
        verbose_name_plural = 'Salt_taxes'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('salt_tax-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Tariff_and_transit(SeshatCommon):
    name = models.CharField(max_length=100, default="Tariff_and_transit")
    tariff_and_transit = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Tariff_and_transit'
        verbose_name_plural = 'Tariff_and_transits'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('tariff_and_transit-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Misc_incomes(SeshatCommon):
    name = models.CharField(max_length=100, default="Misc_incomes")
    misc_incomes = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Misc_incomes'
        verbose_name_plural = 'Misc_incomes'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('misc_incomes-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Total_expenditure(SeshatCommon):
    name = models.CharField(max_length=100, default="Total_expenditure")
    total_expenditure = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Total_expenditure'
        verbose_name_plural = 'Total_expenditures'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('total_expenditure-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Balance(SeshatCommon):
    name = models.CharField(max_length=100, default="Balance")
    balance = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('balance-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Lijin(SeshatCommon):
    name = models.CharField(max_length=100, default="Lijin")
    lijin = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Lijin'
        verbose_name_plural = 'Lijins'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('lijin-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Maritime_custom(SeshatCommon):
    name = models.CharField(max_length=100, default="Maritime_custom")
    maritime_custom = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Maritime_custom'
        verbose_name_plural = 'Maritime_customs'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('maritime_custom-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Other_incomes(SeshatCommon):
    name = models.CharField(max_length=100, default="Other_incomes")
    other_incomes = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Other_incomes'
        verbose_name_plural = 'Other_incomes'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('other_incomes-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Revenue_official(SeshatCommon):
    name = models.CharField(max_length=100, default="Revenue_official")
    revenue_official = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Revenue_official'
        verbose_name_plural = 'Revenue_officials'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('revenue_official-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Revenue_real(SeshatCommon):
    name = models.CharField(max_length=100, default="Revenue_real")
    revenue_real = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Revenue_real'
        verbose_name_plural = 'Revenue_reals'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('revenue_real-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gdp_total(SeshatCommon):
    name = models.CharField(max_length=100, default="Gdp_total")
    GDP_total = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Gdp_total'
        verbose_name_plural = 'Gdp_totals'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('GDP_total-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gdp_growth_rate(SeshatCommon):
    name = models.CharField(max_length=100, default="Gdp_growth_rate")
    GDP_growth_rate = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    
    class Meta:
        verbose_name = 'Gdp_growth_rate'
        verbose_name_plural = 'Gdp_growth_rates'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('GDP_growth_rate-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Shares_of_world_gdp(SeshatCommon):
    name = models.CharField(max_length=100, default="Shares_of_world_gdp")
    shares_of_world_GDP = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    
    class Meta:
        verbose_name = 'Shares_of_world_gdp'
        verbose_name_plural = 'Shares_of_world_gdps'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('shares_of_world_GDP-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Gdp_per_capita(SeshatCommon):
    name = models.CharField(max_length=100, default="Gdp_per_capita")
    GDP_per_capita = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Gdp_per_capita'
        verbose_name_plural = 'Gdp_per_capitas'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('GDP_per_capita-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Rate_of_gdp_per_capita_growth(SeshatCommon):
    name = models.CharField(max_length=100, default="Rate_of_gdp_per_capita_growth")
    rate_of_GDP_per_capita_growth = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    
    class Meta:
        verbose_name = 'Rate_of_gdp_per_capita_growth'
        verbose_name_plural = 'Rate_of_gdp_per_capita_growths'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('rate_of_GDP_per_capita_growth-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Wages(SeshatCommon):
    name = models.CharField(max_length=100, default="Wages")
    wages = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    
    class Meta:
        verbose_name = 'Wages'
        verbose_name_plural = 'Wages'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('wages-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Annual_wages(SeshatCommon):
    name = models.CharField(max_length=100, default="Annual_wages")
    annual_wages = models.IntegerField(blank=True, null=True)
    job_category = models.CharField(max_length=500, choices=job_category_annual_wages_choices)
    job_description = models.CharField(max_length=500, choices=job_description_annual_wages_choices)

    
    class Meta:
        verbose_name = 'Annual_wages'
        verbose_name_plural = 'Annual_wages'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('annual_wages-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Rate_of_return(SeshatCommon):
    name = models.CharField(max_length=100, default="Rate_of_return")
    rate_of_return = models.IntegerField(blank=True, null=True)
    job_category = models.CharField(max_length=500, choices=job_category_rate_of_return_choices)
    job_description = models.CharField(max_length=500, choices=job_description_rate_of_return_choices)

    
    class Meta:
        verbose_name = 'Rate_of_return'
        verbose_name_plural = 'Rate_of_returns'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('rate_of_return-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Famine_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Famine_event")
    longitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    famine_event = models.IntegerField(blank=True, null=True)
    elevation = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    sub_category = models.CharField(max_length=500, choices=sub_category_famine_event_choices)
    magnitude = models.CharField(max_length=500, choices=magnitude_famine_event_choices)
    duration = models.CharField(max_length=500, choices=duration_famine_event_choices)

    
    class Meta:
        verbose_name = 'Famine_event'
        verbose_name_plural = 'Famine_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('famine_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Disease_event(SeshatCommon):
    name = models.CharField(max_length=100, default="Disease_event")
    longitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    disease_event = models.IntegerField(blank=True, null=True)
    elevation = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    sub_category = models.CharField(max_length=500, choices=sub_category_disease_event_choices)
    magnitude = models.CharField(max_length=500, choices=magnitude_disease_event_choices)
    duration = models.CharField(max_length=500, choices=duration_disease_event_choices)

    
    class Meta:
        verbose_name = 'Disease_event'
        verbose_name_plural = 'Disease_events'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('disease_event-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Jinshi_degrees_awarded(SeshatCommon):
    name = models.CharField(max_length=100, default="Jinshi_degrees_awarded")
    emperor = models.CharField(max_length=500,)
    jinshi_degrees_awarded = models.IntegerField(blank=True, null=True)
    population_in_year_x = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Jinshi_degrees_awarded'
        verbose_name_plural = 'Jinshi_degrees_awardeds'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('jinshi_degrees_awarded-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Examination(SeshatCommon):
    name = models.CharField(max_length=100, default="Examination")
    examination = models.CharField(max_length=500,)
    no_of_participants = models.IntegerField(blank=True, null=True)
    degrees_awarded = models.IntegerField(blank=True, null=True)
    passing_ratio = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    place = models.CharField(max_length=500,)
    ratio_examiner_per_candidate = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    no_of_examiners = models.IntegerField(blank=True, null=True)

    
    class Meta:
        verbose_name = 'Examination'
        verbose_name_plural = 'Examinations'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('examination-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Taiping_rebellion(SeshatCommon):
    name = models.CharField(max_length=100, default="Taiping_rebellion")
    taiping_rebellion = models.CharField(max_length=500,)
    rebel = models.CharField(max_length=500,)
    place = models.CharField(max_length=500,)
    ethnic_composition = models.CharField(max_length=500,)
    family_background = models.CharField(max_length=500,)
    role = models.CharField(max_length=500,)
    rank = models.CharField(max_length=500,)
    civil_examination = models.CharField(max_length=500,)

    
    class Meta:
        verbose_name = 'Taiping_rebellion'
        verbose_name_plural = 'Taiping_rebellions'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('taiping_rebellion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        
class Worker_wage(SeshatCommon):
    name = models.CharField(max_length=100, default="Worker_wage")
    worker_wage = models.CharField(max_length=500,)
    area = models.CharField(max_length=500,)
    unskilled_construction = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    skilled_construction = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    number_of_districts_with_available_data = models.IntegerField(blank=True, null=True)
    unskilled_arms_manufacturer = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)
    population_in_millions_in_1787 = models.DecimalField(max_digits= 25, decimal_places = 10, blank=True, null=True)

    
    class Meta:
        verbose_name = 'Worker_wage'
        verbose_name_plural = 'Worker_wages'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('worker_wage-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        