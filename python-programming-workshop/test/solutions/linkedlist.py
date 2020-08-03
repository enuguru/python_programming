# CSE 143, Winter 2010, Steve Geluso

# inner class making up ListNodes for LinkedList
class ListNode:
	# constructs a new LinkNode
	# defaults data and next to None
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	# returns string representatio of node; "self.data"
	def __str__(self):
		return str(self.data)

# a linked list object that stores a list of elements and provides basic
# add, remove... functionality
class LinkedList:
		
	# creates a new LinkedList; front set to None by default
	def __init__(self):
		self.front = None

	# adds value to given index. defaults to end of list when no index given
	def add(self, value, index=-1):
		if (self.front == None or index == 0):
			self.front = ListNode(value, self.front)
		else:
			current = self.front
			count = 0
			while ((index == -1 and current.next != None) or count < index - 1):
				current = current.next
				count += 1
			current.next = ListNode(value, current.next)
	
	# returns value of node at given index. Index must be 0 <= index < list size
	def get(self, index):
		current = self.front
		for i in range(index):
			current = current.next
		return current.data
	
	# removes the element at given index from list
	def remove(self, index=None):
		if (index == 0 or index==None):
			self.front = self.front.next
		else:
			current = self.front
			for i in range(index-1):
				current = current.next
			current.next = current.next.next
	
	# returns an iterator
	def __iter__(self):
		self.iter = self.front
		return self
	
	# iterates over each node in the list, returning each node
	# interesting read: http://www.python.org/dev/peps/pep-3114/
	def __next__(self):
		if (self.iter == None):
			raise StopIteration
		result = self.iter
		self.iter = self.iter.next
		return result
	
	# returns length of the list to make list behave more like a sequence
	def __len__(self):
		count = 0
		current = self.front
		while (current != None):
			current = current.next
			count += 1
		return count
		
	# returns true of list contains value, returns false otherwise
	def __contains__(self, value):
		current = self.front
		while(current != None):
			if(current.data == value):
				return True
			current = current.next
		return False
	
	# returns a string representation of the list as "[v1, v2.. vn]"
	def __str__(self):
		current = self.front
		result = "[ "
		while (current != None):
			result += str(current) + " "
			current = current.next
		return result + "]"
		
	# doubles the value of each node in the list
	def double(self):
		for node in self:
			node.data = node.data * 2
			
# main
print("creating linked list...")
l = LinkedList()
print("adding values 2, 23, 1, 46...")
l.add(2)
l.add(23)
l.add(1)
l.add(46)
print(l)
print("doubling values in list...")
l.double()
print(l)
