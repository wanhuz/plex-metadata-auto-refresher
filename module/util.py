import os

class Util:
    
    @staticmethod
    def filter_list_by_file_exts(path_to_files : list, exts : list):
        temp_path_to_file = []
        
        for path in path_to_files:
            filename, file_extension = os.path.splitext(path)
            if file_extension in exts:
                temp_path_to_file.append(path)

        return temp_path_to_file
                 
    @staticmethod
    def parse_path_from_list(path_to_files : list):
        temp_path_to_file = []

        for path in path_to_files:
            path, filename = os.path.split(path)
            foldername = os.path.basename(path)
            if (foldername not in temp_path_to_file):
                temp_path_to_file.append(foldername)
        
        return temp_path_to_file
            
