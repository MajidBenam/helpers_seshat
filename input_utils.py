# underscore_to_space
import pandas as pd
import os


###########################

###################################### MODELS
# all_my_models = []

def model_generator(vars_dic):
    all_my_models = []
    for k,v in vars_dic.items():
        # test to see if a key in vars_dic has any plural letters:
        if has_any_uppercase(k):
            print("WARNING: variable ", k, " has uppercase letters in its name and it is not recommended")
            
        plural_form = string_pluralizer(k)
        # let's create the columns in models for multi column models
        rows_to_be_added_to_the_model = []
        if 'cols' in v.keys():
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                if v[key_str]["dtype"] == MYTXT_CH:
                    raw_str = f'{v[key_str]["varname"]} = models.{v[key_str]["dtype"][0]}(max_length=500, choices={v[key_str]["varname"]}_{k}_choices)\n'
                if v[key_str]["dtype"] == MYTXT:
                    raw_str = f'{v[key_str]["varname"]} = models.{v[key_str]["dtype"][0]}(max_length=500, blank=True, null=True)\n'
                if v[key_str]["dtype"] == MYINT:
                    raw_str = f'{v[key_str]["varname"]} = models.{v[key_str]["dtype"][0]}(blank=True, null=True)\n'
                if v[key_str]["dtype"] == MYDEC:
                    raw_str = f'{v[key_str]["varname"]} = models.{v[key_str]["dtype"][0]}(max_digits= 25, decimal_places = 10, blank=True, null=True)\n'
                rows_to_be_added_to_the_model.append(raw_str)
            model_cols = "    ".join([myvalue for myvalue in rows_to_be_added_to_the_model])

        else:
            print('Invalid key, value pair in vars dic: ', k)
            
        # let's now create a model
        one_model = f"""
class {k.capitalize()}(SeshatCommon):
    name = models.CharField(max_length=100, default="{k.capitalize()}")
    {model_cols}
    
    class Meta:
        verbose_name = '{k.capitalize()}'
        verbose_name_plural = '{plural_form}'

    @property
    def display_citations(self):
        return return_citations(self)

    def clean(self):
        clean_times(self)

    def get_absolute_url(self):
        return reverse('{k}-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
        
        """
        #print(one_model)
        all_my_models.append(one_model)
    return all_my_models
        

    
############################################ Serializers
def serial_generator(vars_dic):
    all_my_serials = []
    all_my_vars_related_friendly = []
    for k,v in vars_dic.items():
        plural_form = k + 's'
        if k[-1] == "y":
            plural_form = k[:-1] + "ies"
        my_good_var = 'crisisdb_' + k.lower() + '_related'
        all_my_vars_related_friendly.append(my_good_var)
            
        if 'cols' in v.keys():
            all_inner_vars = []
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                all_inner_vars.append(v[key_str]["varname"])
            all_inner_vars_str = ("', '").join(all_inner_vars)
        else:
            all_inner_vars_str = v['varname']
            
        one_serial = f"""
class {k.capitalize()}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {k.capitalize()}
        fields = ['year_from', 'year_to', '{all_inner_vars_str}', 'tag']
"""
        all_my_serials.append(one_serial)
    print('Please insert that into the code a s well:\n', all_my_vars_related_friendly)
        
    return all_my_serials


def serial_for_polity_serializer_generator(vars_dic):
    list_of_sers = []
    for k in vars_dic.keys():
        my_good_var = '\tcrisisdb_' + k.lower() + '_related' + ' = ' + k.capitalize() + 'Serializer' + '(many=True, read_only=True)\n'
        
        list_of_sers.append(my_good_var)
    #print(output_str + ', '.join(list_of_models))
    return ''.join(list_of_sers)

############################################ FORMS
# all_my_forms = []

def form_header_generator(vars_dic):
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)


def form_generator(vars_dic):
    all_my_forms = []
    # here I should generate all the variables
    # make a loop to do so and then add the string to both the fields and the widgets area.
    # four to five variables might be needed.
    for k,v in vars_dic.items():
        # let's consider the potential multi-col models
        rows_to_be_added_to_the_form = []
        if 'cols' in v.keys():
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                raw_str = f"""fields.append('{v[key_str]["varname"]}')\n"""
                rows_to_be_added_to_the_form.append(raw_str)
                
            form_rows = "        ".join([myvalue for myvalue in rows_to_be_added_to_the_form])

        else:
            raw_str = f"""fields.append('{v["varname"]}')\n"""            
            form_rows = raw_str
        
        widgets_to_be_added_to_the_form  = []
        if 'cols' in v.keys():
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                raw_str1 = f"""widgets['{v[key_str]["varname"]}'] = forms.{v[key_str]["dtype"][1]}"""
                raw_str2 = "(attrs={'class': 'form-control  mb-3', })\n"
                widgets_to_be_added_to_the_form.append(raw_str1 + raw_str2)
                
            form_widgets = "        ".join([myvalue for myvalue in widgets_to_be_added_to_the_form])

        else:
            raw_str = f"""widgets['{v["varname"]}'] = forms.{v["dtype"][1]}(
            attrs={{'class': 'form-control  mb-3', }})
        """          
            form_widgets = raw_str
        
        one_form = f"""
class {k.capitalize()}Form(forms.ModelForm):
    class Meta:
        model = {k.capitalize()}
        fields = commonfields.copy()
        {form_rows}
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        {form_widgets}
        """
        #print(one_form)
        all_my_forms.append(one_form)
    return all_my_forms
    
    
    
#################################### URLS
#all_my_urls = []

def url_header_generator(vars_dic):
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)


def url_generator(vars_dic):
    all_my_urls = []
    for k,v in vars_dic.items():
        plural_form = k + 's'
        if k[-1] == "y":
            plural_form = k[:-1] + "ies"
        one_url = f"""
urlpatterns += [
    path('{k}/create/', views.{k.capitalize()}Create.as_view(),
         name="{k}-create"),

    path('{plural_form}/', views.{k.capitalize()}ListView.as_view(), name='{plural_form}'),
    path('{k}/<int:pk>', views.{k.capitalize()}DetailView.as_view(),
         name='{k}-detail'),
    path('{k}/<int:pk>/update/',
         views.{k.capitalize()}Update.as_view(), name="{k}-update"),
    path('{k}/<int:pk>/delete/',
         views.{k.capitalize()}Delete.as_view(), name="{k}-delete"),
    # Download
    path('{k}download/', views.{k}_download,
         name="{k}-download"),
]
        """
        #print(one_view)
        all_my_urls.append(one_url)
    return all_my_urls

################################## VIEWS
# all_my_views = []

def view_header_generator(vars_dic):
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)

def view_header_generator_2(vars_dic):
    output_str = "from .forms import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize()+"Form")
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)

def generate_vars_dic(vars_dic):
    vars_dic_output = {}
    for k, v in vars_dic.items():
        k_cap = k.capitalize()
#         if 'section' in v.keys():
#             section_value = v['section'],
        section_value = v.get('section')
        subsection_value = v.get('subsection')
        vars_dic_output[k_cap] = {
            'model': k_cap + ",",
            'list': k_cap+"ListView,",
            'create': k_cap+"Create,",
            # it is now ingrained in the data dic we are putting in, but potentially we should dynamically read and update it.
            'section': section_value,
            'subsection': subsection_value,
        }
    return vars_dic_output

def view_generator(vars_dic):
    all_my_views = []
    for k,v in vars_dic.items():
        plural_form = k + 's'
        if k[-1] == "y":
            plural_form = k[:-1] + "ies"
            
        #
        if 'cols' in v.keys():
            my_vars_list = []
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                a_good_var = v[key_str]['varname']
                my_vars_list.append(a_good_var)
            myvar = "\', \'".join(my_vars_list)
            myname = v['col1']['varname']
            myvalue = ", obj.".join(my_vars_list)
        else:
            myname = v['varname']
            myvar = v['varname']
            myvalue = v['varname']
        mysection = "No Section Provided"
        mysubsection = "No Subsection Provided"
        if 'section' in v.keys():
            mysection = v['section']
        if 'subsection' in v.keys():
            mysubsection = v['subsection']
            
        one_view = f"""
class {k.capitalize()}Create(PermissionRequiredMixin, CreateView):
    model = {k.capitalize()}
    form_class = {k.capitalize()}Form
    template_name = "crisisdb/{k}/{k}_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('{k}-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "{mysection}"
        context["mysubsection"] = "{mysubsection}"
        context["myvar"] = "{underscore_to_space(myname)}"

        return context


class {k.capitalize()}Update(PermissionRequiredMixin, UpdateView):
    model = {k.capitalize()}
    form_class = {k.capitalize()}Form
    template_name = "crisisdb/{k}/{k}_update.html"
    permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "{mysection}"
        context["mysubsection"] = "{mysubsection}"
        context["myvar"] = "{underscore_to_space(myname)}"

        return context

class {k.capitalize()}Delete(PermissionRequiredMixin, DeleteView):
    model = {k.capitalize()}
    success_url = reverse_lazy('{plural_form}')
    template_name = "core/delete_general.html"
    permission_required = 'catalog.can_mark_returned'


class {k.capitalize()}ListView(generic.ListView):
    model = {k.capitalize()}
    template_name = "crisisdb/{k}/{k}_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('{plural_form}')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mysection"] = "{mysection}"
        context["mysubsection"] = "{mysubsection}"
        context["myvar"] = "{underscore_to_space(myname)}"

        return context
        
class {k.capitalize()}DetailView(generic.DetailView):
    model = {k.capitalize()}
    template_name = "crisisdb/{k}/{k}_detail.html"


@permission_required('admin.can_add_log_entry')
def {k}_download(request):
    items = {k.capitalize()}.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{plural_form}.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', '{myvar}', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.{myvalue}, ])

    return response

        """
        #print(one_view)
        all_my_views.append(one_view)
    return all_my_views



######################################### ADMINS
def admin_header_generator(vars_dic):
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)

def admin_register_generator(vars_dic):
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    #print(output_str + ', '.join(list_of_models))
    return output_str + ', '.join(list_of_models)


####### Functions for Templates:
def templates_folder_make(k):
    foldername = k

    # Create the root folder (once)
    rootfolder = "all_new_seshat_html_templates"
    if not os.path.exists(rootfolder):
        os.mkdir(rootfolder)

    inner_folder = rootfolder + "/" + foldername
    # Create the insider folders (if not already done)
    if not os.path.exists(rootfolder + "/" + foldername ):
        os.mkdir(inner_folder)
        
    full_name_list = inner_folder + "/" + k +"_list.html"
    full_name_detail = inner_folder  + "/" + k +"_detail.html"
    full_name_form = inner_folder + "/" + k +"_form.html"
    full_name_update = inner_folder + "/" + k +"_update.html"
    
    return (full_name_list, full_name_detail, full_name_form, full_name_update)
    



############################################ TEMPLATES
# this takes care of all templates:

def create_all_templates(vars_dic):
    all_my_detail_templates = []
    all_my_list_templates = []
    all_my_form_templates = []
    all_my_update_templates = []
    for k,v in vars_dic.items():
        full_name_list, full_name_detail, full_name_form, full_name_update = templates_folder_make(k)

        # potential changes to k and v values before altering the string
        if "cols" not in v.keys():
            plural_form = k + 's'
            if k[-1] == "y":
                plural_form = k[:-1] + "ies"

            spaced_value = underscore_to_space(v["varname"])
            
            with_comma_value = comma_value_maker(v)
                
            if 'vardesc' in v.keys():
                my_top_note = v['vardesc']
                myheadings_str = col_heading_maker(spaced_value, my_top_note, importance_maker(v))
            else:
                myheadings_str = col_heading_maker(spaced_value, "NOTHING", importance_maker(v))
            #myheadings_str = f'''<th style="text-align: center;" scope="col">{spaced_value}</th>'''
            myvalues_str = f'''<td class="{importance_maker(v)}" style="text-align: center;">{{{{ object.{with_comma_value} }}}}</td>'''
            # for list page
            myvalues_for_list_str = inner_value_maker(with_comma_value, importance_maker(v))
            # for the only variable in FORM.PY
            my_extra_vars_str = f'''{{{{ form.{v["varname"]}|as_crispy_field }}}}'''
            # we have no extra variables in this conditional chunk 
            my_extra_vars2_str = ""
            
        else:
            myheadings = []
            myvalues = []
            my_extra_vars_str = ""
            my_extra_vars2 = []
            myvalues_for_list_str0 = ""
            myvalues_for_list = []
            # my main column in the model
            main_col_header = ""
            main_col_value = ""
            # other columns
            for j in range(v['cols']):
                key_str = 'col' + str(j+1)
                spaced_value = underscore_to_space(v[key_str]["varname"])
                if j == 0:
                    main_col_header = spaced_value
                         
                if 'vardesc' in v[key_str].keys():
                    # here we should add the description (notes) to the top-of-the-table column 
                    my_top_note = v[key_str]['vardesc']
                    raw_str = col_heading_maker(spaced_value, my_top_note, importance_maker(v[key_str]))
                else:
                    raw_str = col_heading_maker(spaced_value, "NOTHING", importance_maker(v[key_str]))
                myheadings.append(raw_str)
                # input for comma_value_make must be v["key_str"]
                with_comma_value = comma_value_maker(v[key_str])
                raw_str2 = f'''<td class="{importance_maker(v[key_str])}" style="text-align: center;">{{{{ object.{with_comma_value} }}}}</td>'''
                myvalues.append(raw_str2)
                if j == 0:
                    my_extra_vars_str = f'''{{{{ form.{v[key_str]["varname"]}|as_crispy_field }}}}'''
                    myvalues_for_list_str0 = inner_value_maker(with_comma_value, importance_maker(v[key_str]))
                    myvalues_for_list.append(myvalues_for_list_str0)
                else:
                    if v['cols'] == 3 or v['cols'] == 2:
                        div = 6
                    elif v['cols'] == 4:
                        div = 4
                    elif v['cols'] == 5:
                        div = 3
                    else:
                        div = 4
                    raw_str3 = f'''
<div class="col-md-{div} mb-2">
    {{{{ form.{v[key_str]["varname"]}|as_crispy_field }}}}
</div>'''
                    my_extra_vars2.append(raw_str3)
                    raw_for_list = inner_value_maker(with_comma_value, importance_maker(v[key_str]))
                    myvalues_for_list.append(raw_for_list)
                    
            # myheadings_str for both list and detail
            myheadings_str = "\n".join([myheading for myheading in myheadings])
            # for detail
            myvalues_str = "\n".join([myvalue for myvalue in myvalues])
            # for detail pages
            my_extra_vars2_str = "\n".join([myvalue for myvalue in my_extra_vars2])
            # for list pages
            myvalues_for_list_str = "\n".join([myvalue for myvalue in myvalues_for_list])
        
        main_descr_str = main_description_maker(v)
                
        # we need to add several headings and several extra cols if needed
        one_detail = f'''{{% extends "core/detail_base.html" %}}
{{% load static %}}
{{% load humanize %}}

{{% block addmore %}}
<a href="{{% url '{k}-create' %}}" class="btn btn-outline-success mx-3 my-4 float-end"> &#128934; &nbsp; Add Another Fact &nbsp; <i class="fa fa-plus"></i>
</a>
<a href="{{% url '{plural_form}' %}}" class="btn btn-outline-primary ms-auto my-4 float-end">&#8983; See All Such Facts
</a>
{{% endblock addmore %}}

{{% block myheadings %}}
{myheadings_str}
{{% endblock myheadings %}}

{{% block extracols %}}
{myvalues_str}
{{% endblock extracols %}}
        '''
        print(one_detail)
        all_my_detail_templates.append(one_detail)
        
        
        one_form = f'''{{% extends "core/form_base.html" %}}
{{% load crispy_forms_tags %}}
{{% load humanize %}}

{{% block extra_vars %}}
    <div class="col-md-4 mb-2">
        {my_extra_vars_str}
    </div>
{{% endblock extra_vars %}}

{{% block extra_vars2 %}}
{my_extra_vars2_str}
{{% endblock extra_vars2 %}}
        '''
        print(one_form)
        all_my_form_templates.append(one_form)
        one_update = f'''{{% extends "core/form_base.html" %}}
{{% load crispy_forms_tags %}}
{{% load humanize %}}

{{% block extra_vars %}}
    <div class="col-md-4 mb-2">
        {my_extra_vars_str}
    </div>
{{% endblock extra_vars %}}

{{% block extra_vars2 %}}
{my_extra_vars2_str}
{{% endblock extra_vars2 %}}

{{% block delete_button %}}
    <a href="{{% url '{k}-delete' object.id %}}" type="cancel" class="btn btn-outline-danger my-auto btn-block btn-lg">Delete </a>
{{% endblock delete_button %}}
        '''
        print(one_update)
        all_my_update_templates.append(one_update)
        
        one_list = f'''{{% extends "core/list_base.html" %}}
{{% load crispy_forms_tags %}}
{{% load static %}}
{{% load humanize %}}

{{% block download_button %}}
    <a href="{{% url '{k}-create' %}}" class="btn btn-outline-success mx-3 my-4 float-end"><i class="fas fa-plus"></i> &nbsp; Add More Facts</a>
    <a href="{{% url '{k}-download' %}}" class="btn btn-outline-primary ms-auto my-4 float-end"><i class="fas fa-download"></i> &nbsp; Download All</a>
{{% endblock download_button %}}

{{% block main_description %}}
{main_descr_str}
{{% endblock main_description %}}

{{% block myheadings_list %}}
{myheadings_str}
{{% endblock myheadings_list %}}

{{% block extra_vars_list %}}
{myvalues_for_list_str}
{{% endblock extra_vars_list %}}

<!-- Update Button -->
{{% block update_button %}}
    <td style="text-align: center;"><a href="{{% url '{k}-update' obj.id %}}"><button class="btn btn-outline-primary btn-sm">Update</button></a></td>
{{% endblock update_button %}}
        '''
        print(one_list)
        all_my_list_templates.append(one_list)
        
        with open(full_name_detail, 'w') as f_d:
            f_d.write(one_detail)
        
        with open(full_name_list, 'w') as f_l:
            f_l.write(one_list)
            
        with open(full_name_form, 'w') as f_f:
            f_f.write(one_form)
            
        with open(full_name_update, 'w') as f_u:
            f_u.write(one_update)
          #return all_my_detail_templates
    
    
def template_detail_generator(vars_dic):
    all_my_details = []
    for k,v in vars_dic.items():
        plural_form = k + 's'
        if k[-1] == "y":
            plural_form = k[:-1] + "ies"
        one_detail = f"""
{{% extends "core/detail_base.html" %}}
{{% load static %}}
{{% load humanize %}}

<a href="{{% url '{k}-create' %}}" class="btn btn-outline-success mx-3 my-4 float-end"> &nbsp; Add Another Fact &nbsp; <i class="fa fa-plus"></i>
</a>
        """
        print(one_detail)
        all_my_details.append(one_detail)
    return all_my_details




######################### SQL scripts to GENERATE and POPULATE Database


# reads and saves MULTIPLE sheets from ONE excel sheet file 
def read_all_excel_sheets(file_path, sheet_list):
    """Returns a DICTIONARY containing key value pairs as follows:
    key: sheet_name
    value: a df containing all the data in the sheet
    """
    output_dfs = {}
    xls_full_file = pd.ExcelFile(file_path, engine='openpyxl')
    for sheet in sheet_list:
        output_dfs[sheet] = pd.read_excel(xls_full_file, sheet)
    
    return output_dfs

# reads and saves MULTIPLE sheets from ONE excel sheet file and saves them to a huge dataframe
def read_and_save_all_excel_sheets(file_path, sheet_list, output_dicts):
    """Returns a DICTIONARY containing key value pairs as follows:
    key: sheet_name
    value: a df containing all the data in the sheet
    """
    #output_dfs = {}
    xls_full_file = pd.ExcelFile(file_path, engine='openpyxl')
    for sheet in sheet_list:
        new_key = str(sheet)
        df = pd.read_excel(xls_full_file, sheet)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.dropna(axis = 0, how = 'all', inplace = True)
        #df = df.where(df.notnull(), None)
        output_dicts[new_key] = df
    
    return output_dicts


def read_and_save_all_excel_sheets_at_once(file_path_dics):
    """Returns a DICTIONARY containing key value pairs as follows:
    key: sheet_name
    value: a df containing all the data in the sheet
    """
    output_dics = {}
    for k, v in file_path_dics.items():
        output_dics[k] = read_and_save_all_excel_sheets(k, v, {})
    return output_dics