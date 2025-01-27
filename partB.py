import sys

import partA as A

def intersection_of_two_files(file1, file2):
    token_list1 = A.tokenize(file1)
    token_list2 = A.tokenize(file2)

   # print("type: ", type(token_list1), "token1: ", token_list1)
   # print("token2", token_list2)
    """
    intersection = set(token_list1).intersection(set(token_list2))
    # print("intersection:", intersection, ", length is:", len(intersection))
    # I have referred for intersection: https://lungfish.tistory.com/entry/python-%EB%91%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B5%90%EC%A7%91%ED%95%A9-%ED%95%A9%EC%A7%91%ED%95%A9-%EC%B0%A8%EC%A7%91%ED%95%A9
    print(len(intersection))
    """

    token_set1 = set(token_list1)
    token_set2 = set(token_list2)
    count = 0
    for i in token_set1:
        if i in token_set2:
            count += 1

 #   print(count)
    return count


if __name__ == '__main__':
   # intersection_of_two_files(sys.argv[1], sys.argv[2])
    print(intersection_of_two_files(sys.argv[1], sys.argv[2]))