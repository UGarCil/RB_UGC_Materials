    # -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:25:03 2021

@author: Uriel
"""

# Binary tree

# Binary tree (BT) works with recursion of two subsets of original data.
# (DD) Data definition:
# BT has:
#  - pivot
#  - left BT
#  - right BT

# bt ([1]) #stub

# EXAMPLES:
# bt([3,1]) = [1,3]
# bt([3,1,6,4]) = [1,3,4,6]

# (FD) Function definition
# def bt(lon):
#   if trivial_case:
#     return []
#   else:
#     result = (bt(fn-left-reduction) 
#              + [pivot]
#             + bt(fn-right-reduction))
#   return result


# APPLICATION
myNumbers = [6,3,1,7,8,9]

def lessthanpivot(sourceList, p):
    sub_s = []
    for n in sourceList:
        if n < p:
            sub_s.append(n)
    return sub_s

def morethanpivot(sourceList, p):
    sub_s = []
    for n in sourceList:
        if n > p:
            sub_s.append(n)
    return sub_s

    

final_list = []
# a = array

def bt(a):
    if len(a) == 0:
        return []
        
    else:
        pivot = a[0]
        # create sublist with items to the left of pivot
        # create sublist with items to right of pivot
        final_list = (bt(lessthanpivot(a, pivot))+[pivot]+bt(morethanpivot(a, pivot)))
    return final_list
        
bt(myNumbers)


# APPLYING BT INTO NEWICK FORMATTING AND PHYLOGENETIC TREES
# def phylogeny(soi, _s_):
#     if "," not in soi:
#         _s_ += soi
#         return _s_
#     else:
#         pivot = findMidComma(soi)
#         print(f"left is {soi[1:pivot]}; right is {soi[pivot+1: -1]}")
#         _s_ = "(" + phylogeny(soi[1:pivot], _s_)
#         _s_ += soi[pivot]
#         if soi[-1] == ")" and "," in soi[pivot+1:-1]:
#             _s_ += "("
#         _s_ = phylogeny(soi[pivot+1:-1], _s_) + ")"
#         return (_s_)

# print(phylogeny("((A,B),C)", ""))


