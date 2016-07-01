class Song:
    '''A Song class.'''

    def __init__(self, single_string):
        '''(Song, string) -> None
        A new Song with title, artist, duration from single_string
        '''

        string_list = single_string.strip().split("<SEP>")
        self.title = string_list[1]
        self.artist = string_list[0]
        self.duration = string_list[2]

    def __str__(self):
        '''(Song) -> str
        Return string in the form "artist - title (duration)"
        '''

        return "{} - {} ({})".format(self.artist, self.title, self.duration)

    def __eq__(self, other):
        '''(Song, object) -> bool
        Return True Iff the song's title, artist and duration are all equal.
        '''

        return (self.title == other.title) and (self.artist == other.artist)\
               and (self.duration == other.duration)

    def __ne__(self, other):
        '''(song, object) -> bool
        Return True iff the song's title, artist and duration are not all equal
        '''

        return not self.__eq__(other)


class Pair:
    ''' A Pair class.'''

    def __init__(self, key, obj):
        '''(Pair, string, object) -> None
        A new Pair with value, key and data
        '''

        self.key = key
        self.data = obj

    def __str__(self):
        '''(Pair) -> string
        Return string representation of the Pair's data
        '''

        return "{}".format(self.data)

    def __lt__(self, other):
        '''(Pair, object) -> bool
        Return True iff lowercase of key value of self is less than
        lowercase of key value of other.
        '''

        return self.key.lower() < other.key.lower()

    def __gt__(self, other):
        '''(Pair, object) -> bool
        Return Ture iff lowercase of key value of self is greater than
        lowercase of key value of other.
        '''

        return self.key.lower() > other.key.lower()

    def __eq__(self, other):
        '''(Pair, object) -> bool
        Return True iff the lowercase of key value of self is equal to the
        lowercase of key value of other and their data objects are equal.
        '''

        return (self.key.lower() == other.key.lower())\
               and (self.data == other.data)

    def __ne__(self, other):
        '''(Pair, object) -> bool
        Return True iff the lowercase of key value of self is not equal to the
        lowercase of key value of other and their data objects are not equal.
        '''

        return not self.__eq__(other)

    def __ge__(self, other):
        '''(Pair, object) -> bool
        Return Ture iff lowercase of key value of self is greater than or equal
        to lowercase of key value of other.
        '''

        return self.key.lower() >= other.key.lower()

    def __le__(self, other):
        '''(Pair, object) -> bool
        Return True iff lowercase of key value of self is less than or equal to
        lowercase of key value of other.
        '''

        return self.key.lower() <= other.key.lower()
