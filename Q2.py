# PART 2 Stack or Queue Tasks arriving one after another: Task1, Task2, Task3, Task4, Task5
# 1.If served using a stack, write the order in which they get completed.
# 2.If served using a queue, write the order in which they get completed.
# 3.A printer prints jobs in the order they arrive. Which structure should it use, and write out the order it will print Task1 to Task5.


from collections import deque
tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

# Using Stack
print("STACK:Last In First Out")
stack = []
for task in tasks:
    stack.append(task)
while stack:
    print(stack.pop())
print()

# Using Queue
print("QUEUE:First In First Out")
queue = deque(tasks)
while queue:
    print(queue.popleft())
print()

# Printer
print("Printer")
printer_queue = deque(["Task1", "Task2", "Task3", "Task4", "Task5"])
while printer_queue:
    print("Printing:", printer_queue.popleft())
print("A printer uses a Queue:FIFO(First In First Out)")
print("The first document sent to the printer is printed first.")    