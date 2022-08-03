import cmd 

''' Print Columns Function '''
def print_columns(data):
    tag_list = []
    column_count = 0
    tag_index = data.columns[2:]

    for tag in tag_index:
        count_str = str(column_count)
        column_row = '|' + count_str + ' ' + tag
        tag_list.append(column_row)
        column_count += 1

    print("\nTag Names: ")
    print('_'*80)
    cli = cmd.Cmd()
    cli.columnize(tag_list, displaywidth=80)
    print('_'*80)
    print('\n')

    return tag_list
