"""Generate Markov text from text files."""

from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open("green-eggs.txt").read()

    return open_file 


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words_str = open_and_read_file("green-eggs.txt")
    words = words_str.split()
   

    chains = {}
   

    for idx in range(len(words)-2):
        bigram = (words[idx], words[idx + 1]) # give me a tuple 
        chains[bigram] = chains.get(bigram, []) + [words[idx+2]]

    return chains

dict = make_chains("green-eggs.txt")  

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])


    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return " ".join(words)


    # new_list = [] 

    # current_key = choice(list(chains.keys()))
    # list_of_values = chains[current_key]
    # third_word = choice(list_of_values)
    # second_word = current_key[1]

    # second_key = (second_word, third_word)

    # list_of_values_2 = chains[second_key]

    # rand_word = choice(list_of_values_2)

    # link = [second_word, third_word, rand_word] 



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
