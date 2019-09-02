# insert(index, value)

# insert() with index = 0 always prepends to the list
the_list = [0, 1, 2]
the_list.insert(0, 42)

# insert() with index >= len(list) always appends to the list
the_list = [0, 1, 2]
the_list.insert(len(the_list), 42)
the_list.insert(999, 1000)

# In general, insert() inserts *before* the given index
the_list = [0, 1, 2]
the_list.insert(1, 42)

# It is safe to insert into an empty list
the_list = []
the_list.insert(0, 42)

the_list = []
the_list.insert(999, 42)
