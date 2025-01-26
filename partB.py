import partA as A

def intersection_of_two_files(file1, file2):
    token_list1 = A.tokenize(file1)
    token_list2 = A.tokenize(file2)

    # print("token1", token_list1)
    # print("token2", token_list2)

    intersection = set(token_list1).intersection(set(token_list2))
    # print("intersection:", intersection, ", length is:", len(intersection))
    print(len(intersection))


if __name__ == '__main__':
    print("Part B Start")
    intersection_of_two_files("long1.txt", "long2.txt")
