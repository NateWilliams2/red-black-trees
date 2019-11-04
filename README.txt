Nate Williams
Assignment 5
11/3/2019

1. Problem Description
This problem has two parts. One is programming a linear feedback shift register function which, given an optional seed
as input, produces a series of random-appearing but deterministic output numbers between 0 and 256.
The main part of the problem is an implementation of Red-Black Binary Trees. This implementation should have insertion
and deletion functions and should maintain the red-black tree properties.

2. Analysis
The classes are
    -node:
    This class implements a single node of the rb-tree and stores a parent, left and right child, a key, and a color,
    represented by a boolean value.
    Node also has the methods
        -print_level, which prints all sub-nodes of a given height.
        -get_color, which translates the boolean color value into a string for printing.
        -get-minimum, which returns the smallest-key node in node's sub-tree.
    -nil:
    This class is my way of implementing the nil value for rb-trees. It contains a parent and left and right children
    and a key which should always be set to None, as well as a color which should always be black. It serves as an empty
    node class which I found easier to separate into its own class so that node children can be set to nil by default.
    -tree:
    This class implements the actual rb-tree data structure. It stores only a root node.
    Tree has the methods:
        -rb_insert
        -rb_insert_fixup
        -rb_transplant
        -rb_delete
        -rb_delete_fixup
        -left_rotate
        -right_rotate
        -find_node
        -print_tree

The following methods are also defined:
-get_height
-get_black_height
-initialize
-
