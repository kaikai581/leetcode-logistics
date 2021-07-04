#!/usr/bin/env python

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        pass

    def mirror(self, root):
        if root == None:
            return None
        
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root

    def traverse(self, root):
        if root == None:
            return []
    
        return [root.val]+self.traverse(root.left)+self.traverse(root.right)
        
        
    def isSymmetric(self, root: TreeNode) -> bool:
        arr1 = self.traverse(root)
        mirror_root = self.mirror(root)
        arr2 = self.traverse(mirror_root)
        
        return arr1 == arr2

# Function to insert nodes in level order 
def construct_tree(arr, root, i):
    n = len(arr)
    # Base case for recursion 
    if i < n:
        root = TreeNode(arr[i]) 
  
        # insert left child 
        root.left = construct_tree(arr, root.left,
                                     2 * i + 1) 
  
        # insert right child 
        root.right = construct_tree(arr, root.right,
                                      2 * i + 2)
    return root

# Function to print tree nodes in 
# InOrder fashion 
def inOrder(root):
    if root == None:
        return []

    return inOrder(root.left)+[root.val]+inOrder(root.right)

def preorder(root):
    if root == None:
        return []

    return [root.val]+preorder(root.left)+preorder(root.right)

def postorder(root):
    if root == None:
        return []

    return preorder(root.left)+preorder(root.right)+[root.val]

def mirror(root):
    if root == None:
        return None
    
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
    
    return root

def pseudoPalindromicPaths(root: TreeNode) -> int:
    # def traverse(root, num_freq):
    #     if root == None:
    #         return
        
    #     num_freq[root.val] += 1
    #     traverse(root.left, num_freq)
    #     traverse(root.right, num_freq)
        
    #     if root.left == None and root.right == None:
    #         print(num_freq)
    #         nodd_freq = 0
    #         for freq in num_freq.values():
    #             if freq%2 == 1:
    #                 nodd_freq += 1
    #         if nodd_freq <= 1:
    #             # res += 1
    #             pass
    
    def traverse(root, arr):
        if root == None:
            return
        
        arr.append(root.val)
        traverse(root.left, arr)
        traverse(root.right, arr)
        
        if root.left == None and root.right == None:
            print(arr)
        
        arr.pop()

    res = 0
    traverse(root, [])
    
    return res

if __name__ == '__main__':
    tree1 = construct_tree([1,2,2,3,4,4,3], TreeNode(), 0)
    tree2 = mirror(tree1)
    print(preorder(tree1))
    print(postorder(tree1))
    # arr1 = inOrder(tree1)
    # arr2 = inOrder(tree2)
    # print(arr1)
    # print(arr2)

    tree3 = construct_tree([1,2,2,None,3,None,3], TreeNode(), 0)
    tree4 = mirror(tree3)
    print(preorder(tree3))
    print(postorder(tree3))
    # arr3 = inOrder(tree3)
    # arr4 = inOrder(tree4)
    # print(arr3)
    # print(arr4)
    # print(arr3 == arr4)

    # my_sol = Solution()
    # print(my_sol.isSymmetric(tree3))

    # 1457. Pseudo-Palindromic Paths in a Binary Tree
    tree1475 = construct_tree([2,3,1,3,1,None,1], TreeNode(), 0)
    print(pseudoPalindromicPaths(tree1475))
