# [] is Python's index operator
# The key can be an integer or a slice!

# Retrieve a single item
the_list = [0, 1, 2]
result = the_list[1]

# Update a single item
the_list = [0, 1, 2]
the_list[1] = 42

# [] with an integer key can only update elements that already exist
the_list = []
# the_list[0] = 42  # Raises an IndexError
