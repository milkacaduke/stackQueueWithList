import collections
import timeit

class myStack(object):
	def __init__(self):
		self.stack = []

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		return self.stack.pop()

	def get_len(self):
		return len(self.stack)


class myQueue(object):
	def __init__(self):
		self.queue = collections.deque([])

	def push(self, value):
		self.queue.append(value)
	
	def pop(self):
		return self.queue.popleft()

class myQueue2(object):
	def __init__(self):
		self.queue = collections.deque([])

	def push(self, value):
		self.queue.appendleft(value)

	def pop(self):
		return self.queue.pop()


# class shittyQueue(object):
# 	def __init__(self):
# 		self.queue = []




my_stack = myStack()
my_queue = myQueue()
my_queue2 = myQueue2()
number = 100000000

def stackpush():	
	my_stack.push('a')

def stackpop():
	my_stack.pop()

def queuepush():
	my_queue.push('a')

def queuepop():
	my_queue.pop()

def queue2push():
	my_queue2.push('a')

def queue2pop():
	my_queue2.pop()




print("stack push with {} number: {}".format(number, timeit.timeit(stmt=stackpush, number=number)))
print("stack pop with {} number: {}".format(number, timeit.timeit(stmt=stackpop, number=number)))
my_stack = None

print("queue push with {} number: {}".format(number, timeit.timeit(stmt=queuepush, number=number)))
print("queue pop with {} number: {}".format(number, timeit.timeit(stmt=queuepop, number=number)))
my_queue = None

print("queue2 push with {} number: {}".format(number, timeit.timeit(stmt=queue2push, number=number)))
print("queue2 pop with {} number: {}".format(number, timeit.timeit(stmt=queue2pop, number=number)))
my_queue2 = None


