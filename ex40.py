
class Song(object):
    
    # this now exists
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    # this is a Song function to print lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# new song variables using class, passing lists of strings as lyrics
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# call song function for each of our song variables
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()