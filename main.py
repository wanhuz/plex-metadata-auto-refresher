from module.plex import Plex
from module.snapshot import Snapshot as DirSnapshot
from module.util import Util
from yaml import safe_load as yaml_safe_load
import schedule
from sys import exit
import time

try:
    with open('config.yaml', 'r') as file:
        config = yaml_safe_load(file)
except IOError:
    exit('Config.yaml file could not be found. Create yaml file using config_example.yaml')

baseurl = config['plex']['url']
token = config['plex']['x-token']
library = config['plex']['library']
src_folder = config['user']['folder_to_watch']
exts = config['user']['extension_to_watch']

plex = Plex(baseurl, token, src_folder, library)
plex.authenticate()
print('Authenticated to Plex')


def job():
    snapshot = DirSnapshot(src_folder)
    snapshot.init()
    snapshot.load()

    new_snapshot = snapshot.create()
    changed_file = snapshot.get_modified_file(new_snapshot)
    
    file_to_refresh = Util.filter_list_by_file_exts(changed_file, exts)
    print('Detecting file to refresh ' + str(changed_file))

    directory_to_refresh = Util.parse_path_from_list(file_to_refresh)
    print("Directory to refresh since last snapshot " + str(directory_to_refresh))

    if (directory_to_refresh):
        snapshot.save(snapshot.create())

        print('Retrieving shows from Plex to refresh...')
        items_to_refresh = plex.get_item_from_location(directory_to_refresh)

        print('Refreshing shows ' + str(items_to_refresh))
        plex.refresh_items(items_to_refresh)
        print('Operation complete!')
    else:
        print('Nothing to refresh')

job()
schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
