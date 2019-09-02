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

# Retrieve mutliple items using a slice
the_list = [0, 1, 2, 3]
result = the_list[1:3]

# Slices are open on the right!
# This yields an empty list
the_list = [0, 1, 2, 3]
the_list[1:1]

# Set multiple items
the_list = [0, 1, 2, 3]
the_list[1:3] = [11, 22]

# Extend a list
the_list = [0, 1, 2, 3]
the_list[len(the_list):] = [11, 22]

# Can extend an empty list
the_list = []
the_list[0:] = [11, 22]

# Gotcha! Slice is too small
the_list = [0, 1, 2, 3]
the_list[1:2] = [11, 22]

# Gotcha! Slice is too large
the_list = [0, 1, 2, 3]
the_list[1:4] = [11, 22]
