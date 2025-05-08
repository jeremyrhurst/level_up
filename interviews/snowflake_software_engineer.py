# Implement a data structure with the following methods:

# birth(name, parent_name)
# death(name)
# order_of_succession(): list of names
# Eldest child of the crown is first in succession, followed by their children and so on.

# For example, given the family tree:

# Elizabeth

# Charles

# William

# George

# Charlotte

# Henry

# Andrew

# The order of succession is: Elizabeth, Charles, William, George, Charlotte, Henry, Andrew

# If somebody dies, it removes them from the line of succession, does not change the ordering of anyone who survives.


# Charles, Elizabeth
# 1   2   3
# 4   5   6


#          George
#           |
#      -----------------
#      |       |       |
# Elizabeth Margaret  Edward
#      |
#   -------------------------
#   |      |        |       |
# Charles Anne   Andrew  Edward
#    |
#   ---------
#   |       |
# William  Harry
#    |
# ---------
# |   |   |
# G_  C   L

# To return order of succession we do DFS preorder
# Nary tree: each parent can have any number of children

class Person():
    def __init__(self, name, parent_name) -> None:
        self.name = name
        self.parent_name = parent_name
        self.children = []

class Family_tree():
    def __init__(self) -> None:
        self.head = None
        self.data = {}

    def birth(name, parent_name):
        new_person = Person(name, parent_name)
        self.data[parent_name].children.append(new_person)
        self.data[name] = new_person
        # Search for parent
        # add new person as a child

    def death(name):

    def order_of_succession():
        names = []
        # DFS preorder
        # Start with the head node
        # add current node to names
        # recur first on the first child
        # recur on the rest of the children

        return names
        
    
family_tree = 