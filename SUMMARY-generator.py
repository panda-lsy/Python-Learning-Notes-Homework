import os


def generate_summary(root_dir):
    # 创建或清空SUMMARY.md文件
    with open(os.path.join(root_dir, 'SUMMARY.md'), 'w',encoding='utf-8') as summary_file:
        summary_file.write('# Summary\n\n')

        # 遍历根目录下的所有子目录
        for subdir, dirs, files in os.walk(root_dir):
            # 排除 venv 和 .git 文件夹
            if 'venv' in dirs:
                dirs.remove('venv')
            if '.git' in dirs:
                dirs.remove('.git')

            if subdir == root_dir:
                continue

            # 获取当前子目录的相对路径
            subdir_ = subdir.replace('_', ' ')
            relative_path = os.path.relpath(subdir, root_dir)
            relative_path_ = os.path.relpath(subdir_, root_dir)

            # 写入子目录标题到SUMMARY.md
            summary_file.write(f'## {relative_path_}\n\n')

            # 遍历子目录中的所有Markdown文件
            for file in files:
                if file.endswith('.md') and file != 'SUMMARY.md':
                    file_path = os.path.join(relative_path, file)
                    file_title = os.path.splitext(file)[0]
                    file_title = file_title.replace('_', ' ')
                    summary_file.write(f'- [{file_title}]({file_path})\n')

            summary_file.write('\n')


if __name__ == '__main__':
    root_directory = os.getcwd()
    generate_summary(root_directory)
    print("SUMMARY.md 已生成。")