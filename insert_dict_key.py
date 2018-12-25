dictionary = {'text-which-matches-a-key': 'value corresponding to the key'}

# Open file and fill a list in which each element is a line.
f = open('file', 'r')
lines = f.readlines()
f.close()

# Empty the file.
f = open('file', 'w')
f.close()

# Insert dictionary value at the right place.
for index, line in enumerate(lines):
    '''Remove the newline character '\n'
    to the right of the strings in the file.
    The lines don't match dictionary keys if
    the dictionary keys don't have newlines
    appended.'''
    line = line.rstrip()
    # Check if any line is a key in the dictionary.
    if line in dictionary.keys():
        key_occurs_in_text = True
        key_occurring_in_text = line
    ''' 'some important lines' is reached and a key
    of the dictionary has appeared as a line in the
    file. Save the list index which corresponds to
    the line after or before 'some important lines' in
    the variable insert_index. '''
    if 'some important lines' == line and key_occurs_in_text:
        insert_index = index + 1
        # insert_index = index - 1

'''A line in the file
is a key in the dictionary.
Insert the value of the key at the index we saved
in insert_index.
Prepend and append newline characters to match
the file format.'''
if key_occurs_in_text:
    lines.insert(insert_index, '\n'+dictionary[key_occurring_in_text]+'\n')

# Write the changed file content to the empty file.
f = open('file', 'w')
for line in lines:
    f.write(line)
f.close