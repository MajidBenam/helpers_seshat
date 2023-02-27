# new functions
# with static section and subsections removed
def QingVars(request):
    context = {}
    mylist = []
    # create an empty dic for sections and subsections:
    ultimate_dic = {'Unnamed Section': {'Unnamed Subsection': []}}
    for k, v in vars_dic.items():
        inner_list = []

        spaced_value_list_0 = k.split("_")
        spaced_value_list = []
        for item in spaced_value_list_0:
            if len(item) >= 3 and item.lower() not in ["for", "and", "from", "the"]:
                spaced_value_list.append(item.capitalize())
            else:
                spaced_value_list.append(item)

        spaced_value = " ".join([myvalue for myvalue in spaced_value_list])
        inner_list.append(spaced_value)
        inner_list.append(v['model'].objects.count())
        list_link = v['list']()
        inner_list.append(list_link.get_absolute_url())
        create_link = v['create']()
        inner_list.append(create_link.get_absolute_url())
        ultimate_dic['Unnamed Section']['Unnamed Subsection'].append(inner_list)

    context["mylist"] = ultimate_dic
    return render(request, 'crisisdb/qing-vars.html', context=context)

def playground(request):
    if request.method == "POST":
        print(request.POST.get("selected_pols", 'Hallo'))
    all_pols = list_of_all_Polities()
    all_vars = dic_of_all_vars_with_varhier()
    all_vars_plus = dic_of_all_vars_in_sections()
    context = {'allpols': all_pols, 'all_var_hiers': all_vars, 'crisi': all_vars_plus}
    return render(request, 'crisisdb/playground.html', context=context)

Tags_dic = {
    'TRS': 'Evidenced',
    'DSP': 'Disputed',
    'SSP': 'Suspected',
    'IFR': 'Inferred',
    'UNK': 'Unknown',
}

@permission_required('admin.can_add_log_entry')
def playgrounddownload(request):
    checked_pols = request.POST.getlist("selected_pols")
    print("The checked politys are:", checked_pols)

    checked_vars = request.POST.getlist("selected_vars")
    print("The checked vars are:", checked_vars)

    new_checked_vars = ["crisisdb_" + item.lower() + '_related' for item in checked_vars]
    print("The modified checked vars are:", new_checked_vars)

    checked_separator = request.POST.get("SeparatorRadioOptions")
    print("The checked separator are:", checked_separator)

    if checked_separator == "comma":
        checked_sep = ","
    elif checked_separator == "bar":
        checked_sep = "|"
    else:
        print("Bad selection of Separator.")

    #url = "http://127.0.0.1:8000/api/politys/"
    url = "https://www.majidbenam.com/api/politys/"
    #url = settings.MY_CURRENT_SERVER + "/api/politys/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']

    final_response = HttpResponse(content_type='text/csv')
    now = datetime.datetime.now()
    now_str = now.strftime("%H%M%S")
    myfile_name = 'CrisisDB_data_' + str(request.user) + '_' + now_str
    final_response['Content-Disposition'] = f'attachment; filename="{myfile_name}.csv"'

    writer = csv.writer(final_response, delimiter=checked_sep)
    # the top row is the same as Equinox, so no need to read data from user input for that
    writer.writerow(['polity', 'variable_name', 'variable_sub_name', 'value',
                     'year_from', 'year_to', 'certainty', 'references', 'notes'])

    for polity_with_everything in all_my_data:
        if polity_with_everything['name'] not in checked_pols:
            continue
        else:
            for variable in new_checked_vars:
                if variable not in polity_with_everything.keys():
                    continue
                else:
                    # we can get into a list of dictionaries
                    for var_instance in polity_with_everything[variable]:
                        all_inner_keys = var_instance.keys()
                        # print(all_inner_keys)
                        all_used_keys = []
                        for active_key in all_inner_keys:
                            if active_key not in ['year_from', 'year_to', 'tag'] and active_key not in all_used_keys:
                                an_equinox_row = []
                                an_equinox_row.append(
                                    polity_with_everything['name'])
                                an_equinox_row.append(
                                    variable[:-8])
                                an_equinox_row.append(
                                    active_key)
                                an_equinox_row.append(
                                    var_instance[active_key])
                                all_used_keys.append(active_key)
                                an_equinox_row.append(
                                    var_instance['year_from'])
                                an_equinox_row.append(
                                    var_instance['year_to'])
                                full_tag = Tags_dic[var_instance['tag']]
                                an_equinox_row.append(full_tag)
                                writer.writerow(an_equinox_row)


    return final_response
