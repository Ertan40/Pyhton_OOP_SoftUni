import math

class PhotoAlbum:

    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]  # [[], []]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / PhotoAlbum.PHOTOS_ON_A_PAGE))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_A_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        output = ["-----------"]
        for page in self.photos:
            output.append(("[] " * len(page)).rstrip())
            output.append("-" * 11)
        return '\n'.join(output)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
