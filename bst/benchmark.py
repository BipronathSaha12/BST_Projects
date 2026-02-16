import time
import random
from .tree import BinarySearchTree


def benchmark_insert(n=10000):
    bst = BinarySearchTree()
    data = random.sample(range(n * 10), n)

    start = time.perf_counter()
    for value in data:
        bst.insert(value)
    end = time.perf_counter()

    return end - start


def benchmark_search(n=10000):
    bst = BinarySearchTree()
    data = random.sample(range(n * 10), n)

    for value in data:
        bst.insert(value)

    start = time.perf_counter()
    for value in data:
        bst.search(value)
    end = time.perf_counter()

    return end - start
