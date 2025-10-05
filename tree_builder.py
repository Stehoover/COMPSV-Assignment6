class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        """
        Inserts a new employee under the specified manager.

        Uses a recursive search to find the manager and then inserts the new employee
        as their left or right subordinate, provided the spot is empty.
        """
        if self.root is None:
            print("⚠️ Cannot add employee. Please add a Team Lead (root) first.")
            return

        if current_node is None:
            # Start the recursive search from the root
            current_node = self.root

        if current_node.name == manager_name:
            # Manager found, attempt to insert
            new_node = EmployeeNode(employee_name)
            side = side.lower()

            if side == "left":
                if current_node.left is None:
                    current_node.left = new_node
                    print(f"✅ {employee_name} added as the LEFT subordinate of {manager_name}.")
                    return True 
                else:
                    print(f"❌ Cannot add {employee_name}. {manager_name} already has a left subordinate: {current_node.left.name}")
                    return False
            elif side == "right":
                if current_node.right is None:
                    current_node.right = new_node
                    print(f"✅ {employee_name} added as the RIGHT subordinate of {manager_name}.")
                    return True 
                else:
                    print(f"❌ Cannot add {employee_name}. {manager_name} already has a right subordinate: {current_node.right.name}")
                    return False
            else:
                print("❌ Invalid side specified. Must be 'LEFT' or 'RIGHT'.")
                return False

        # Recursively search the left and right subtrees
        found = False
        if current_node.left:
            found = self.insert(manager_name, employee_name, side, current_node.left)
            if found:
                return True

        if current_node.right and not found:
            found = self.insert(manager_name, employee_name, side, current_node.right)
            if found:
                return True

        # Only print this message if the initial call to insert didn't find the manager
        if current_node == self.root and not found:
            print(f"❌ Manager '{manager_name}' not found in the team structure.")
            return False

        return found

    def print_tree(self, node=None, level=0):
        """
        Prints the tree structure using a recursive pre-order traversal.
        """
        if self.root is None:
            print("The team structure is empty. Add a team lead first.")
            return

        if node is None:
            node = self.root

        # Pre-order traversal logic
        indent = "  " * level
        print(f"{indent}- {node.name}")

        if node.left:
            # Recursively print the left subtree
            self.print_tree(node.left, level + 1)

        if node.right:
            # Recursively print the right subtree
            self.print_tree(node.right, level + 1)

# Test your code here
def test_team_tree():
    print("--- Starting TeamTree Test ---")
    tree = TeamTree()

    #Test adding root
    tree.root = EmployeeNode("Alice (CEO)")
    print(f"Root added: {tree.root.name}")
    tree.print_tree()

    #Test inserting left and right subordinates
    print("\nAttempting to insert subordinates...")
    tree.insert("Alice (CEO)", "Bob (VP)", "left")
    tree.insert("Alice (CEO)", "Charlie (VP)", "right")

    #Test inserting deeper
    tree.insert("Bob (VP)", "David (Director)", "left")
    tree.insert("Bob (VP)", "Eve (Director)", "right")

    #Test inserting under a non-existent manager
    tree.insert("Frank", "George", "left")

    #Test trying to overwrite a spot (left of Charlie)
    tree.insert("Charlie (VP)", "Fiona (Director)", "left")
    tree.insert("Charlie (VP)", "Gary (Director)", "left") # Should fail

    #Test printing the final tree
    print("\n--- Final Team Structure ---")
    tree.print_tree()

    print("--- TeamTree Test Complete ---")

#Run Tests
test_team_tree()


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

# Run the Command Line Interface
if __name__ == "__main__":
    company_directory()