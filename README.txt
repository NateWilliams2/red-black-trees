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
    -rb_node:
    This class implements a single rb_node of the rb-tree and stores a parent, left and right child, a key, and a color,
    represented by a boolean value.
    rb_node also has the methods
        -print_level, which prints all sub-rb_nodes of a given height.
        -get_color, which translates the boolean color value into a string for printing.
        -get-minimum, which returns the smallest-key rb_node in rb_node's sub-tree.
    -nil:
    This class is my way of implementing the nil value for rb-trees. It contains a parent and left and right children
    and a key which should always be set to None, as well as a color which should always be black. It serves as an empty
    rb_node class which I found easier to separate into its own class so that rb_node children can be set to nil by default.
    -tree:
    This class implements the actual rb-tree data structure. It stores only a root rb_node.
    Tree has the methods:
        -rb_insert: inserts a given rb_node into the tree.
            This function contains a loop which iterates on at most every level of the tree, taking O(height) = O(logn) time.
            It also calls rb_insert_fixup, which similarly has a loop whose number of iterations is based on the height.
        -rb_insert_fixup: returns tree to red-black properties after an insert
            As mentioned above, this function contains a loop which looks two rb_nodes above the current rb_node and iterates again.
            It is therefore O(height), or O(logn)
        -rb_transplant: transplants one rb_node for another
            This function is constant-time, because it has no loops and every function it calls is constant
        -rb_delete: deletes a given rb_node from the tree.
            This function has no loops but calls the rb_delete_fixup function, so its time is O(logn)
        -rb_delete_fixup: returns tree to red-black properties after an insert
            The only non-constant part of this function is a loop which repeats moving a pointer up the tree. It therefore
            loops based on the height of the tree in the worst case, so it is O(height) or O(logn).
        -left_rotate: rotates given rb_node and children to the left
            This function is constant-time, because it has no loops and every function it calls is constant
        -right_rotate: rotates given rb_node and children to the right
            This function is constant-time, because it has no loops and every function it calls is constant
        -find_rb_node: finds a rb_node given a value
            Just like in a binary tree, this function is O(logn) because it stops once at each height of the tree.
        -print_tree: prints the entire tree in human-readable format
            This function is O(n) because it visits and prints every rb_node once.

The following methods are also defined:
-get_height: gets the height of a given rb_node
    This function is O(n) because it visits every rb_node once.
-get_black_height: gets the black-height of a given rb_node
    This function is O(n) because it visits every rb_node once.
-initialize: initializes a tree with 10 pseudo-random values based on lfsr initialized with a given seed.

3. Instructions:
To run this code, make sure you have version 3 of python installed and simply run python red_black_tree.py .
You will then be prompted to enter a seed or simply use the default. Follow the command line instructions to execute
tree commands.

4. Sample I.O:
Enter an integer below 256 to seed rb_nodes. Enter -1 to use default seed value.
-1
Initializing tree...
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (161, red)
Enter ADD, DEL, BLKH, or anything else to quit
ADD
What value would you like to add?
122
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (122, red) (161, red)
Enter ADD, DEL, BLKH, or anything else to quit
ADD
What value would you like to add?
30
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (30, red) (122, red) (161, red)
Enter ADD, DEL, BLKH, or anything else to quit
ADD
What value would you like to add?
344
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (30, red) (122, red) (161, red) (344, red)
Enter ADD, DEL, BLKH, or anything else to quit
DEL
What value would you like to delete?
30
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (122, red) (161, red) (344, red)
Enter ADD, DEL, BLKH, or anything else to quit
DEL
What value would you like to delete?
122
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (161, red) (344, red)
Enter ADD, DEL, BLKH, or anything else to quit
DEL
What value would you like to delete?
344
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (161, red)
Enter ADD, DEL, BLKH, or anything else to quit
DEL
What value would you like to delete?
22
a node with that value does not exist
(122, black)
(61, red) (233, red)
(30, black) (67, black) (135, black) (244, black)
(15, red) (161, red)
Enter ADD, DEL, BLKH, or anything else to quit
BLKH
What value's black height would you like to find?
122
rb_node height is: 2
Enter ADD, DEL, BLKH, or anything else to quit
BLKH
What value's black height would you like to find?
67
rb_node height is: 1
Enter ADD, DEL, BLKH, or anything else to quit
BLKH
What value's black height would you like to find?
15
rb_node height is: 0
Enter ADD, DEL, BLKH, or anything else to quit
BLKH
What value's black height would you like to find?
1
a node with that value does not exist
Enter ADD, DEL, BLKH, or anything else to quit
QUIT

Process finished with exit code 0

5. My Experience
This assignment reminded my of many CS-207 assignments, because it was an implementation rather than a problem solving
assignment. I found myself spending a lot of my time reviewing pseudocode from the textbook and implementing it in python.
I found the LFSR program to be an interesting aside from that: rather than a lot of implementation code, it was fairly
simple but required more intentional thought and problem solving before-hand. Overall the most frustrating part of this
assignment was tracking down bugs that were there because of mistakes I made when interpreting pseudocode.