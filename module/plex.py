from plexapi.server import PlexServer

class Plex:

    def __init__(self, base_url, x_token, src_folder, library):
        self.BASE_URL = base_url
        self.X_TOKEN = x_token
        self.SRC_FOLDER = src_folder
        self.LIBRARY = library

    def authenticate(self):
        self.Plex = PlexServer(self.BASE_URL, self.X_TOKEN)

    def get_item_from_location(self, locations: list) -> list:
        items_to_refresh = []
        items = self.Plex.library.section(self.LIBRARY)
        items = items.all()

        for item in items:
            for item_location in item.locations:
                if any(location in item_location for location in locations):
                    items_to_refresh.append(item)
        
        return items_to_refresh

    def refresh_items(self, items_to_refresh : list) -> None:
        for item in items_to_refresh:
            item.refresh()