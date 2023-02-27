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
