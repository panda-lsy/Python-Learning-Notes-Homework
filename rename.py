import os

def replace_spaces_with_underscores(directory):
    # 遍历目录中的所有文件和子目录
    for root, dirs, files in os.walk(directory, topdown=False):
        # 先处理文件
        for name in files:
            if ' ' in name or ']' in name or '[' in name:
                old_file = os.path.join(root, name)
                new_name = name.replace(' ', '_').replace(']', '_').replace('[', '')
                new_file = os.path.join(root, new_name)
                os.rename(old_file, new_file)
                print(f'Renamed file: {old_file} -> {new_file}')
        
        # 然后处理目录
        for name in dirs:
            if ' ' in name:
                old_dir = os.path.join(root, name)
                new_name = name.replace(' ', '_')
                new_dir = os.path.join(root, new_name)
                os.rename(old_dir, new_dir)
                print(f'Renamed directory: {old_dir} -> {new_dir}')

if __name__ == "__main__":
    directory = os.getcwd()
    replace_spaces_with_underscores(directory)