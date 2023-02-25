"""WAP to print string that start with 'c' and ends with 'b'"""
name = ['chb','asdf','chtrb','dfg','cgyb']
new_name = [x for x in name if name.startswith('c')& name.endswith('b')]
print(new_name)