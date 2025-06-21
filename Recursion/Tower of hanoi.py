# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N = 3

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

"""
Output
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C

Time complexity: O(2^N), There are two possibilities for every disk. 

Therefore, 2 * 2 * 2 * . . . * 2(N times) is 2^N

Auxiliary Space: O(N), Function call stack space

"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def toh_iterative(n):
    src = 'A'
    aux = 'B'
    dest = 'C'
    moves = 2 ** n - 1

    rods = {src: list(range(n, 0, -1)), aux: [], dest: []}               # Stack representation of rods

    if n % 2 == 0:                                                       # Swap if number of disks is even
        aux, dest = dest, aux

    def move_disk(from_rod, to_rod):

        f = rods[from_rod][-1] if rods[from_rod] else float('inf')       # Get top disks or assign dummy large value if rod empty
        t = rods[to_rod][-1] if rods[to_rod] else float('inf')


        if f < t:                                                        # Move the smaller disk
            disk = rods[from_rod].pop()
            rods[to_rod].append(disk)
            print(f"Move disk {disk} from {from_rod} to {to_rod}")
        else:
            disk = rods[to_rod].pop()
            rods[from_rod].append(disk)
            print(f"Move disk {disk} from {to_rod} to {from_rod}")

    for move in range(1, moves + 1):
        if move % 3 == 1:
            move_disk(src, dest)
        elif move % 3 == 2:
            move_disk(src, aux)
        elif move % 3 == 3:
            move_disk(aux, dest)


toh_iterative(3)

