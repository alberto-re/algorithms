"""Implementation of the classical recursive solution for the Hanoi Tower
problem: http://www.cs.cmu.edu/~cburch/survey/recurse/hanoi.html
"""

DISK_NUMBER = 9


class Tower:

    def __init__(self, *disks):
        self._content = []
        for disk in disks:
            self._content.append(disk)

    def push(self, disk):
        self._content.append(disk)

    def pop(self):
        return self._content.pop()

    def __len__(self):
        return len(self._content)

    def __getitem__(self, index):
        return self._content[index]


class State:

    def __init__(self, *towers):
        self._towers = []
        self._print_fmt = '{0: ^%d}' % (DISK_NUMBER + ((DISK_NUMBER - 1) * 2))
        for tower in towers:
            self._towers.append(tower)

    def __len__(self):
        return len(self._towers)

    def __getitem__(self, index):
        return self._towers[index]

    def print(self):
        print()
        for i in range(DISK_NUMBER, -1, -1):
            for tower in self._towers:
                if len(tower) > i:
                    print(self._print_fmt.format(u"\u2584" * ((tower[i] * 2) + 1)), end="")
                else:
                    print(self._print_fmt.format(u"\u2588"), end="")
            print()


def solve_hanoi(state):

    def move_tower(disk, source, dest, spare):
        if disk == 1:
            state[dest].push(state[source].pop())
            state.print()
        else:
            move_tower(disk - 1, source, spare, dest)
            state[dest].push(state[source].pop())
            state.print()
            move_tower(disk - 1, spare, dest, source)
    
    state.print()
    move_tower(DISK_NUMBER, 0, 2, 1)


def main():
    state = State(Tower(*[x for x in range(DISK_NUMBER, 0, -1)]), Tower(), Tower())
    solve_hanoi(state)


if __name__ == "__main__":
    main()
