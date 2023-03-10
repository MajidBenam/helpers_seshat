
from .models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real, Gdp_total, Gdp_growth_rate, Shares_of_world_gdp, Gdp_per_capita, Rate_of_gdp_per_capita_growth, Wages, Annual_wages, Rate_of_return, Famine_event, Disease_event, Jinshi_degrees_awarded, Examination, Taiping_rebellion, Worker_wage
from .forms import PopulationForm, Land_taxes_collectedForm, Land_yieldForm, Total_taxForm, Total_economic_outputForm, Total_revenueForm, Diding_taxesForm, Salt_taxForm, Tariff_and_transitForm, Misc_incomesForm, Total_expenditureForm, BalanceForm, LijinForm, Maritime_customForm, Other_incomesForm, Revenue_officialForm, Revenue_realForm, Gdp_totalForm, Gdp_growth_rateForm, Shares_of_world_gdpForm, Gdp_per_capitaForm, Rate_of_gdp_per_capita_growthForm, WagesForm, Annual_wagesForm, Rate_of_returnForm, Famine_eventForm, Disease_eventForm, Jinshi_degrees_awardedForm, ExaminationForm, Taiping_rebellionForm, Worker_wageForm
class PopulationCreate(PermissionRequiredMixin, CreateView):
    model = Population
    form_class = PopulationForm
    template_name = "crisisdb/population/population_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('population-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context


class PopulationUpdate(PermissionRequiredMixin, UpdateView):
    model = Population
    form_class = PopulationForm
    template_name = "crisisdb/population/population_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context

class PopulationDelete(PermissionRequiredMixin, DeleteView):
    model = Population
    success_url = reverse_lazy('populations')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class PopulationListView(generic.ListView):
    model = Population
    template_name = "crisisdb/population/population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('populations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Population"

        return context
        
class PopulationDetailView(generic.DetailView):
    model = Population
    template_name = "crisisdb/population/population_detail.html"


@permission_required('admin.can_add_log_entry')
def population_download(request):
    items = Population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_population, ])

    return response

        
class Land_taxes_collectedCreate(PermissionRequiredMixin, CreateView):
    model = Land_taxes_collected
    form_class = Land_taxes_collectedForm
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('land_taxes_collected-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Taxes Collected"

        return context


class Land_taxes_collectedUpdate(PermissionRequiredMixin, UpdateView):
    model = Land_taxes_collected
    form_class = Land_taxes_collectedForm
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Taxes Collected"

        return context

class Land_taxes_collectedDelete(PermissionRequiredMixin, DeleteView):
    model = Land_taxes_collected
    success_url = reverse_lazy('land_taxes_collecteds')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Land_taxes_collectedListView(generic.ListView):
    model = Land_taxes_collected
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('land_taxes_collecteds')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Taxes Collected"

        return context
        
class Land_taxes_collectedDetailView(generic.DetailView):
    model = Land_taxes_collected
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_detail.html"


@permission_required('admin.can_add_log_entry')
def land_taxes_collected_download(request):
    items = Land_taxes_collected.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="land_taxes_collecteds.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'land_taxes_collected', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.land_taxes_collected, ])

    return response

        
class Land_yieldCreate(PermissionRequiredMixin, CreateView):
    model = Land_yield
    form_class = Land_yieldForm
    template_name = "crisisdb/land_yield/land_yield_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('land_yield-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Yield"

        return context


class Land_yieldUpdate(PermissionRequiredMixin, UpdateView):
    model = Land_yield
    form_class = Land_yieldForm
    template_name = "crisisdb/land_yield/land_yield_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Yield"

        return context

class Land_yieldDelete(PermissionRequiredMixin, DeleteView):
    model = Land_yield
    success_url = reverse_lazy('land_yields')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Land_yieldListView(generic.ListView):
    model = Land_yield
    template_name = "crisisdb/land_yield/land_yield_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('land_yields')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Land Yield"

        return context
        
class Land_yieldDetailView(generic.DetailView):
    model = Land_yield
    template_name = "crisisdb/land_yield/land_yield_detail.html"


@permission_required('admin.can_add_log_entry')
def land_yield_download(request):
    items = Land_yield.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="land_yields.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'land_yield', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.land_yield, ])

    return response

        
class Total_taxCreate(PermissionRequiredMixin, CreateView):
    model = Total_tax
    form_class = Total_taxForm
    template_name = "crisisdb/total_tax/total_tax_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('total_tax-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Amount of Taxes Collected"

        return context


class Total_taxUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_tax
    form_class = Total_taxForm
    template_name = "crisisdb/total_tax/total_tax_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Amount of Taxes Collected"

        return context

class Total_taxDelete(PermissionRequiredMixin, DeleteView):
    model = Total_tax
    success_url = reverse_lazy('total_taxes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Total_taxListView(generic.ListView):
    model = Total_tax
    template_name = "crisisdb/total_tax/total_tax_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('total_taxes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Amount of Taxes Collected"

        return context
        
class Total_taxDetailView(generic.DetailView):
    model = Total_tax
    template_name = "crisisdb/total_tax/total_tax_detail.html"


@permission_required('admin.can_add_log_entry')
def total_tax_download(request):
    items = Total_tax.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_taxes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_amount_of_taxes_collected', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_amount_of_taxes_collected, ])

    return response

        
class Total_economic_outputCreate(PermissionRequiredMixin, CreateView):
    model = Total_economic_output
    form_class = Total_economic_outputForm
    template_name = "crisisdb/total_economic_output/total_economic_output_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('total_economic_output-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Economic Output"

        return context


class Total_economic_outputUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_economic_output
    form_class = Total_economic_outputForm
    template_name = "crisisdb/total_economic_output/total_economic_output_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Economic Output"

        return context

class Total_economic_outputDelete(PermissionRequiredMixin, DeleteView):
    model = Total_economic_output
    success_url = reverse_lazy('total_economic_outputs')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Total_economic_outputListView(generic.ListView):
    model = Total_economic_output
    template_name = "crisisdb/total_economic_output/total_economic_output_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('total_economic_outputs')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Economic Output"

        return context
        
class Total_economic_outputDetailView(generic.DetailView):
    model = Total_economic_output
    template_name = "crisisdb/total_economic_output/total_economic_output_detail.html"


@permission_required('admin.can_add_log_entry')
def total_economic_output_download(request):
    items = Total_economic_output.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_economic_outputs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_economic_output', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_economic_output, ])

    return response

        
class Total_revenueCreate(PermissionRequiredMixin, CreateView):
    model = Total_revenue
    form_class = Total_revenueForm
    template_name = "crisisdb/total_revenue/total_revenue_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('total_revenue-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Revenue"

        return context


class Total_revenueUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_revenue
    form_class = Total_revenueForm
    template_name = "crisisdb/total_revenue/total_revenue_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Revenue"

        return context

class Total_revenueDelete(PermissionRequiredMixin, DeleteView):
    model = Total_revenue
    success_url = reverse_lazy('total_revenues')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Total_revenueListView(generic.ListView):
    model = Total_revenue
    template_name = "crisisdb/total_revenue/total_revenue_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('total_revenues')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Revenue"

        return context
        
class Total_revenueDetailView(generic.DetailView):
    model = Total_revenue
    template_name = "crisisdb/total_revenue/total_revenue_detail.html"


@permission_required('admin.can_add_log_entry')
def total_revenue_download(request):
    items = Total_revenue.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_revenues.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_revenue', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_revenue, ])

    return response

        
class Diding_taxesCreate(PermissionRequiredMixin, CreateView):
    model = Diding_taxes
    form_class = Diding_taxesForm
    template_name = "crisisdb/diding_taxes/diding_taxes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('diding_taxes-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Diding Taxes"

        return context


class Diding_taxesUpdate(PermissionRequiredMixin, UpdateView):
    model = Diding_taxes
    form_class = Diding_taxesForm
    template_name = "crisisdb/diding_taxes/diding_taxes_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Diding Taxes"

        return context

class Diding_taxesDelete(PermissionRequiredMixin, DeleteView):
    model = Diding_taxes
    success_url = reverse_lazy('diding_taxes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Diding_taxesListView(generic.ListView):
    model = Diding_taxes
    template_name = "crisisdb/diding_taxes/diding_taxes_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('diding_taxes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Diding Taxes"

        return context
        
class Diding_taxesDetailView(generic.DetailView):
    model = Diding_taxes
    template_name = "crisisdb/diding_taxes/diding_taxes_detail.html"


@permission_required('admin.can_add_log_entry')
def diding_taxes_download(request):
    items = Diding_taxes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="diding_taxes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'diding_taxes', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.diding_taxes, ])

    return response

        
class Salt_taxCreate(PermissionRequiredMixin, CreateView):
    model = Salt_tax
    form_class = Salt_taxForm
    template_name = "crisisdb/salt_tax/salt_tax_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('salt_tax-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Salt Tax"

        return context


class Salt_taxUpdate(PermissionRequiredMixin, UpdateView):
    model = Salt_tax
    form_class = Salt_taxForm
    template_name = "crisisdb/salt_tax/salt_tax_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Salt Tax"

        return context

class Salt_taxDelete(PermissionRequiredMixin, DeleteView):
    model = Salt_tax
    success_url = reverse_lazy('salt_taxes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Salt_taxListView(generic.ListView):
    model = Salt_tax
    template_name = "crisisdb/salt_tax/salt_tax_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('salt_taxes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Salt Tax"

        return context
        
class Salt_taxDetailView(generic.DetailView):
    model = Salt_tax
    template_name = "crisisdb/salt_tax/salt_tax_detail.html"


@permission_required('admin.can_add_log_entry')
def salt_tax_download(request):
    items = Salt_tax.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salt_taxes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'salt_tax', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.salt_tax, ])

    return response

        
class Tariff_and_transitCreate(PermissionRequiredMixin, CreateView):
    model = Tariff_and_transit
    form_class = Tariff_and_transitForm
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('tariff_and_transit-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tariff and Transit"

        return context


class Tariff_and_transitUpdate(PermissionRequiredMixin, UpdateView):
    model = Tariff_and_transit
    form_class = Tariff_and_transitForm
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tariff and Transit"

        return context

class Tariff_and_transitDelete(PermissionRequiredMixin, DeleteView):
    model = Tariff_and_transit
    success_url = reverse_lazy('tariff_and_transits')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Tariff_and_transitListView(generic.ListView):
    model = Tariff_and_transit
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('tariff_and_transits')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tariff and Transit"

        return context
        
class Tariff_and_transitDetailView(generic.DetailView):
    model = Tariff_and_transit
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_detail.html"


@permission_required('admin.can_add_log_entry')
def tariff_and_transit_download(request):
    items = Tariff_and_transit.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tariff_and_transits.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'tariff_and_transit', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.tariff_and_transit, ])

    return response

        
class Misc_incomesCreate(PermissionRequiredMixin, CreateView):
    model = Misc_incomes
    form_class = Misc_incomesForm
    template_name = "crisisdb/misc_incomes/misc_incomes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('misc_incomes-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Misc Incomes"

        return context


class Misc_incomesUpdate(PermissionRequiredMixin, UpdateView):
    model = Misc_incomes
    form_class = Misc_incomesForm
    template_name = "crisisdb/misc_incomes/misc_incomes_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Misc Incomes"

        return context

class Misc_incomesDelete(PermissionRequiredMixin, DeleteView):
    model = Misc_incomes
    success_url = reverse_lazy('misc_incomes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Misc_incomesListView(generic.ListView):
    model = Misc_incomes
    template_name = "crisisdb/misc_incomes/misc_incomes_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('misc_incomes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Misc Incomes"

        return context
        
class Misc_incomesDetailView(generic.DetailView):
    model = Misc_incomes
    template_name = "crisisdb/misc_incomes/misc_incomes_detail.html"


@permission_required('admin.can_add_log_entry')
def misc_incomes_download(request):
    items = Misc_incomes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="misc_incomes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'misc_incomes', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.misc_incomes, ])

    return response

        
class Total_expenditureCreate(PermissionRequiredMixin, CreateView):
    model = Total_expenditure
    form_class = Total_expenditureForm
    template_name = "crisisdb/total_expenditure/total_expenditure_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('total_expenditure-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Expenditure"

        return context


class Total_expenditureUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_expenditure
    form_class = Total_expenditureForm
    template_name = "crisisdb/total_expenditure/total_expenditure_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Expenditure"

        return context

class Total_expenditureDelete(PermissionRequiredMixin, DeleteView):
    model = Total_expenditure
    success_url = reverse_lazy('total_expenditures')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Total_expenditureListView(generic.ListView):
    model = Total_expenditure
    template_name = "crisisdb/total_expenditure/total_expenditure_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('total_expenditures')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Total Expenditure"

        return context
        
class Total_expenditureDetailView(generic.DetailView):
    model = Total_expenditure
    template_name = "crisisdb/total_expenditure/total_expenditure_detail.html"


@permission_required('admin.can_add_log_entry')
def total_expenditure_download(request):
    items = Total_expenditure.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_expenditures.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_expenditure', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_expenditure, ])

    return response

        
class BalanceCreate(PermissionRequiredMixin, CreateView):
    model = Balance
    form_class = BalanceForm
    template_name = "crisisdb/balance/balance_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('balance-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Balance"

        return context


class BalanceUpdate(PermissionRequiredMixin, UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = "crisisdb/balance/balance_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Balance"

        return context

class BalanceDelete(PermissionRequiredMixin, DeleteView):
    model = Balance
    success_url = reverse_lazy('balances')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class BalanceListView(generic.ListView):
    model = Balance
    template_name = "crisisdb/balance/balance_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('balances')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Balance"

        return context
        
class BalanceDetailView(generic.DetailView):
    model = Balance
    template_name = "crisisdb/balance/balance_detail.html"


@permission_required('admin.can_add_log_entry')
def balance_download(request):
    items = Balance.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="balances.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'balance', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.balance, ])

    return response

        
class LijinCreate(PermissionRequiredMixin, CreateView):
    model = Lijin
    form_class = LijinForm
    template_name = "crisisdb/lijin/lijin_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('lijin-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lijin"

        return context


class LijinUpdate(PermissionRequiredMixin, UpdateView):
    model = Lijin
    form_class = LijinForm
    template_name = "crisisdb/lijin/lijin_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lijin"

        return context

class LijinDelete(PermissionRequiredMixin, DeleteView):
    model = Lijin
    success_url = reverse_lazy('lijins')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class LijinListView(generic.ListView):
    model = Lijin
    template_name = "crisisdb/lijin/lijin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('lijins')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lijin"

        return context
        
class LijinDetailView(generic.DetailView):
    model = Lijin
    template_name = "crisisdb/lijin/lijin_detail.html"


@permission_required('admin.can_add_log_entry')
def lijin_download(request):
    items = Lijin.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lijins.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'lijin', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.lijin, ])

    return response

        
class Maritime_customCreate(PermissionRequiredMixin, CreateView):
    model = Maritime_custom
    form_class = Maritime_customForm
    template_name = "crisisdb/maritime_custom/maritime_custom_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('maritime_custom-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Maritime Custom"

        return context


class Maritime_customUpdate(PermissionRequiredMixin, UpdateView):
    model = Maritime_custom
    form_class = Maritime_customForm
    template_name = "crisisdb/maritime_custom/maritime_custom_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Maritime Custom"

        return context

class Maritime_customDelete(PermissionRequiredMixin, DeleteView):
    model = Maritime_custom
    success_url = reverse_lazy('maritime_customs')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Maritime_customListView(generic.ListView):
    model = Maritime_custom
    template_name = "crisisdb/maritime_custom/maritime_custom_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('maritime_customs')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Maritime Custom"

        return context
        
class Maritime_customDetailView(generic.DetailView):
    model = Maritime_custom
    template_name = "crisisdb/maritime_custom/maritime_custom_detail.html"


@permission_required('admin.can_add_log_entry')
def maritime_custom_download(request):
    items = Maritime_custom.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="maritime_customs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'maritime_custom', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.maritime_custom, ])

    return response

        
class Other_incomesCreate(PermissionRequiredMixin, CreateView):
    model = Other_incomes
    form_class = Other_incomesForm
    template_name = "crisisdb/other_incomes/other_incomes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('other_incomes-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Other Incomes"

        return context


class Other_incomesUpdate(PermissionRequiredMixin, UpdateView):
    model = Other_incomes
    form_class = Other_incomesForm
    template_name = "crisisdb/other_incomes/other_incomes_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Other Incomes"

        return context

class Other_incomesDelete(PermissionRequiredMixin, DeleteView):
    model = Other_incomes
    success_url = reverse_lazy('other_incomes')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Other_incomesListView(generic.ListView):
    model = Other_incomes
    template_name = "crisisdb/other_incomes/other_incomes_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('other_incomes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Other Incomes"

        return context
        
class Other_incomesDetailView(generic.DetailView):
    model = Other_incomes
    template_name = "crisisdb/other_incomes/other_incomes_detail.html"


@permission_required('admin.can_add_log_entry')
def other_incomes_download(request):
    items = Other_incomes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="other_incomes.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'other_incomes', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.other_incomes, ])

    return response

        
class Revenue_officialCreate(PermissionRequiredMixin, CreateView):
    model = Revenue_official
    form_class = Revenue_officialForm
    template_name = "crisisdb/revenue_official/revenue_official_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('revenue_official-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Official"

        return context


class Revenue_officialUpdate(PermissionRequiredMixin, UpdateView):
    model = Revenue_official
    form_class = Revenue_officialForm
    template_name = "crisisdb/revenue_official/revenue_official_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Official"

        return context

class Revenue_officialDelete(PermissionRequiredMixin, DeleteView):
    model = Revenue_official
    success_url = reverse_lazy('revenue_officials')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Revenue_officialListView(generic.ListView):
    model = Revenue_official
    template_name = "crisisdb/revenue_official/revenue_official_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('revenue_officials')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Official"

        return context
        
class Revenue_officialDetailView(generic.DetailView):
    model = Revenue_official
    template_name = "crisisdb/revenue_official/revenue_official_detail.html"


@permission_required('admin.can_add_log_entry')
def revenue_official_download(request):
    items = Revenue_official.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="revenue_officials.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'revenue_official', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.revenue_official, ])

    return response

        
class Revenue_realCreate(PermissionRequiredMixin, CreateView):
    model = Revenue_real
    form_class = Revenue_realForm
    template_name = "crisisdb/revenue_real/revenue_real_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('revenue_real-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Real"

        return context


class Revenue_realUpdate(PermissionRequiredMixin, UpdateView):
    model = Revenue_real
    form_class = Revenue_realForm
    template_name = "crisisdb/revenue_real/revenue_real_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Real"

        return context

class Revenue_realDelete(PermissionRequiredMixin, DeleteView):
    model = Revenue_real
    success_url = reverse_lazy('revenue_reals')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Revenue_realListView(generic.ListView):
    model = Revenue_real
    template_name = "crisisdb/revenue_real/revenue_real_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('revenue_reals')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Revenue Real"

        return context
        
class Revenue_realDetailView(generic.DetailView):
    model = Revenue_real
    template_name = "crisisdb/revenue_real/revenue_real_detail.html"


@permission_required('admin.can_add_log_entry')
def revenue_real_download(request):
    items = Revenue_real.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="revenue_reals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'revenue_real', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.revenue_real, ])

    return response

        
class Gdp_totalCreate(PermissionRequiredMixin, CreateView):
    model = Gdp_total
    form_class = Gdp_totalForm
    template_name = "crisisdb/gdp_total/gdp_total_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('gdp_total-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Total"

        return context


class Gdp_totalUpdate(PermissionRequiredMixin, UpdateView):
    model = Gdp_total
    form_class = Gdp_totalForm
    template_name = "crisisdb/gdp_total/gdp_total_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Total"

        return context

class Gdp_totalDelete(PermissionRequiredMixin, DeleteView):
    model = Gdp_total
    success_url = reverse_lazy('gdp_totals')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Gdp_totalListView(generic.ListView):
    model = Gdp_total
    template_name = "crisisdb/gdp_total/gdp_total_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('gdp_totals')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Total"

        return context
        
class Gdp_totalDetailView(generic.DetailView):
    model = Gdp_total
    template_name = "crisisdb/gdp_total/gdp_total_detail.html"


@permission_required('admin.can_add_log_entry')
def gdp_total_download(request):
    items = Gdp_total.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_totals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gdp_total', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.gdp_total, ])

    return response

        
class Gdp_growth_rateCreate(PermissionRequiredMixin, CreateView):
    model = Gdp_growth_rate
    form_class = Gdp_growth_rateForm
    template_name = "crisisdb/gdp_growth_rate/gdp_growth_rate_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('gdp_growth_rate-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Growth Rate"

        return context


class Gdp_growth_rateUpdate(PermissionRequiredMixin, UpdateView):
    model = Gdp_growth_rate
    form_class = Gdp_growth_rateForm
    template_name = "crisisdb/gdp_growth_rate/gdp_growth_rate_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Growth Rate"

        return context

class Gdp_growth_rateDelete(PermissionRequiredMixin, DeleteView):
    model = Gdp_growth_rate
    success_url = reverse_lazy('gdp_growth_rates')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Gdp_growth_rateListView(generic.ListView):
    model = Gdp_growth_rate
    template_name = "crisisdb/gdp_growth_rate/gdp_growth_rate_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('gdp_growth_rates')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Growth Rate"

        return context
        
class Gdp_growth_rateDetailView(generic.DetailView):
    model = Gdp_growth_rate
    template_name = "crisisdb/gdp_growth_rate/gdp_growth_rate_detail.html"


@permission_required('admin.can_add_log_entry')
def gdp_growth_rate_download(request):
    items = Gdp_growth_rate.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_growth_rates.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gdp_growth_rate', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.gdp_growth_rate, ])

    return response

        
class Shares_of_world_gdpCreate(PermissionRequiredMixin, CreateView):
    model = Shares_of_world_gdp
    form_class = Shares_of_world_gdpForm
    template_name = "crisisdb/shares_of_world_gdp/shares_of_world_gdp_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('shares_of_world_gdp-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shares of World Gdp"

        return context


class Shares_of_world_gdpUpdate(PermissionRequiredMixin, UpdateView):
    model = Shares_of_world_gdp
    form_class = Shares_of_world_gdpForm
    template_name = "crisisdb/shares_of_world_gdp/shares_of_world_gdp_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shares of World Gdp"

        return context

class Shares_of_world_gdpDelete(PermissionRequiredMixin, DeleteView):
    model = Shares_of_world_gdp
    success_url = reverse_lazy('shares_of_world_gdps')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Shares_of_world_gdpListView(generic.ListView):
    model = Shares_of_world_gdp
    template_name = "crisisdb/shares_of_world_gdp/shares_of_world_gdp_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('shares_of_world_gdps')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shares of World Gdp"

        return context
        
class Shares_of_world_gdpDetailView(generic.DetailView):
    model = Shares_of_world_gdp
    template_name = "crisisdb/shares_of_world_gdp/shares_of_world_gdp_detail.html"


@permission_required('admin.can_add_log_entry')
def shares_of_world_gdp_download(request):
    items = Shares_of_world_gdp.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shares_of_world_gdps.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'shares_of_world_gdp', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.shares_of_world_gdp, ])

    return response

        
class Gdp_per_capitaCreate(PermissionRequiredMixin, CreateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('gdp_per_capita-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context


class Gdp_per_capitaUpdate(PermissionRequiredMixin, UpdateView):
    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context

class Gdp_per_capitaDelete(PermissionRequiredMixin, DeleteView):
    model = Gdp_per_capita
    success_url = reverse_lazy('gdp_per_capitas')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Gdp_per_capitaListView(generic.ListView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('gdp_per_capitas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gdp Per Capita"

        return context
        
class Gdp_per_capitaDetailView(generic.DetailView):
    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_detail.html"


@permission_required('admin.can_add_log_entry')
def gdp_per_capita_download(request):
    items = Gdp_per_capita.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gdp_per_capitas.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'gdp_per_capita', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.gdp_per_capita, ])

    return response

        
class Rate_of_gdp_per_capita_growthCreate(PermissionRequiredMixin, CreateView):
    model = Rate_of_gdp_per_capita_growth
    form_class = Rate_of_gdp_per_capita_growthForm
    template_name = "crisisdb/rate_of_gdp_per_capita_growth/rate_of_gdp_per_capita_growth_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('rate_of_gdp_per_capita_growth-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Gdp Per Capita Growth"

        return context


class Rate_of_gdp_per_capita_growthUpdate(PermissionRequiredMixin, UpdateView):
    model = Rate_of_gdp_per_capita_growth
    form_class = Rate_of_gdp_per_capita_growthForm
    template_name = "crisisdb/rate_of_gdp_per_capita_growth/rate_of_gdp_per_capita_growth_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Gdp Per Capita Growth"

        return context

class Rate_of_gdp_per_capita_growthDelete(PermissionRequiredMixin, DeleteView):
    model = Rate_of_gdp_per_capita_growth
    success_url = reverse_lazy('rate_of_gdp_per_capita_growths')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Rate_of_gdp_per_capita_growthListView(generic.ListView):
    model = Rate_of_gdp_per_capita_growth
    template_name = "crisisdb/rate_of_gdp_per_capita_growth/rate_of_gdp_per_capita_growth_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('rate_of_gdp_per_capita_growths')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Gdp Per Capita Growth"

        return context
        
class Rate_of_gdp_per_capita_growthDetailView(generic.DetailView):
    model = Rate_of_gdp_per_capita_growth
    template_name = "crisisdb/rate_of_gdp_per_capita_growth/rate_of_gdp_per_capita_growth_detail.html"


@permission_required('admin.can_add_log_entry')
def rate_of_gdp_per_capita_growth_download(request):
    items = Rate_of_gdp_per_capita_growth.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rate_of_gdp_per_capita_growths.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'rate_of_gdp_per_capita_growth', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.rate_of_gdp_per_capita_growth, ])

    return response

        
class WagesCreate(PermissionRequiredMixin, CreateView):
    model = Wages
    form_class = WagesForm
    template_name = "crisisdb/wages/wages_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('wages-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wages"

        return context


class WagesUpdate(PermissionRequiredMixin, UpdateView):
    model = Wages
    form_class = WagesForm
    template_name = "crisisdb/wages/wages_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wages"

        return context

class WagesDelete(PermissionRequiredMixin, DeleteView):
    model = Wages
    success_url = reverse_lazy('wages')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class WagesListView(generic.ListView):
    model = Wages
    template_name = "crisisdb/wages/wages_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('wages')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wages"

        return context
        
class WagesDetailView(generic.DetailView):
    model = Wages
    template_name = "crisisdb/wages/wages_detail.html"


@permission_required('admin.can_add_log_entry')
def wages_download(request):
    items = Wages.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="wages.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'wages', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.wages, ])

    return response

        
class Annual_wagesCreate(PermissionRequiredMixin, CreateView):
    model = Annual_wages
    form_class = Annual_wagesForm
    template_name = "crisisdb/annual_wages/annual_wages_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('annual_wages-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Annual Wages"

        return context


class Annual_wagesUpdate(PermissionRequiredMixin, UpdateView):
    model = Annual_wages
    form_class = Annual_wagesForm
    template_name = "crisisdb/annual_wages/annual_wages_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Annual Wages"

        return context

class Annual_wagesDelete(PermissionRequiredMixin, DeleteView):
    model = Annual_wages
    success_url = reverse_lazy('annual_wages')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Annual_wagesListView(generic.ListView):
    model = Annual_wages
    template_name = "crisisdb/annual_wages/annual_wages_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('annual_wages')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Annual Wages"

        return context
        
class Annual_wagesDetailView(generic.DetailView):
    model = Annual_wages
    template_name = "crisisdb/annual_wages/annual_wages_detail.html"


@permission_required('admin.can_add_log_entry')
def annual_wages_download(request):
    items = Annual_wages.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="annual_wages.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'annual_wages', 'job_category', 'job_description', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.annual_wages, obj.job_category, obj.job_description, ])

    return response

        
class Rate_of_returnCreate(PermissionRequiredMixin, CreateView):
    model = Rate_of_return
    form_class = Rate_of_returnForm
    template_name = "crisisdb/rate_of_return/rate_of_return_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('rate_of_return-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Return"

        return context


class Rate_of_returnUpdate(PermissionRequiredMixin, UpdateView):
    model = Rate_of_return
    form_class = Rate_of_returnForm
    template_name = "crisisdb/rate_of_return/rate_of_return_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Return"

        return context

class Rate_of_returnDelete(PermissionRequiredMixin, DeleteView):
    model = Rate_of_return
    success_url = reverse_lazy('rate_of_returns')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Rate_of_returnListView(generic.ListView):
    model = Rate_of_return
    template_name = "crisisdb/rate_of_return/rate_of_return_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('rate_of_returns')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Rate of Return"

        return context
        
class Rate_of_returnDetailView(generic.DetailView):
    model = Rate_of_return
    template_name = "crisisdb/rate_of_return/rate_of_return_detail.html"


@permission_required('admin.can_add_log_entry')
def rate_of_return_download(request):
    items = Rate_of_return.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rate_of_returns.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'rate_of_return', 'job_category', 'job_description', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.rate_of_return, obj.job_category, obj.job_description, ])

    return response

        
class Famine_eventCreate(PermissionRequiredMixin, CreateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('famine_event-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context


class Famine_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context

class Famine_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Famine_event
    success_url = reverse_lazy('famine_events')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Famine_eventListView(generic.ListView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('famine_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Famine Event"

        return context
        
class Famine_eventDetailView(generic.DetailView):
    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_detail.html"


@permission_required('admin.can_add_log_entry')
def famine_event_download(request):
    items = Famine_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famine_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'famine_event', 'latitude', 'longitude', 'elevation', 'sub_category', 'magnitude', 'duration', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.famine_event, obj.latitude, obj.longitude, obj.elevation, obj.sub_category, obj.magnitude, obj.duration, ])

    return response

        
class Disease_eventCreate(PermissionRequiredMixin, CreateView):
    model = Disease_event
    form_class = Disease_eventForm
    template_name = "crisisdb/disease_event/disease_event_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('disease_event-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Disease Event"

        return context


class Disease_eventUpdate(PermissionRequiredMixin, UpdateView):
    model = Disease_event
    form_class = Disease_eventForm
    template_name = "crisisdb/disease_event/disease_event_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Disease Event"

        return context

class Disease_eventDelete(PermissionRequiredMixin, DeleteView):
    model = Disease_event
    success_url = reverse_lazy('disease_events')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Disease_eventListView(generic.ListView):
    model = Disease_event
    template_name = "crisisdb/disease_event/disease_event_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('disease_events')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Disease Event"

        return context
        
class Disease_eventDetailView(generic.DetailView):
    model = Disease_event
    template_name = "crisisdb/disease_event/disease_event_detail.html"


@permission_required('admin.can_add_log_entry')
def disease_event_download(request):
    items = Disease_event.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="disease_events.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'disease_event', 'latitude', 'longitude', 'elevation', 'sub_category', 'magnitude', 'duration', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.disease_event, obj.latitude, obj.longitude, obj.elevation, obj.sub_category, obj.magnitude, obj.duration, ])

    return response

        
class Jinshi_degrees_awardedCreate(PermissionRequiredMixin, CreateView):
    model = Jinshi_degrees_awarded
    form_class = Jinshi_degrees_awardedForm
    template_name = "crisisdb/jinshi_degrees_awarded/jinshi_degrees_awarded_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('jinshi_degrees_awarded-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Jinshi Degrees Awarded"

        return context


class Jinshi_degrees_awardedUpdate(PermissionRequiredMixin, UpdateView):
    model = Jinshi_degrees_awarded
    form_class = Jinshi_degrees_awardedForm
    template_name = "crisisdb/jinshi_degrees_awarded/jinshi_degrees_awarded_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Jinshi Degrees Awarded"

        return context

class Jinshi_degrees_awardedDelete(PermissionRequiredMixin, DeleteView):
    model = Jinshi_degrees_awarded
    success_url = reverse_lazy('jinshi_degrees_awardeds')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Jinshi_degrees_awardedListView(generic.ListView):
    model = Jinshi_degrees_awarded
    template_name = "crisisdb/jinshi_degrees_awarded/jinshi_degrees_awarded_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('jinshi_degrees_awardeds')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Jinshi Degrees Awarded"

        return context
        
class Jinshi_degrees_awardedDetailView(generic.DetailView):
    model = Jinshi_degrees_awarded
    template_name = "crisisdb/jinshi_degrees_awarded/jinshi_degrees_awarded_detail.html"


@permission_required('admin.can_add_log_entry')
def jinshi_degrees_awarded_download(request):
    items = Jinshi_degrees_awarded.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="jinshi_degrees_awardeds.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'jinshi_degrees_awarded', 'emperor', 'population_in_year_x', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.jinshi_degrees_awarded, obj.emperor, obj.population_in_year_x, ])

    return response

        
class ExaminationCreate(PermissionRequiredMixin, CreateView):
    model = Examination
    form_class = ExaminationForm
    template_name = "crisisdb/examination/examination_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('examination-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination"

        return context


class ExaminationUpdate(PermissionRequiredMixin, UpdateView):
    model = Examination
    form_class = ExaminationForm
    template_name = "crisisdb/examination/examination_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination"

        return context

class ExaminationDelete(PermissionRequiredMixin, DeleteView):
    model = Examination
    success_url = reverse_lazy('examinations')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class ExaminationListView(generic.ListView):
    model = Examination
    template_name = "crisisdb/examination/examination_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('examinations')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination"

        return context
        
class ExaminationDetailView(generic.DetailView):
    model = Examination
    template_name = "crisisdb/examination/examination_detail.html"


@permission_required('admin.can_add_log_entry')
def examination_download(request):
    items = Examination.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="examinations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'examination', 'no_of_participants', 'degrees_awarded', 'passing_ratio', 'place', 'ratio_examiner_per_candidate', 'no_of_examiners', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.examination, obj.no_of_participants, obj.degrees_awarded, obj.passing_ratio, obj.place, obj.ratio_examiner_per_candidate, obj.no_of_examiners, ])

    return response

        
class Taiping_rebellionCreate(PermissionRequiredMixin, CreateView):
    model = Taiping_rebellion
    form_class = Taiping_rebellionForm
    template_name = "crisisdb/taiping_rebellion/taiping_rebellion_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('taiping_rebellion-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Taiping Rebellion"

        return context


class Taiping_rebellionUpdate(PermissionRequiredMixin, UpdateView):
    model = Taiping_rebellion
    form_class = Taiping_rebellionForm
    template_name = "crisisdb/taiping_rebellion/taiping_rebellion_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Taiping Rebellion"

        return context

class Taiping_rebellionDelete(PermissionRequiredMixin, DeleteView):
    model = Taiping_rebellion
    success_url = reverse_lazy('taiping_rebellions')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Taiping_rebellionListView(generic.ListView):
    model = Taiping_rebellion
    template_name = "crisisdb/taiping_rebellion/taiping_rebellion_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('taiping_rebellions')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Taiping Rebellion"

        return context
        
class Taiping_rebellionDetailView(generic.DetailView):
    model = Taiping_rebellion
    template_name = "crisisdb/taiping_rebellion/taiping_rebellion_detail.html"


@permission_required('admin.can_add_log_entry')
def taiping_rebellion_download(request):
    items = Taiping_rebellion.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="taiping_rebellions.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'taiping_rebellion', 'rebel', 'place', 'ethnic_composition', 'family_background', 'role', 'rank', 'civil_examination', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.taiping_rebellion, obj.rebel, obj.place, obj.ethnic_composition, obj.family_background, obj.role, obj.rank, obj.civil_examination, ])

    return response

        
class Worker_wageCreate(PermissionRequiredMixin, CreateView):
    model = Worker_wage
    form_class = Worker_wageForm
    template_name = "crisisdb/worker_wage/worker_wage_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('worker_wage-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Worker Wage"

        return context


class Worker_wageUpdate(PermissionRequiredMixin, UpdateView):
    model = Worker_wage
    form_class = Worker_wageForm
    template_name = "crisisdb/worker_wage/worker_wage_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Worker Wage"

        return context

class Worker_wageDelete(PermissionRequiredMixin, DeleteView):
    model = Worker_wage
    success_url = reverse_lazy('worker_wages')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class Worker_wageListView(generic.ListView):
    model = Worker_wage
    template_name = "crisisdb/worker_wage/worker_wage_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('worker_wages')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Worker Wage"

        return context
        
class Worker_wageDetailView(generic.DetailView):
    model = Worker_wage
    template_name = "crisisdb/worker_wage/worker_wage_detail.html"


@permission_required('admin.can_add_log_entry')
def worker_wage_download(request):
    items = Worker_wage.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="worker_wages.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'worker_wage', 'area', 'unskilled_construction', 'skilled_construction', 'number_of_districts_with_available_data', 'unskilled_arms_manufacturer', 'population_in_millions_in_1787', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.worker_wage, obj.area, obj.unskilled_construction, obj.skilled_construction, obj.number_of_districts_with_available_data, obj.unskilled_arms_manufacturer, obj.population_in_millions_in_1787, ])

    return response

        
vars_dic = {
'Population': {
	'model': Population,
	'list': PopulationListView,
	'create': PopulationCreate,
	},

'Land_taxes_collected': {
	'model': Land_taxes_collected,
	'list': Land_taxes_collectedListView,
	'create': Land_taxes_collectedCreate,
	},

'Land_yield': {
	'model': Land_yield,
	'list': Land_yieldListView,
	'create': Land_yieldCreate,
	},

'Total_tax': {
	'model': Total_tax,
	'list': Total_taxListView,
	'create': Total_taxCreate,
	},

'Total_economic_output': {
	'model': Total_economic_output,
	'list': Total_economic_outputListView,
	'create': Total_economic_outputCreate,
	},

'Total_revenue': {
	'model': Total_revenue,
	'list': Total_revenueListView,
	'create': Total_revenueCreate,
	},

'Diding_taxes': {
	'model': Diding_taxes,
	'list': Diding_taxesListView,
	'create': Diding_taxesCreate,
	},

'Salt_tax': {
	'model': Salt_tax,
	'list': Salt_taxListView,
	'create': Salt_taxCreate,
	},

'Tariff_and_transit': {
	'model': Tariff_and_transit,
	'list': Tariff_and_transitListView,
	'create': Tariff_and_transitCreate,
	},

'Misc_incomes': {
	'model': Misc_incomes,
	'list': Misc_incomesListView,
	'create': Misc_incomesCreate,
	},

'Total_expenditure': {
	'model': Total_expenditure,
	'list': Total_expenditureListView,
	'create': Total_expenditureCreate,
	},

'Balance': {
	'model': Balance,
	'list': BalanceListView,
	'create': BalanceCreate,
	},

'Lijin': {
	'model': Lijin,
	'list': LijinListView,
	'create': LijinCreate,
	},

'Maritime_custom': {
	'model': Maritime_custom,
	'list': Maritime_customListView,
	'create': Maritime_customCreate,
	},

'Other_incomes': {
	'model': Other_incomes,
	'list': Other_incomesListView,
	'create': Other_incomesCreate,
	},

'Revenue_official': {
	'model': Revenue_official,
	'list': Revenue_officialListView,
	'create': Revenue_officialCreate,
	},

'Revenue_real': {
	'model': Revenue_real,
	'list': Revenue_realListView,
	'create': Revenue_realCreate,
	},

'Gdp_total': {
	'model': Gdp_total,
	'list': Gdp_totalListView,
	'create': Gdp_totalCreate,
	},

'Gdp_growth_rate': {
	'model': Gdp_growth_rate,
	'list': Gdp_growth_rateListView,
	'create': Gdp_growth_rateCreate,
	},

'Shares_of_world_gdp': {
	'model': Shares_of_world_gdp,
	'list': Shares_of_world_gdpListView,
	'create': Shares_of_world_gdpCreate,
	},

'Gdp_per_capita': {
	'model': Gdp_per_capita,
	'list': Gdp_per_capitaListView,
	'create': Gdp_per_capitaCreate,
	},

'Rate_of_gdp_per_capita_growth': {
	'model': Rate_of_gdp_per_capita_growth,
	'list': Rate_of_gdp_per_capita_growthListView,
	'create': Rate_of_gdp_per_capita_growthCreate,
	},

'Wages': {
	'model': Wages,
	'list': WagesListView,
	'create': WagesCreate,
	},

'Annual_wages': {
	'model': Annual_wages,
	'list': Annual_wagesListView,
	'create': Annual_wagesCreate,
	},

'Rate_of_return': {
	'model': Rate_of_return,
	'list': Rate_of_returnListView,
	'create': Rate_of_returnCreate,
	},

'Famine_event': {
	'model': Famine_event,
	'list': Famine_eventListView,
	'create': Famine_eventCreate,
	},

'Disease_event': {
	'model': Disease_event,
	'list': Disease_eventListView,
	'create': Disease_eventCreate,
	},

'Jinshi_degrees_awarded': {
	'model': Jinshi_degrees_awarded,
	'list': Jinshi_degrees_awardedListView,
	'create': Jinshi_degrees_awardedCreate,
	},

'Examination': {
	'model': Examination,
	'list': ExaminationListView,
	'create': ExaminationCreate,
	},

'Taiping_rebellion': {
	'model': Taiping_rebellion,
	'list': Taiping_rebellionListView,
	'create': Taiping_rebellionCreate,
	},

'Worker_wage': {
	'model': Worker_wage,
	'list': Worker_wageListView,
	'create': Worker_wageCreate,
	},
}