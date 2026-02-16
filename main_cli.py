from bst.tree import BinarySearchTree
from bst.visualize import visualize_tree
from bst.benchmark import benchmark_insert, benchmark_search


def main():
    bst = BinarySearchTree()

    while True:
        print("\n1.Insert 2.Delete 3.Search 4.Inorder 5.Preorder 6.Postorder")
        print("7.Height 8.Balance 9.Visualize 10.Benchmark 0.Exit")

        choice = input("Choice: ")

        try:
            if choice == "1":
                bst.insert(int(input("Value: ")))
                print("Inserted.")

            elif choice == "2":
                bst.delete(int(input("Value: ")))
                print("Deleted.")

            elif choice == "3":
                result = bst.search(int(input("Value: ")))
                print("Found" if result else "Not Found")

            elif choice == "4":
                print("Inorder:", bst.inorder())

            elif choice == "5":
                print("Preorder:", bst.preorder())

            elif choice == "6":
                print("Postorder:", bst.postorder())

            elif choice == "7":
                print("Height:", bst.height())

            elif choice == "8":
                print("Balanced" if bst.is_balanced() else "Not Balanced")

            elif choice == "9":
                visualize_tree(bst.root)

            elif choice == "10":
                print("Insert Time:", benchmark_insert())
                print("Search Time:", benchmark_search())

            elif choice == "0":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
