import os

path = os.path.join(os.getcwd(), 'log_ICS_TPCM')
sn_list = []
for root, _, files in os.walk(path):
    for file_name in files:
        print(root, file_name)
        file_path = os.path.join(root, file_name)
        sheet_name = root.split('\\')[1]
        print(file_path, sheet_name)
        with open(file_path, encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                if line.__contains__("loadCmValue cmBuffer="):
                    cm_data = line.split("loadCmValue cmBuffer=")[1]
                    print(cm_data)
                    filename = os.path.join(path, 'TPCM.txt')
                    with open(filename, 'a') as file_object:
                        file_object.write(cm_data)
                        file_object.write("\n")
