import os
import re

def swap_name_id(file_name):
    pattern = r'(.+)\+([0-9]{17}[0-9xX]).jpg'
    match = re.match(pattern, file_name)
    if match:
        name, id_number = match.groups()
        return f"{id_number}+{name}.jpg"
    else:
        return None

# 让用户输入文件路径
directory_path = input("请输入文件路径：")

# 检查路径是否存在
if not os.path.exists(directory_path):
    print("路径不存在，请输入正确的路径。")
else:
    # 遍历目录中的文件并重命名
    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith('.jpg'):
            new_name = swap_name_id(file_name)
            if new_name:
                os.rename(os.path.join(directory_path, file_name), os.path.join(directory_path, new_name))
                print(f"已重命名：'{file_name}' 更名为 '{new_name}'")
        else:
            print(f"跳过：'{file_name}'")
