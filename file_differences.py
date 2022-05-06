"""
Property of ayesha siddiqa. 
Date: May 6th, 2022
"""
import sys

def find_differences(file1, file2):
    """
    Produces two txt files that contains the differences found
    in file1 and in file2. Note that file1 and file2 are text files that contain emails
    and are not ordered.

    "txt_diff1.txt" is the text file produced that has emails present in file1 that
    are not present in file2.

    "txt_diff2.txt" is the text file produced that has emails present in file2 that
    are not present in file1.

    """
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    f3 = open('txt_diff1.txt', 'w')
    # contains emails found in file1 and not found in file2
    f4 = open('txt_diff2.txt', 'w')
    # contains emails found in file2 and not found in file1

    list_file1 = f1.readlines()
    dict1 = {} # this stores the lower case version of emails and the corresponding indices from list file1

    trie = TrieTree() # tree with emails of file1
    i = 0
    while i < len(list_file1):
        if list_file1[i].lower() not in dict1:
            trie.insert(list_file1[i].lower())
            dict1[list_file1[i].lower()] = [i]

        else:
            dict1[list_file1[i].lower()].append(i)
        i += 1
    list_file2 = f2.readlines()

    index = 0
    while index < len(list_file2):
        item = list_file2[index].lower()
        if item not in trie:
            f4.write(list_file2[index])
        else:
            # now we need to check if its in the dictionary, if it is then we pop from dict
            if item in dict1:
                del dict1[item]
        index += 1

    
    # now we write the remaining emails from the dict into txt_diff1
    for elements in list(dict1.values()):
        for items in elements:
            f3.write(list_file1[items])

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    return


class TrieTree:
    def __init__(self, char='', value= ''):
        '''
        Initializes:
            The node's char: self.char, ie. current character in the key
            The node's set of subtrees, 'children', using a dictionary
            The node's value, self.value  only set if it is a valid word in the dictionary
        '''
        self.value = value
        self.children = {}
        self.char = char

    def insert(self, word):
        '''
        Insert word into Trie tree
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> trie.insert("water")
        >>> "word" in trie
        True
        >>> "water" in trie
        True
        >>> "bob" in trie
        False
        '''
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieTree(ch)
            curr = curr.children[ch]
        curr.value = word
            
    def __contains__(self, key):
        '''
        Returns True if key is in tree, otherwise False
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> "word" in trie
        True
        >>> "other" in trie
        False
        '''
        curr = self
        for ch in key:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.value == key
            
find_differences(sys.argv[1], sys.argv[2])