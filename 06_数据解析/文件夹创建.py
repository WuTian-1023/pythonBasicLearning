import os

title = '清纯妹子西瓜 - JK校服2'


def create_directory(directory_path):
    try:
        # 如果目录不存在，则创建它
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"目录 '{directory_path}' 已创建。")
        else:
            print(f"目录 '{directory_path}' 已存在。")
    except Exception as e:
        print(f"创建目录时发生错误: {e}")


create_directory(f"./file/image/{title}")
