# file_operations.py
def read_csv_file(file_name):
    return_me = list()
    my_file = open(file_name, "r")
    for line in my_file:
        current = line.replace("\n","")
        return_me.append(current.split(','))

    my_file.close()
    return return_me

def write_csv_file(header, data, file_name):
    my_file = open(file_name, "w")
    my_file.write("{}\n".format(",".join(header)))
    for line in data:
        my_file.write("{}\n".format(",".join(line)))
    my_file.close()
