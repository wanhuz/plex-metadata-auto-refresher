import os
import datetime
from module.util import Util as util

class Walker:

    def __init__(self, src_folder):
        self.SRC_FOLDER = src_folder
    
    def get_new_directory(self, date : datetime.datetime):
        new_directory = util.filter_dir_by_date_modified(self.SRC_FOLDER, date)
        return new_directory

    def get_directory_with_new_subtitle(self, list_of_dir : list, exts: list, date : datetime.datetime):
        directory_with_new_subtitles = []
        for dir in list_of_dir:
            new_files = util.filter_file_by_date_created(os.path.join(self.SRC_FOLDER, dir), date)
            
            if util.contains_substring(exts, new_files):
                directory_with_new_subtitles.append(dir)

        return directory_with_new_subtitles