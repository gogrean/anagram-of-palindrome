"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?
    
    If the word is an anagram of a palindrome, each letter except at
    most one will appear an even number of times. The function counts
    the number of times each letter appears in the word and stores the
    count in a dictionary, then sums up the remainders of dividing each
    count by 2. If the sum is greater than one, more than one letter 
    appears an odd number of times, and then the word is not the 
    anagram of a palindrome.
    """
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    num_oddly_appearing_letters = sum([letter_count[letter] % 2 for letter in letter_count])
    return num_oddly_appearing_letters <= 1


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
