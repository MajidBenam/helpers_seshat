# old comma_value_maker
def human_readable_varname_from_dic(v):
    # input must be a dictionary
    if "varname" not in v.keys() or "dtype" not in v.keys():
        print("Invalid dictionary as input")
        return 0
    elif v["dtype"][0] in ["IntegerField", "PositiveBigIntegerField",]:
        return v["varname"] + "|intcomma"
    else:
        return v["varname"]

def importance_maker(v):
    if "importance" in v.keys():
        return v["importance"]
    else:
        return "NORMAL"

def underscore_to_space(mystr):
    spaced_value_list_0 = mystr.split("_")
    spaced_value_list = []
    for item in spaced_value_list_0:
        if len(item) >= 3 and item.lower() not in ["for", "and", "from", "the"]:
            spaced_value_list.append(item.capitalize())
        else:
            spaced_value_list.append(item)

    spaced_value = " ".join([myvalue for myvalue in spaced_value_list])
    return spaced_value
              
def col_heading_maker(heading, note, importance):
    # importance must be chosen carefully
    if importance == "HIGH":
        font_class = "fw-bold"
    elif importance == "LOW":
        font_class = "fw-light"
    else:
        font_class = "fw-normal"
    # note can be done carefully as well
    if note == "NOTHING":
        return f'''<th class = "{font_class}" style="text-align: center;" scope="col">{heading}</th>'''
    else:
        return f'''<th class = "{font_class}" style="text-align: center;" scope="col">{heading}
<sup>
<span type="button" data-bs-toggle="popover" data-bs-html="true" data-bs-content="{note}">&nbsp;<i class="fas fa-question-circle"></i></span>
</sup>
</th>'''

def inner_value_maker(actual_value, importance):
    """
    This will be used for the values that go inside the lists
    """
    # importance must be chosen carefully
    if importance == "HIGH":
        font_class = "fw-bold"
    elif importance == "LOW":
        font_class = "fw-light"
    else:
        font_class = "fw-normal"
                
    return f'''
<td class = "{{% if obj.tag == 'DSP' %}}
text-danger
{{% elif obj.tag == 'SSP' %}}
text-warning
{{% elif obj.tag == 'UNK' %}}
text-secondary
{{% elif obj.tag == 'IFR' %}}
text-primary
{{% else %}}
text-success
{{% endif %}} {font_class}" style="text-align: center;">{{{{ obj.{actual_value} }}}}
</td>'''
              
def main_description_maker(v):
    """
    This will be used for the descriptions to be shown on top of the pages.
    """
    if 'maindesc' in v.keys():
        main_descr = str(v['maindesc'])
        return f'''
<div class="row">
<p>
{main_descr}
</p>
</div>
'''
    else:
        return ""
    
def string_pluralizer_capitalizer(k):
    plural_form = k + 's'
    if k[-1] == "y":
        plural_form = k[:-1].capitalize() + "ies"
    if k[-1] == "x" or k[-1] == "z":
        plural_form = k.capitalize() + "es"
    if k[-1] == "s":
        plural_form = k.capitalize()
    return plural_form

def string_pluralizer(k):
    plural_form = k + 's'
    if k[-1] == "y":
        plural_form = k[:-1] + "ies"
    if k[-1] == "x" or k[-1] == "z":
        plural_form = k + "es"
    if k[-1] == "s":
        plural_form = k
    return plural_form

def has_any_uppercase(s):
    return any(ele.isupper() for ele in s)

def width_decider(form_variable, num_of_columns):
    if num_of_columns in [1,2,3]:
        div = 6
    elif num_of_columns == 4:
        div = 4
    elif num_of_columns == 5:
        div = 3
    else:
        div = 4
    return f'''
<div class="col-md-{div} mb-2">
{{{{ form.{form_variable}|as_crispy_field }}}}
</div>'''