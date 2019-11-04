from linear_feedback_shift_register import lfsr
RED = True
BLACK = False

class nil:
    def __init__(self):
        self.parent = None
        self.key = None
        self.color = BLACK
        self.right = None 
        self.left = None

NIL = nil()

class tree: 
    def __init__(self):
        self.root = NIL
    
    #inserts a node into rb-tree
    def rb_insert(self, node):
        y = NIL
        x = self.root
        while x != NIL:
            y = x
            if node.key < x.key:
                x = x.left 
            else: 
                x = x.right 
        node.parent = y
        if y == NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.left = NIL
        node.right = NIL
        node.color = RED
        self.rb_insert_fixup(node)

    #fixes rb tree post-insert to ensure it still follows rb-tree properties
    def rb_insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            elif node.parent == node.parent.parent.right:
                y = node.parent.parent.left
                if y.color:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self.root.color = BLACK

    #transplants node u with node v
    def rb_transplant(self, u, v):
        if u.parent == NIL:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    #deletes given node from tree
    def rb_delete(self, z):
        y = z
        y_original_color = z.color
        if z.left == NIL:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == NIL:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = z.right.get_minimum()
            print(y.key, y.color)
            y_original_color = y.color
            x = y.right 
            if y.parent == z:
                x.parent = y
            else: 
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            if y_original_color == BLACK:
                self.rb_delete_fixup(x)

    #fixes rb tree properties after delete operation
    def rb_delete_fixup(self, x):
        while x is not self.root and x.color != BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK 
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK 
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

                
    #rotates tree left around node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    #rotates tree right around node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == NIL:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    #finds a node in tree based on a given value
    def find_node(self, val):
        node = self.root
        while node != NIL:
            if val == node.key:
                return node
            elif val < node.key:
                node = node.left
            elif val > node.key: 
                node = node.right
        return NIL

    #level-order print of tree's nodes
    def print_tree(self):
        for level in range (1, get_height(self.root) + 1):
            self.root.print_level(level)
            print("")
    
#node of a rb-tree
class node:
    #initializes node with defaults: no relatives, key=0, color=red
    def __init__(self, key = 0):
        self.parent = NIL
        self.key = key
        #true = red, false = black
        self.color = RED
        self.right = NIL 
        self.left = NIL

    #recursively prints a givel level of child nodes of node
    def print_level(self, level):
        if level == 1: 
            print("(" + str(self.key) + ", " + self.get_color(), end = ') ') 
        elif level > 1: 
            if self.left != NIL:
                self.left.print_level(level - 1) 
            else: print("nil", end=" ")
            if self.right != NIL: 
                self.right.print_level(level - 1) 
            else: print("nil", end=" ")

    #gets the color of a node in a human-readable string
    def get_color(self):
        if self.color:
            return "red"
        else:
            return "black"

    #gets the minimum node from a subtree
    def get_minimum(self):
        node = self
        while node.left != NIL:
            node = node.left
        return node

#gets the un-colored height of a node
def get_height(node):
    if node == NIL:
        return 0
    else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        return max(left_height, right_height) + 1

#gets the black height of a node
def get_black_height(node):
    if node == NIL:
        return 0
    else:
        left_height = get_black_height(node.left)
        right_height = get_black_height(node.right)
        if node.color:
            return max(left_height, right_height)
        else:
            return max(left_height, right_height) + 1

#initializes tree with random values
def initialize(seed = None):
    new_node = node()
    if seed == None:
        gen = lfsr()
    else:
        gen = lfsr(seed)
    t = tree()
    for i in range (0, 9):
        t.rb_insert(node(gen.nextValue()))
    return t

#runs program in indefinite loop with user input
user_input = int(input("Enter an integer below 256 to seed nodes or anything else for the default seed\n"))
if user_input >= 0 and user_input < 256:
    print("Initializing tree...")
    t = initialize(user_input)
else:
    print("Initializing tree...")
    t = initialize()
t.print_tree()
while 1:
    user_input = input(
        "Enter ADD, DEL, BLKH, or anything else to quit\n")
    if user_input == "ADD":
        user_input = int(input("What value would you like to add?\n"))
        new_node = node(user_input)
        t.rb_insert(new_node)
        t.print_tree()
    elif user_input == "DEL":
        user_input = int(input("What value would you like to delete?\n"))
        node = t.find_node(user_input)
        if node != NIL and node != None:
            t.rb_delete(node)
        else: 
            print("Node does not exist")
        t.print_tree()
    elif user_input == "BLKH":
        user_input = int(input("What value's black height would you like to find?\n"))
        node = t.find_node(user_input)
        if node != NIL and node != None:
            print("Node height is: " + str(get_black_height(node)))
        else: 
            print("Node does not exist")
    else:
        break

