class Stack:
    def __init__(self) -> None:
        self.data = [0 for i in range(1000)]
        self.data[0] = 1
        self.size = 1

    def set_size(self, new_size):
        self.size = new_size

    def append(self, j, k):
        res = 0
        for i in range(j, k + 1):
            res += self.data[i]
        self.data[self.size] = res
        self.size += 1
        assert self.size <= 1000

    def back(self):
        return self.data[self.size - 1]


def do_work(stack, n):
    initial_size = stack.size
    main_res = None
    for l in range(initial_size):
        for k in reversed(range(l, initial_size)):
            stack.append(l, k)
            if stack.back() == n:
                return [(l + 1, k + 1), ]
            if stack.back() > n:
                return None
            if stack.size > 1000:
                return None
            res = do_work(stack, n)
            stack.set_size(initial_size)
            if res is None:
                continue
            if main_res is None or (len(main_res) - 1) > len(res):
                main_res = [(l + 1, k + 1)] + res
    return main_res


def find_way(n):
    stack = Stack()
    return do_work(stack, n)


def print_answer(answer):
    print(len(answer))
    for elem in answer:
        print(elem[0], elem[1])


t = int(input())
n_list = [int(input()) for _ in range(t)]
for n in n_list:
    print_answer(find_way(n))
