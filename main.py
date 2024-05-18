from module.plex import Plex
from module.walker import Walker
from module.last_runtime import Last_runtime as Runtime_Date
from yaml import safe_load as yaml_safe_load


with open('config.yaml', 'r') as file:
    config = yaml_safe_load(file)

baseurl = config['plex']['url']
token = config['plex']['x-token']
library = config['plex']['library']
src_folder = config['user']['folder_to_watch']
exts = config['user']['extension_to_watch']

plex = Plex(baseurl, token, src_folder, library)
plex.authenticate()
print('Authenticated to Plex')

walker = Walker(src_folder)

runtime_date = Runtime_Date()
runtime_date.init()
runtime_date.load()
last_runtime_date = runtime_date.get()
print("Last script running is " + str(last_runtime_date))

new_modified_directory = walker.get_new_directory(last_runtime_date)
print("Modified directory since last run " + str(new_modified_directory))

directory_to_refresh = walker.get_directory_with_new_subtitle(new_modified_directory, exts, last_runtime_date)
print("Directory to refresh since last run " + str(directory_to_refresh))

runtime_date.save()

if (directory_to_refresh):
    items_to_refresh = plex.get_item_from_location(directory_to_refresh)

    print('Refreshing shows ' + str(items_to_refresh))
    plex.refresh_items(items_to_refresh)
    print('Operation complete!')
else:
    print('Nothing to refresh')