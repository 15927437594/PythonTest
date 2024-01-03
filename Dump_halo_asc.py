import os

path = os.path.join(os.getcwd(), 'log_halo_asc')
timestamp = None
is_first = True
for root, _, files in os.walk(path):
    for file_name in files:
        print(root, file_name)
        file_path = os.path.join(root, file_name)
        print(file_path)
        with open(file_path, encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                if line.__contains__("CANFD 1 487"):
                    if is_first:
                        timestamp = float(line.split(" ")[0])
                        is_first = False
                    else:
                        print(timestamp)
                        timestamp_str = line.split(" ")[0]
                        timestamp = (int(timestamp * 1000) + 20) / 1000
                        print(timestamp)
                        dot_str_split = str(timestamp).split(".")
                        dot_str = dot_str_split[1]
                        print(dot_str)
                        while len(dot_str) < 6:
                            dot_str = dot_str + "0"
                        replace_timestamp = dot_str_split[0] + "." + dot_str
                        line = line.replace(timestamp_str, str(replace_timestamp))
                        print(line)
                    filename = os.path.join(path, 'output_Photo_listen.asc')
                    line = line.replace("Rx", "Tx")
                    with open(filename, 'a') as file_object:
                        file_object.write(line)
