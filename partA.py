import re

def tokenize(text_file_path: str) -> list:
    """
    Runtime Complexity: TODO

    Reads in a text file and returns a list of tokens in that file.
    For the purpos of this project, a token is a sequence of alphanumeric characters, independent of capitalization.

    :param text_file_path: Path to the text file to be read.
    :return: List of the tokens in that file.
    """
    token_list = []
    with open(text_file_path, mode='r', encoding='utf-8') as file:
        for line in file:

            line = line.lower()
            # print("line: ", line)

            # divide all the words in the line into token alphanumeric
            regex = r"([a-zA-Z0-9]+)"
            token = re.findall(regex, line)
            # print("token: ", token)

            # add the token to the token_list
            token_list.extend(token)

    # return the list of tokens
    return token_list



def compute_word_frequency(tokens: list) -> dict:
    """
    Runtime Complexity: TODO

    Counts the numbers of accurrences of each token in the token list.
    Must write this from scratch

    :param tokens: List of tokens.
    :return: disct, mapping each taken to the number of accurrences.
    """

    # Token Dictionary, that takes word as a key, count as a value.
    token_dict = {}

    # If the token exist in the dictionary, put the token in the key, and add the value.
    for i in range(len(tokens)):
        if tokens[i] not in token_dict:
            token_dict[tokens[i]] = 1
        else:
            token_dict[tokens[i]] += 1

    return token_dict

def print_frequencies(frequencies: dict) -> None:
    """
    Runtime Complexity: TODO

    TODO Chose one of the output formats to print the results
    <token>\t<freq>
    <token> <freq>
    <token> - <freq>
    <token> = <freq>
    <token> > <freq>
    <token> -> <freq>
    <token> => <freq>

    :param frequencies: dict, mapping each token to the number of accurrences.
    """

    # With the given dictionary 'frequencies', print key-value.
    for key, value in frequencies.items():
        print(key,"-",value)

"""
if __name__ == '__main__':
    print("Part A Start")
    token1 = tokenize("long2.txt")
    compute = compute_word_frequency(token1)
    print_frequencies(compute)
"""