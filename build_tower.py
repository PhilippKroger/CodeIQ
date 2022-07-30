"""
Build Tower
Build a pyramid-shaped tower given
a positive integer number of floors.
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
"""

def tower_builder(n_floors):
    tree = []
    for i in range(1, 2*n_floors, 2):
        n_floors -= 1
        tree.append(" " * n_floors + "*"*i + " " * n_floors)
    return tree

print(tower_builder(5))