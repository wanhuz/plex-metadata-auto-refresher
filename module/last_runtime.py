import datetime
import os

class Last_runtime:

    def __init__(self):
        self.data_path = 'last_runtime.dat'

    def save(self) -> None:
        with open(self.data_path, 'w') as f:
            f.write(str(datetime.datetime.now()))

    def init(self) -> None:
        if (not (os.path.isfile(self.data_path))):
            self.save()

    def load(self) -> None:
        with open(self.data_path, 'r') as f:
            last_mod_date = f.readline()
        
        last_mod_date = datetime.datetime.strptime(last_mod_date, "%Y-%m-%d %H:%M:%S.%f")
        self.set(last_mod_date)

    def get(self) -> datetime.datetime:
        return self.CURRENT_LAST_RUNTIME

    def set(self, date: datetime.datetime) -> None:
        self.CURRENT_LAST_RUNTIME = date