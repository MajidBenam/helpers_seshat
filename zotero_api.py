
"""
- pip install pyzotero or conda config --add channels conda-forge && conda install pyzotero
- You'll need the ID of the personal or group library you want to access:
Your personal library ID is available here, in the section Your userID for use in API calls
For group libraries, the ID can be found by opening the group's page: https://www.zotero.org/groups/groupname, and hovering over the group settings link. The ID is the integer after /groups/
You'll also need† to get an API key here
Are you accessing your own Zotero library? library_type is 'user'
Are you accessing a shared group library? library_type is 'group'.

"""

# api_hint = fordjango1483101
# api_key = VF5X3TCC3bUYov8Au5gCHf3a
from pyzotero import zotero
zot = zotero.Zotero(1051264, 'group', 'VF5X3TCC3bUYov8Au5gCHf3a')
items = zot.top(limit=500)
# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    #print(item)
    try:
        print('Item: %s | Key: %s | Main cretaor: %s | year: %s | Title: %s'  % (item['data']['itemType'], item['data']['key'], item['data']['creators'][0]['lastName'], item['data']['date'], item['data']['title']))
    except:
        print("No creator")