from bst.tree import BinarySearchTree
from bst.visualize import visualize_tree

def menu():
    print("\nBinary Search Tree CLI")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Height")
    print("8. Check Balance")
    print("9. Visualize Tree")
    print("0. Exit")

def main():
    bst = BinarySearchTree()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            key = int(input("Enter value to insert: "))
            bst.insert(key)

        elif choice == "2":
            key = int(input("Enter value to delete: "))
            bst.delete(key)

        elif choice == "3":
            key = int(input("Enter value to search: "))
            result = bst.search(key)
            print("Found!" if result else "Not Found!")

        elif choice == "4":
            print("Inorder:", bst.inorder())

        elif choice == "5":
            print("Preorder:", bst.preorder())

        elif choice == "6":
            print("Postorder:", bst.postorder())

        elif choice == "7":
            print("Height:", bst.height())

        elif choice == "8":
            print("Balanced!" if bst.is_balanced() else "Not Balanced!")

        elif choice == "9":
            visualize_tree(bst.root)

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
