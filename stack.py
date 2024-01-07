comma_pairs : dict = ['()', '[]', '{}']


class Stack():

    def __init__(self, stack : str = ''):
        self.stack = list(stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item : str):
        self.stack += item

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def balanced_commas(input_stack: Stack) -> str :
    if not input_stack.is_empty() and input_stack.size() % 2 == 0:
        true_stack = Stack()
        while input_stack.size() > 1:
            last_comma : str = input_stack.pop()
            next_comma : str = input_stack.peek()
            commas_closed : bool = (next_comma + last_comma) in comma_pairs
            if true_stack.size() > input_stack.size():
                message = 'Not Balanced'
                break
            if not commas_closed:
                true_stack.push(last_comma)
                continue
            input_stack.pop()
            message = 'Balanced'
            while not true_stack.is_empty():
                last_comma : str = true_stack.pop()
                next_comma : str = input_stack.pop()
                commas_closed : bool = (next_comma + last_comma) in comma_pairs
                if not commas_closed:
                    message = 'Not Balanced'
    else:
        message = 'Not Balanced'
    return message


if __name__ == '__main__':
    example1 = Stack('(((([{}]))))')
    example2 = Stack('[([])((([[[]]])))]')
    example3 = Stack('{()}')
    example4 = Stack('}{}')
    example5 = Stack('{{[(])]}}')
    example6 = Stack('[[{())}]')
    examples : dict = [example1, example2, example3, example4, example5, example6]
    for example in examples:
        print(balanced_commas(example))
