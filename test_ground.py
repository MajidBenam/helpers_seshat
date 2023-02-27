from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import os
import csv
import re
import bs4
import json
#import time

def list_of_items_to_html(my_list_of_items, 
                        my_online_base_address,
                        my_local_address,
                        my_prefix="full_",
                        my_suffix=".html"):
    """
    - Goes through a list of items that we know of (valid links) and saves them to my_local_address
    - (local address must have the rtrailing slash)
    - the local address doe not have to be made beforehand. The code checks for it.
    - The base addres: my_online_address
    - each item in my_list_of_items will get concatenated to my_online_address to form a vlaid link:
    INPUTS: (list, str, str, [str], [str]) 
    """
    for item in my_list_of_items:
         # a potential value: 'https://seshat.info/w/index.php?title='
        source_url = my_online_base_address + str(item)
        # cool trick
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        # the needed source to be used in beautiful soup.
        source = requests.get(source_url, headers=headers)
        #source = requests.get(source_url, headers=headers).text

        # form the soup, using source and lxml
        #soup = html.fromstring(source)
        soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')

        # get the full html content of the soup (in string):
        html_content = str(soup)
        # create the folder(s) if it (they) does (do) not exist
        if not os.path.exists(my_local_address):
            os.makedirs(my_local_address)
        my_file_address = my_local_address + my_prefix + item + my_suffix
        with open (my_file_address, "w") as f:
            f.write(html_content)


def json_of_refs_in_seshatdatabank(my_list_of_items,
                        my_local_address,
                        my_online_base_address='http://seshatdatabank.info/browser/',
                        my_json_file="seshat_refs.json"):
    """
    - Goes through a list of items that we know of (valid seshat links)
    - and saves the references at the end of those pages into TWO json file in my_local_address
    - (local address must have the rtrailing slash):
    - JSON1: all refs
    - JSON2: all unique_refs
    - the local address doe not have to be made beforehand. The code checks for it.
    - The base addres: my_online_address
    - each item in my_list_of_items will get concatenated to my_online_address to form a vlaid link:
    INPUTS: (list, str, str, [str]) 
    """
    big_dic_of_references = {}
    unique_references = {}
    for item in my_list_of_items:
         # a potential value: 'https://seshat.info/w/index.php?title='
        source_url = my_online_base_address + str(item)
        # cool trick
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        # the needed source to be used in beautiful soup.
        source = requests.get(source_url, headers=headers)

        # form the soup, using source and lxml
        soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')

        # get the full html content of the soup (in string):
        html_content = str(soup)

        main_text_with_references = soup.find_all('span', class_ = 'reference-text')        
        # dic that will save a dictionary for each polity, keeping all the records.
        big_dic_of_references[item] = {}
        for my_ref in main_text_with_references:
            inside_href_messy = my_ref.find_previous('a')['href']
            inside_number_neat = inside_href_messy.split('-')[1]
            # the first occurrence of our unique reference
            key_for_unique_ref = item + '_' + str(inside_number_neat)
            if my_ref.text not in unique_references.values():
                unique_references[key_for_unique_ref] = my_ref.text
            big_dic_of_references[item][key_for_unique_ref] = my_ref.text

        if not os.path.exists(my_local_address):
            os.makedirs(my_local_address)
        my_file_address = my_local_address + my_json_file
        my_file_address_unique = my_local_address + "unique_" + my_json_file
        with open(my_file_address, "w") as my_jsonfile:
            json.dump(big_dic_of_references, my_jsonfile)
        with open(my_file_address_unique, "w") as my_u_jsonfile:
            json.dump(unique_references, my_u_jsonfile)
