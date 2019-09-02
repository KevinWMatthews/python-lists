# Create an empty list
the_list = []
# or
the_list = list()

# Multiplication
list_size = 3
the_list = [''] * list_size

# List comprehension
list_size = 3
the_list = ['' for _ in range(list_size)]

# itertools.repeat()
import itertools
list_size = 3
the_list = list(itertools.repeat('', list_size))
