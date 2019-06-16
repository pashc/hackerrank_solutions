class MyQueue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def peek(self):
        if len(self.out_stack) == 0:
            while not len(self.in_stack) == 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        pass

    def pop(self):
        if len(self.out_stack) == 0:
            while not len(self.in_stack) == 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def put(self, value):
        self.in_stack.append(value)

    def __is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def __size(self):
        return len(self.in_stack) + len(self.out_stack)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
