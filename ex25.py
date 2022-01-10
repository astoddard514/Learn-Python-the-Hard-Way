def break_words(stuff):
    # Will be using documentation comments throughout this program.
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who

# >>> help(ex25)
# Help on module ex25:

# NAME
#     ex25

# FUNCTIONS
#     break_words(stuff)
#         This function will break up words for us.

#     print_first_and_last(sentence)
#         Prints the first and last words of the sentence.

#     print_first_and_last_sorted(sentence)
#         Sorts the words then prints the first and last one.

#     print_first_word(words)
#         Prints the first word after popping it off.

#     print_last_word(words)
#         Prints the last word after popping it off.

#     sort_sentence(sentence)
#         Takes in a full sentence and returns the sorted words.

#     sort_words(words)
#         Sorts the words.#

# >>> help(ex25.break_words)
# Help on function break_words in module ex25:

# break_words(stuff)
#     This function will break up words for us.

# can also say: from ex25 import *
# >>> from ex25 import *
# >>> sentence = " I love you. "
# >>> words = break_words(sentence)
# >>> words
# ['', 'I', 'love', 'you.', '']
# those spaces were taken as words in the list . . .