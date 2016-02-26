#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a program that allows for an integer array to be passed in and will then
output all of the pairs that sum up to 10.  Please provide a solution that
allows for 1) output all pairs (includes duplicates and the reversed ordered
pairs), 2) output unique pairs only once (removes the duplicates but
includes the reversed ordered pairs), and 3) output the same
combo pair only once (removes the reversed ordered pairs). 

For example passing in [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9] the
following results should occur:
                     
1) output all pairs would output: [1,9], [1,9],
[4,6], [4,6], [5,5], [5,5], [5,5], [5,5],
[5,5], [5,5], [6,4], [6,4] [9,1] , [9,1] 
                                            
2) output unique pairs only once would output: 
[1,9], [4,6], [5,5],[6,4], [9,1] 
                                                        
3) output the same combo pair only once would output:
[1,9], [4,6], [5,5]
"""
from itertools import permutations

def get_all_pairs(array):
    # Naive way to show all pairs
    #array = sorted(array)
    for i in permutations(array, 2):
        if i[0] + i[1] == 10:
            print((i[0],i[1]))

def get_unique_pairs(array):
    pairs = []
    for elem in permutations(array, 2):
        if elem[0] + elem[1] == 10:
            pair = elem[0], elem[1]
            pairs.append(pair)
    # Using set() will handle uniqueness
    pairs = set(pairs)
    print(pairs)

def get_pairs_optimal(array, k):
    # Use a dictionary for fast lookup, should be near O(N)
    pairs = {}
    unique = []
    for i in range(len(array)):
        if array[i] in pairs:
            res = (array[i], pairs.get(array[i]))
            unique.append(res)
        else:
            pairs[k-array[i]] = i
    print(set(unique))

if __name__ == "__main__":
    array = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
    print('All pairs:')
    get_all_pairs(array)
    print('Unique pairs, not reversed:')
    get_unique_pairs(array)
    print('Same combo pairs, optimal:')
    get_pairs_optimal(array, 10)
