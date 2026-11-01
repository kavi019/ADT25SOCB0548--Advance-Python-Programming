import gc


class Node:

    def __init__(self, name):
        self.name = name
        self.partner = None


def create_cycle():
    n1 = Node("NodeA")
    n2 = Node("NodeB")
    n1.partner = n2
    n2.partner = n1  # Creates a reference cycle


if __name__ == "__main__":
    print("--- Garbage Collection Demo ---")
    gc.disable()
    print(f"GC enabled status: {gc.isenabled()}")

    create_cycle()
    print(
        "Reference cycle created and variables went out of scope, but objects remain in memory."
    )

    collected = gc.collect()
    print(f"Manual garbage collection ran. Collected objects: {collected}")

    gc.enable()
    print(f"GC enabled status restored: {gc.isenabled()}")