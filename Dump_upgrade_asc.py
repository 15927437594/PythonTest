import os

path = os.path.join(os.getcwd(), 'log_upgrade_asc')
for root, _, files in os.walk(path):
    for file_name in files:
        print(root, file_name)
        file_path = os.path.join(root, file_name)
        print(file_path)
        with open(file_path, encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                if line.__contains__("04 74 20 08 02 cc cc cc"):
                    print(line)
                    filename = os.path.join(path, 'asc.txt')
                    with open(filename, 'a') as file_object:
                        file_object.write("%s, True, %s" % (file_name.split(".")[0], line))
                        file_object.write("\n")
                elif line.__contains__("04 74 20 10 02"):
                    print(line)
                    filename = os.path.join(path, 'asc.txt')
                    with open(filename, 'a') as file_object:
                        file_object.write("%s, False, %s" % (file_name.split(".")[0], line))
                        file_object.write("\n")
