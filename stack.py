# Import deque from collections for efficient queue operations


# -------------------- STACK IMPLEMENTATION --------------------
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack (LIFO)
        return self.items.pop() if self.items else None

    def undo(self):
        # Undo the last action by popping the top item
        return self.pop()

    def top(self):
        # Peek at the top item without removing it
        return self.items[-1] if self.items else None

    def reverse_string(self, text):
        # Reverse a string using stack logic
        for char in text:
            self.push(char)  # Push each character onto the stack
        reversed_text = ''
        while self.items:
            reversed_text += self.pop()  # Pop characters to reverse order
        return reversed_text

# ----------- STACK USAGE EXAMPLES -----------

# MoMo Pay example: simulate pushing steps and undoing the last one
stack = Stack()
stack.push("Enter Amount")
stack.push("Enter PIN")
stack.push("Confirm Payment")
stack.undo()  # Undo last step ("Confirm Payment")
print("Top step left:", stack.top())  # Should print "Enter PIN"

# UR student example: simulate pushing study resources and popping two
stack2 = Stack()
stack2.push("Lecture Notes")
stack2.push("Practice Questions")
stack2.push("Mock Exam")
stack2.pop()  # Removes "Mock Exam"
stack2.pop()  # Removes "Practice Questions"
print("Top item:", stack2.top())  # Should print "Lecture Notes"

# Reverse the string "RWANDA" using stack
print("Reversed RWANDA:", stack.reverse_string("RWANDA"))  # Should print "ADNAWR"

