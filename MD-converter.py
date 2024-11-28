import os
import nbformat
from nbconvert import MarkdownExporter


def convert_notebooks_to_markdown(root_dir):
    # 创建Markdown导出器
    exporter = MarkdownExporter()

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.ipynb'):
                ipynb_path = os.path.join(subdir, file)
                md_path = os.path.splitext(ipynb_path)[0] + '.md'

                with open(ipynb_path, 'r', encoding='utf-8') as f:
                    content = nbformat.read(f, as_version=4)

                md_content, _ = exporter.from_notebook_node(content)

                # 在每个代码块后添加 "Program" 注释
                md_content = md_content.replace("```python", "```python\n# Program")

                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(md_content)

                print(f"Converted {ipynb_path} to {md_path}")


if __name__ == "__main__":
    root_directory = os.getcwd()  # 使用当前工作目录作为根目录
    convert_notebooks_to_markdown(root_directory)