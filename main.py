def count_and_replace(file_name):
    with open(file_name, 'r') as file:
        edit = file.read()

        # Count occurrences of "terrible"
        count = edit.count('terrible')

        # Replace even occurrences with "pathetic" and odd occurrences with "marvellous"
        replaced_edit = edit.replace('terrible', 'pathetic', count // 2)
        replaced_edit = replaced_edit.replace('terrible', 'marvellous', count - count // 2)
    with open('result.txt', 'w') as result_file:
        result_file.write(replaced_edit)
    return count


# Test the function
file_to_read = 'file_to_read.txt'
total_count = count_and_replace(file_to_read)
result_message = 'Total occurrences of "terrible": {}'.format(total_count)
print(result_message)
print('Replaced text has been written to "result.txt"')