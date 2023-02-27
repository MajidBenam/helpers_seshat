
class Population(SeshatCommon):
    name = models.CharField(max_length=100, default="Population")
    total_population = models.PositiveBigIntegerField(blank=True, null=True)

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
        
        
class Flood(SeshatCommon):
    name = models.CharField(max_length=100, default="Flood")
    total_population = models.DecimalField(blank=True, null=True)

    class Meta:
        verbose_name = 'Flood'
        verbose_name_plural = 'Floods'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('Flood-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        