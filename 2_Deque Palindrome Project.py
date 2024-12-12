class Deque:
  def __init__(self):
    self.elements = []
  def add_first(self, item):
    self.elements.append(item)
  def add_last(self, item):
    self.elements.insert(0, item)
  def remove_first(self):
    item = self.elements.pop()
    return item
  def remove_last(self):
    item = self.elements.pop(0)
    return item
  def is_empty(self):
    if len(self.elements) > 0:
      return False
    return True
  def size(self):
    return len(self.elements)
  def peek_first(self):
    return self.elements[-1]
  def peek_last(self):
    return self.elements[0]
  def display_deque(self):
    print('\t | \t'.join(str(item) for item in self.elements))

def is_palindrome(word):
  deque = Deque()
  for char in word:
    deque.add_first(char)

  while deque.size() > 1:
      # Pop from the rear of the deque. Replace None with code
      first = deque.remove_first()  
      # Pop from the front of the deque. Replace None with code
      last = deque.remove_last()
      # If statement goes below to check for equality
      if first!=last:
        return False
  return True  

deque = Deque()
print(is_palindrome('alskjfwi'))
print(is_palindrome('level'))
print(is_palindrome('kayak'))
