"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    #create empty dictionary for the count_words funciton to store data
    print_dict = {}
    #use for loop to iterate over phrase to split string of words into individual
    #strings
    for word in phrase.split():
    # if statement to see if word already exists as a key, and if not, to create
    # a new key.
        if word in print_dict.keys():
            print_dict[word] = print_dict[word] + 1
        else:
            print_dict[word] = 1
    return print_dict


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    # creating the melon dictionary ( I KNOW IT'S A GENERIC NAME lol)
    melon_dict = { 
                    'Watermelon': 2.95,
                    'Cantaloupe': 2.50,
                    'Musk': 3.25,
                    'Christmas': 14.45
    }
    # if statement to check whether the melon inputted by user is within the
    # dictionary. If it is, the value / price will be returned, if not,
    # the user will get a message saying 'no price found'
    if melon_name in melon_dict.keys():
        return melon_dict[melon_name]
    else:
        return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # created a dictionary to hold the length of words and words
    # with the length as a key and the words in lists as values
    word_lengths = {}

    # for word in inputted list of words, if the length of the word is not set 
    # as a key in the dictionary, then add the length with associated key
    # else add the word to the value list associated with the key/ length of word
    for word in words:
        if len(word) not in word_lengths.keys():
            word_lengths[len(word)] = [word]
        else:
            word_lengths[len(word)].append(word)
    # created an empty list to store keys and values after using method 
    # .iteritems()
 
    list_of_lengths = []
    # for each key, value in the dicitonary word_lengths    
    # iteritems() to return an object (tuple in our case) and we can iterate over
    # the tutples 
    for key, value in word_lengths.iteritems():
        #add the keys and sorted values to this list 
        list_of_lengths.append((key, sorted(value)))
    return list_of_lengths
    return []


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # created a dictionary with english words as keys and pirate slang as values
    pirate_dictionary = {
                            'sir': 'matey',
                            'hotel': 'fleabag inn',
                            'student': 'swabbie',
                            'man': 'matey',
                            'professor': 'foul blaggart',
                            'restaurant': 'galley',
                            'your': 'yer',
                            'excuse': 'arr',
                            'students': 'swabbies',
                            'are': 'be',
                            'restroom': 'head',
                            'my': 'me',
                            'is': 'be'
    }

    # defining a variable to split the phrase inputted by user
    word_list = phrase.split()
    # created an empty list
    pirate_translation = []


    # using for loop to iterate over the string split into individual words
    for word in word_list:
    # if statement to check if word is a key in the pirate dictionary I created
    # as to translate into pirate jargon
        if word in pirate_dictionary.keys():
            # if word is, add word to the pirate_transaltion list using the 
            # value associated with the pirate dictionary -- that being the
            # pirate term
            pirate_translation.append(pirate_dictionary[word])
        else:
            # else just add the word into the list of pirate_translation as itself
            pirate_translation.append(word)

    # create string out of list with translated workd using .join() method,
    # seperating with a space " "
    pirate_translation = " ".join(pirate_translation)

    return pirate_translation



def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    # definitely couldn't even think of how to start, decided to focus on
    # OO assessment - will come back to it when I've got time !!!! 

    return []

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
