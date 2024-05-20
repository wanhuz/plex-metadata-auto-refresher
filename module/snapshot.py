import os
from dill import dump, load
from watchdog.utils import dirsnapshot

class Snapshot:

    def __init__(self, src_dir):
        self.data_path = 'last_snapshot.dat'
        self.src_dir = src_dir

    def save(self, snapshot) -> None:
        with open(self.data_path, 'wb') as snapshot_f:
            dump(snapshot, snapshot_f)

    def init(self) -> None:
        if (not (os.path.isfile(self.data_path))):
            self.save(self.create())

    def load(self) -> None:
        with open(self.data_path, 'rb') as snapshot_f:
            old_snapshot = load(snapshot_f)

        self.set(old_snapshot)

    def create(self) -> None:
        return dirsnapshot.DirectorySnapshot(self.src_dir)

    def get_modified_file(self, new_snapshot : dirsnapshot.DirectorySnapshot):
        modified_files = []
        snapshot_changes = dirsnapshot.DirectorySnapshotDiff(self.snapshot, new_snapshot)

        if (snapshot_changes.files_created):
            for file in snapshot_changes.files_created:
                modified_files.append(file)
        
        if (snapshot_changes.files_deleted):
            for file in snapshot_changes.files_deleted:
                modified_files.append(file)
        
        return modified_files

    def set(self, snapshot: dirsnapshot.DirectorySnapshot) -> None:
        self.snapshot = snapshot