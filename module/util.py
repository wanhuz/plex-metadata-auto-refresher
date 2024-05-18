import os
import datetime

class Util:

    @staticmethod
    def filter_dir_by_date_modified(src_folder, archive_date):
        return [
            name for name in os.listdir(src_folder)
            if os.path.isdir(os.path.join(src_folder, name))
            and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(src_folder, name))) > archive_date
        ]
    
    @staticmethod
    def filter_file_by_date_created(src_folder, archive_date):
        return [
            name for name in os.listdir(src_folder)
            if os.path.isfile(os.path.join(src_folder, name))
            and datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(src_folder, name))) > archive_date
        ]

    @staticmethod
    def contains_substring(substrings, strings):
        for string in strings:
            if any(sub in string for sub in substrings):
                return True

        return False
                 