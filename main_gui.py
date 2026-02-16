import tkinter as tk
from tkinter import messagebox
from bst.tree import BinarySearchTree
from bst.visualize import visualize_tree
from bst.benchmark import benchmark_insert, benchmark_search


class BSTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Tree - Professional GUI")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.bst = BinarySearchTree()

        self.build_ui()

    # -------------------------
    # UI Layout
    # -------------------------
    def build_ui(self):

        title = tk.Label(self.root, text="Binary Search Tree System",
                         font=("Arial", 18, "bold"))
        title.pack(pady=10)

        # Value Entry
        self.entry = tk.Entry(self.root, width=25, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Button Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        buttons = [
            ("Insert", self.insert),
            ("Delete", self.delete),
            ("Search", self.search),
            ("Inorder", self.show_inorder),
            ("Preorder", self.show_preorder),
            ("Postorder", self.show_postorder),
            ("Height", self.show_height),
            ("Balance Check", self.check_balance),
            ("Visualize", self.visualize),
        ]

        row = 0
        col = 0
        for text, command in buttons:
            tk.Button(btn_frame, text=text, width=18,
                      command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 3:
                col = 0
                row += 1

        # -------------------------
        # Benchmark Section
        # -------------------------

        benchmark_frame = tk.LabelFrame(self.root, text="Performance Benchmark",
                                        padx=10, pady=10)
        benchmark_frame.pack(pady=10)

        tk.Label(benchmark_frame, text="Number of Elements (N):").grid(row=0, column=0)

        self.benchmark_entry = tk.Entry(benchmark_frame, width=10)
        self.benchmark_entry.insert(0, "10000")
        self.benchmark_entry.grid(row=0, column=1, padx=5)

        tk.Button(benchmark_frame, text="Run Benchmark",
                  command=self.run_benchmark,
                  bg="lightblue").grid(row=0, column=2, padx=10)

        # Output Console
        self.output_text = tk.Text(self.root, height=10, width=80)
        self.output_text.pack(pady=15)

    # -------------------------
    # Utility Functions
    # -------------------------

    def get_value(self):
        try:
            value = int(self.entry.get())
            self.entry.delete(0, tk.END)
            return value
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return None

    def print_output(self, message):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)

    # -------------------------
    # BST Operations
    # -------------------------

    def insert(self):
        value = self.get_value()
        if value is not None:
            self.bst.insert(value)
            self.print_output(f"{value} inserted successfully.")

    def delete(self):
        value = self.get_value()
        if value is not None:
            self.bst.delete(value)
            self.print_output(f"{value} deleted successfully.")

    def search(self):
        value = self.get_value()
        if value is not None:
            result = self.bst.search(value)
            self.print_output("Found" if result else "Not Found")

    def show_inorder(self):
        self.print_output("Inorder: " + str(self.bst.inorder()))

    def show_preorder(self):
        self.print_output("Preorder: " + str(self.bst.preorder()))

    def show_postorder(self):
        self.print_output("Postorder: " + str(self.bst.postorder()))

    def show_height(self):
        self.print_output("Height: " + str(self.bst.height()))

    def check_balance(self):
        status = "Balanced" if self.bst.is_balanced() else "Not Balanced"
        self.print_output(status)

    def visualize(self):
        if self.bst.root:
            visualize_tree(self.bst.root)
        else:
            messagebox.showinfo("Info", "Tree is empty!")

    # -------------------------
    # Benchmark Function
    # -------------------------

    def run_benchmark(self):
        try:
            n = int(self.benchmark_entry.get())
            if n <= 0:
                raise ValueError

            insert_time = benchmark_insert(n)
            search_time = benchmark_search(n)

            result = (
                f"Benchmark Results (N = {n})\n"
                f"-----------------------------------\n"
                f"Insert Time : {insert_time:.6f} seconds\n"
                f"Search Time : {search_time:.6f} seconds\n"
            )

            self.print_output(result)

        except ValueError:
            messagebox.showerror("Invalid Input",
                                 "Enter a valid positive integer for benchmark size.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BSTApp(root)
    root.mainloop()
