from pyhton_OOP.classes_and_objects.project2.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        else:
            already_in_album = False
            for x in self.songs:
                if x.name == song.name:
                    already_in_album = True
            if already_in_album:
                return f"Song is already in the album."
            else:
                self.songs.append(song)
                return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return f"Song is not in the album."
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."
        # if self.published:
        #     return "Cannot remove songs. Album is published."
        # for item in self.songs:
        #     if item.name == song_name:
        #         self.songs.remove(item)
        #         return f"Removed song {song_name} from album {self.name}."
        # return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]
        return '\n'.join(result)

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())