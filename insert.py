# Create an empty list
the_list = []

# Can only use [] to update elements that already exist
# the_list[0] = 42

# Can insert into an empty list using:
# insert(index, value)
the_list.insert(0, 10)
print(the_list)

# insert() with index = 0 always inserts at the beginning of the list
the_list.insert(0, 20)
print(the_list)

# insert() with index >= len(list) always appends to the list
the_list.insert(999, 30)
print(the_list)

# In general, insert() inserts *before* the given index
the_list.insert(1, 40)
print(the_list)

# Update an existing element using []
the_list[0] = 50
print(the_list)
