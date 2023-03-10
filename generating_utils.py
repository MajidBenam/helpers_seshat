from crisisdb_vars import *
from helping_utils import *
import os
import pandas as pd
from datetime import date



################## General purpose:
def generate_vars_dic(vars_dic):
    vars_list_output = ["\nvars_dic = {"]
    for k, v in vars_dic.items():
        k_cap = k.capitalize()
        one_example = f"""\n'{k_cap}': {{\n\t'model': {k_cap},\n\t'list': {k_cap}ListView,\n\t'create': {k_cap}Create,\n\t}},\n"""
        vars_list_output.append(one_example)
    vars_list_output.append("}")
    vars_str_output = "".join(vars_list_output)
    with open("xyzzz.py", 'w') as f_d:
        f_d.write(str(vars_str_output))
    return str(vars_str_output)

def all_models_imports_generator(vars_dic):
    """
    This is actually generating the models, we can use it for other files as well.
    """
    output_str = "from .models import "
    list_of_models = []
    for k in vars_dic.keys():
        list_of_models.append(k.capitalize())
    return output_str + ', '.join(list_of_models)

def all_forms_imports_generator(vars_dic):
    output_str = "from .forms import "
    list_of_forms = []
    for k in vars_dic.keys():
        list_of_forms.append(k.capitalize()+"Form")
    return output_str + ', '.join(list_of_forms)

def generate_vars_dic_for_views(vars_dic):
    vars_dic_output = {}
    for k, v in vars_dic.items():
        k_cap = k.capitalize()
        #section_value = v.get('section')
        #subsection_value = v.get('subsection')
        vars_dic_output[k_cap] = {
            'model': k_cap + ",",
            'list': k_cap+"ListView,",
            'create': k_cap+"Create,",
            # it is now ingrained in the data dic we are putting in, but potentially we should dynamically read and update it.
            #'section': section_value,
            #'subsection': subsection_value,
        }
    return vars_dic_output


#######################

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
                if has_any_uppercase(v[key_str]["varname"]):
                    print("WARNING: variable ", k, " has uppercase letters in its variable name and it is not recommended")
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
        verbose_name_plural = '{plural_form.capitalize()}'

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
    all_my_serials = ["################ Beginning of Serializers Imports\n"]
    for k,v in vars_dic.items():
        plural_form = string_pluralizer(k)
        if has_any_uppercase(k):
            print("WARNING: variable ", k, " has uppercase letters in its name and it is not recommended")
            
        all_inner_vars = []
        for j in range(v['cols']):
            key_str = 'col' + str(j+1)
            all_inner_vars.append(v[key_str]["varname"])
            all_inner_vars_str = ("', '").join(all_inner_vars)
            
        one_serial = f"""
class {k.capitalize()}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {k.capitalize()}
        fields = ['year_from', 'year_to', '{all_inner_vars_str}', 'tag']
"""
        all_my_serials.append(one_serial)
    my_output = all_my_serials
        
    return my_output


def polity_serializer_generator(vars_dic):
    list_of_sers = []
    all_my_vars_related_friendly = ['id', 'name', 'start', 'end',]
    list_of_sers.append("class PolitySerializer(serializers.ModelSerializer):\n")
    for k in vars_dic.keys():
        my_meta_var = 'crisisdb_' + k + '_related'
        all_my_vars_related_friendly.append(my_meta_var)
        my_good_var = '\tcrisisdb_' + k.lower() + '_related' + ' = ' + k.capitalize() + 'Serializer' + '(many=True, read_only=True)\n'
        
        list_of_sers.append(my_good_var)
    #print(output_str + ', '.join(list_of_models))
    all_meta_vars_str = ("', '").join(all_my_vars_related_friendly)
    meta_string = f"""
\tclass Meta:
\t\tmodel = Polity
\t\tfields = ['{all_meta_vars_str}']
    """
    list_of_sers.append(meta_string)
    list_of_sers.append("\n################ End of Serializers Imports\n")
    return ''.join(list_of_sers)

########################### Forms
def form_generator(vars_dic):
    all_my_forms = []
    for k,v in vars_dic.items():
        rows_to_be_added_to_the_form = []
        widgets_to_be_added_to_the_form  = []
        for j in range(v['cols']):
            key_str = 'col' + str(j+1)
            raw_str_for_row = f"""fields.append('{v[key_str]["varname"]}')"""
            rows_to_be_added_to_the_form.append(raw_str_for_row)
            raw_str_for_widegts_1 = f"""widgets['{v[key_str]["varname"]}'] = forms.{v[key_str]["dtype"][1]}"""
            raw_str_for_widegts_2 = "(attrs={'class': 'form-control  mb-3', })"
            widgets_to_be_added_to_the_form.append(raw_str_for_widegts_1 + raw_str_for_widegts_1)
                
        form_rows = "\n        ".join([myvalue for myvalue in rows_to_be_added_to_the_form])
        form_widgets = "\n        ".join([myvalue for myvalue in widgets_to_be_added_to_the_form])
        
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

######################### URLS
def url_generator(vars_dic):
    all_my_urls = []
    for k,v in vars_dic.items():
        plural_form = string_pluralizer(k)
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
        
##################### ADMINS
def admin_generator(vars_dic):
    all_my_admins = ["from django.contrib import admin\n\n", all_models_imports_generator(vars_dic), '\n\n']
    for k,v in vars_dic.items():
        plural_form = string_pluralizer(k)
        one_admin = f"admin.site.register({k.capitalize()})\n"
        all_my_admins.append(one_admin)
    return all_my_admins

################ VIEWS

def view_generator(vars_dic):
    all_my_views = ['\n', all_models_imports_generator(vars_dic), '\n', all_forms_imports_generator(vars_dic)]
    for k,v in vars_dic.items():
        plural_form = string_pluralizer(k)
        my_vars_list = []
        for j in range(v['cols']):
            key_str = 'col' + str(j+1)
            a_good_var = v[key_str]['varname']
            my_vars_list.append(a_good_var)
        myvar = "\', \'".join(my_vars_list)
        myname = v['col1']['varname']
        myvalue = ", obj.".join(my_vars_list)
        #mysection = "No Section Provided"
        #mysubsection = "No Subsection Provided"
        #if 'section' in v.keys():
        #    mysection = v['section']
        #if 'subsection' in v.keys():
        #    mysubsection = v['subsection']
            
        one_view = f"""
class {k.capitalize()}Create(PermissionRequiredMixin, CreateView):
    model = {k.capitalize()}
    form_class = {k.capitalize()}Form
    template_name = "crisisdb/{k}/{k}_form.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        return reverse('{k}-create')
    def get_context_data(self, **kwargs):
        # get the explanattion:
        all_var_hiers = Variablehierarchy.objects.all()
        for item in all_var_hiers:
            if item.name == "{underscore_to_space(myname)}":
                my_exp = item.explanation
                my_sec = item.section.name
                my_subsec = item.subsection.name
                my_name = item.name
                break
            else:
                my_exp = "No_Explanations"
                my_sec = "No_SECTION"
                my_subsec = "NO_SUBSECTION"
                my_name = "NO_NAME"
        context = super().get_context_data(**kwargs)
        context["mysection"] = my_sec
        context["mysubsection"] = my_subsec
        context["myvar"] = my_name
        context["my_exp"] = my_exp

        return context


class {k.capitalize()}Update(PermissionRequiredMixin, UpdateView):
    model = {k.capitalize()}
    form_class = {k.capitalize()}Form
    template_name = "crisisdb/{k}/{k}_update.html"
    #permission_required = 'catalog.can_mark_returned'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "{underscore_to_space(myname)}"

        return context

class {k.capitalize()}Delete(PermissionRequiredMixin, DeleteView):
    model = {k.capitalize()}
    success_url = reverse_lazy('{plural_form}')
    template_name = "core/delete_general.html"
    #permission_required = 'catalog.can_mark_returned'


class {k.capitalize()}ListView(generic.ListView):
    model = {k.capitalize()}
    template_name = "crisisdb/{k}/{k}_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        return reverse('{plural_form}')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "{underscore_to_space(myname)}"

        return context
        
class {k.capitalize()}DetailView(generic.DetailView):
    model = {k.capitalize()}
    template_name = "crisisdb/{k}/{k}_detail.html"


#@permission_required('admin.can_add_log_entry')
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
    # add the vars_dic to be used in views.py
    all_my_views.append(generate_vars_dic(vars_dic))
    return all_my_views



##############################

####### Functions for Templates:
def templates_folder_make(k):
    foldername = k

    # Create the root folder (once)
    rootfolder = "output_templates"
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
        # files:
        full_name_list, full_name_detail, full_name_form, full_name_update = templates_folder_make(k)

        plural_form = string_pluralizer(k)
        myheadings = []
        form_second_row_var = []
        values_inside_the_list = []

        # all columns
        for j in range(v['cols']):
            key_str = 'col' + str(j+1)
            col_name = v[key_str]["varname"]
            spaced_value = underscore_to_space(col_name)
            with_comma_value = human_readable_varname_from_dic(v[key_str])
            importance_value = importance_maker(v[key_str])

            my_top_note = v[key_str].get('vardesc', "NO DESCRIPTION")
            heading_raw_str = col_heading_maker(spaced_value, my_top_note, importance_value)
            myheadings.append(heading_raw_str)
            if j == 0:
                # we might want to use a main column info
                main_col_header = spaced_value
                # the first col remains in the top row with a 4/12 col proportion (for forms and updates)
                form_first_row_var_str = f'''{{{{ form.{col_name}|as_crispy_field }}}}'''
                first_str_in_the_list = inner_value_maker(with_comma_value, importance_value)
                values_inside_the_list.append(first_str_in_the_list)
            else:
                # the other cols will be on the second, third etc row (for forms and updates)
                raw_str_for_second_row = width_decider(col_name, v['cols'])
                form_second_row_var.append(raw_str_for_second_row)
                raw_str_for_list = inner_value_maker(with_comma_value, importance_value)
                values_inside_the_list.append(raw_str_for_list)
                    
            # myheadings_str for both list and detail
            myheadings_str = "\n".join([myheading for myheading in myheadings])
            # for form and update pages
            form_second_row_var_str = "\n".join([myvalue for myvalue in form_second_row_var])
            # for list pages (and detail pages)
            myvalues_for_list_str = "\n".join([myvalue for myvalue in values_inside_the_list])
        
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
{myvalues_for_list_str}
{{% endblock extracols %}}
        '''
        print(one_detail)
        all_my_detail_templates.append(one_detail)
        
        
        one_form = f'''{{% extends "core/form_base.html" %}}
{{% load crispy_forms_tags %}}
{{% load humanize %}}

{{% block extra_vars %}}
    <div class="col-md-4 mb-2">
        {form_first_row_var_str}
    </div>
{{% endblock extra_vars %}}

{{% block extra_vars2 %}}
{form_second_row_var_str}
{{% endblock extra_vars2 %}}
        '''
        print(one_form)
        all_my_form_templates.append(one_form)
        one_update = f'''{{% extends "core/form_base.html" %}}
{{% load crispy_forms_tags %}}
{{% load humanize %}}

{{% block extra_vars %}}
    <div class="col-md-4 mb-2">
        {form_first_row_var_str}
    </div>
{{% endblock extra_vars %}}

{{% block extra_vars2 %}}
{form_second_row_var_str}
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


############################## SQL
######################### SQL scripts to GENERATE and POPULATE Database

# reads and saves MULTIPLE sheets from ONE excel sheet file and saves them to a huge dataframe
def read_and_save_an_excel_sheet(file_path, sheet_list):
    output_dicts = {}
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
        # the folder where we save our modified excel sheets:
        excel_folder = "excel_files/"
        file_path = excel_folder + str(k)
        output_dics[k] = read_and_save_an_excel_sheet(file_path, v)
    return output_dics

# READ CSV files
# we need to make sure that there is a match between the csv file col names and the vars_dic we are feeding this whole process with 
def read_and_save_a_csv_file(file_path, my_delimeter):
    output_dicts = {}
    df = pd.read_csv(file_path, delimiter=my_delimeter)
    new_key = str(file_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # Column names: remove white spaces and convert to lower case
    df.columns= df.columns.str.strip().str.lower()
    # ALTERNATIVELY: 	
    # df = df.rename(columns=str.lower)
    # we have to replace any empty strings in the df with np.nan objects
    # df['ABC'].replace('', np.nan, inplace=True)
    # before can drop null values
    # df.dropna(subset=['ABC'], inplace=True)
    df.dropna(axis = 0, how = 'all', inplace = True)
    #df = df.where(df.notnull(), None)
    output_dicts[new_key] = df
    
    return output_dicts


def read_and_save_all_csv_files_at_once(file_path_dics, my_delimeter):
    """Returns a DICTIONARY containing key value pairs as follows:
    key: csv_file_name
    value: a df containing all the data in the sheet
    So the data will be totally in the inner dataframe,
    but we should be 100% sure that it is valid data.
    """
    output_dics = {}
    for k, v in file_path_dics.items():
        # the folder where we save our modified csv sheets:
        csv_folder = "csv_files/"
        file_path = csv_folder + str(k)
        output_dics[k] = read_and_save_a_csv_file(file_path, my_delimeter)
    return output_dics


#######################    SQL actual generator

def good_columns_selector(list_of_columns):
    """
    Decides on good columns
    """
    bad_cols = ["year_from", "year_to", "PolID", "section",'note',
                'source', 'sources', 'description', 'citation', 'data_source']
    # will keep the list of all good columns
    my_selected_cols = []
    #df["year_from"] = df["year_from"].astype("int64")
    for item in list_of_columns:
        if item not in bad_cols:
            my_selected_cols.append(item)

    return my_selected_cols

def polity_id_decider(my_df, my_row):
    """
    Decides on the Polity ID
    TODO: Make it dynamic or make it unchangeably static by attaching te polity creation to sql generations
    """
    polity_id = 3
    if my_df['year_from'][my_row].astype('int64') >= 1795:
        polity_id = 4

    return polity_id

# I need to decide on the main model name if there are multiple columns in one csv file
def model_name_for_multi_column_models(list_of_columns):
    model_name = 'MYBADMAINCOLUMN'
    for mycol in list_of_columns:
        if "MAINCOLUMN" in mycol:
            model_name = mycol
    return model_name 

def sql_generator_for_all(my_files_dic, my_good_dfs):
    for my_key, my_v in my_files_dic.items():
        # build df
        for my_sheet in my_v:
            df = my_good_dfs[my_key][my_sheet]
            #df = df_old.where(pd.notnull(df), None)
            sheet = str(my_key) + str(my_sheet)
            sql_list_of_strings = []
            list_of_columns = df.columns.values.tolist()
            selected_list = good_columns_selector(list_of_columns)

            #  we go through each row of the spread sheet to make one (or several) model instances
            # Mullti Column Models Available in one Sheet
            if "PROBLEMATIC" in str(my_sheet):
                # Ignore this sheet
                continue
            if 'MCMA' in str(my_sheet):
                MCMA_list_of_vars = ', '.join(selected_list)
                model_name = model_name_for_multi_column_models(list_of_columns)
                for row in range(df.shape[0]):
                    polity_id = polity_id_decider(df, row)
                    spaced_name = underscore_to_space(model_name)
                    year_from_df = df['year_from'][row].astype('int64')
                    year_to_df = df['year_from'][row].astype('int64')
                    if 'year_to' in list_of_columns:
                        year_to_df = df['year_to'][row].astype('int64')
                    MCMA_list_of_values = []
                    if "note" in list_of_columns:
                        mynote = "\'" + str(df["note"][row]) + "\'"
                    else:
                        mynote = "NULL"
                    
                    for column in selected_list:
                        #print('here we go', df[column].dtypes)
                        #MCMA_list_of_types.append(str(df[column].dtypes))
                        if str(df[column].dtypes) == 'object':
                            to_be_appended = "\'" + str(df[column][row]) + "\'"
                            MCMA_list_of_values.append(to_be_appended)
                        else:
                            MCMA_list_of_values.append(str(df[column][row]))
                            
                    MCMA_list_of_values_str = ', '.join(MCMA_list_of_values)
                    sql_line = f"INSERT INTO crisisdb_{model_name} (polity_id, year_from, year_to, {MCMA_list_of_vars}, finalized, tag, name, note, created_date) VALUES ({polity_id}, {year_from_df}, {year_to_df}, {MCMA_list_of_values_str}, True, 'TRS', '{spaced_name}', {mynote},'{date.today()}');"
                    # replace "nan" with NULL
                    better_sql_line = sql_line.replace("\'nan\'", "NULL")
                    best_sql_line = better_sql_line.replace(" nan,", " NULL,")
                    
                    sql_list_of_strings.append(best_sql_line)
                
            # Each column represents a Model
            else:   
                for row in range(df.shape[0]):
                    # we go through all the columns for the cases when each column is a separate model
                    for column in selected_list:
                        if column == "note":
                            continue
                        else:
                            polity_id = polity_id_decider(df, row)
                            spaced_name = underscore_to_space(column)

                            if str(df[column].dtypes) == 'object':
                                myvarsql_value = "\'" + str(df[column][row]) + "\'"
                            elif str(df[column].dtypes) == 'int64':
                                myvarsql_value = str(df[column][row].astype('int64'))
                            elif str(df[column].dtypes) == 'float64':
                                myvarsql_value = str(df[column][row].astype('float64'))
                                #myvarsql_value = str(df[column][row].astype('float64'))
                            else:
                                myvarsql_value = str(df[column][row])
                            
                            if "note" in list_of_columns:
                                mynote = "\'" + str(df["note"][row]) + "\'"
                            else:
                                mynote = "NULL"
                            myvarsql = vars_dic[column]["col1"]["varname"]
                            year_from_df = df["year_from"][row].astype('int64')
                            year_to_df = df['year_from'][row].astype('int64')
                            if 'year_to' in list_of_columns:
                                year_to_df = df['year_to'][row].astype('int64')
                            #df[column].where(df[column].notnull(), None)
                            if pd.isna(df[column][row]):
                                sql_line = f"INSERT INTO crisisdb_{column} (polity_id, year_from, year_to, note, {myvarsql}, finalized, tag, name, created_date) VALUES ({polity_id}, {year_from_df}, {year_to_df}, {mynote}, NULL, True, 'TRS', '{spaced_name}', '{date.today()}');"
                            else:
                                sql_line = f"INSERT INTO crisisdb_{column} (polity_id, year_from, year_to, note, {myvarsql}, finalized, tag, name, created_date) VALUES ({polity_id}, {year_from_df}, {year_to_df}, {mynote}, {myvarsql_value}, True, 'TRS', '{spaced_name}', '{date.today()}');"
                            # replace "nan" with NULL
                            better_sql_line = sql_line.replace("\'nan\'", "NULL")
                            best_sql_line = better_sql_line.replace(" nan,", " NULL,")
                    
                            sql_list_of_strings.append(best_sql_line)
            sql_file_name = "all_sql_files/"+sheet+".sql"

            with open(sql_file_name , "w") as sql_file:
                for l in sql_list_of_strings:
                    sql_file.write(l)
                    sql_file.write("\n")
            #print(my_str_dic)
    