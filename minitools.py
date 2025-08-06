import os

def generate_tree(directory, padding="", exclude_folders=None):
    """
    生成目录树
    :param directory: 要遍历的目录
    :param padding: 当前行的缩进
    :param exclude_folders: 需要排除的文件夹列表
    """
    if exclude_folders is None:
        exclude_folders = []

    # 获取目录下的所有文件和文件夹
    entries = sorted(os.listdir(directory))

    # 遍历每个条目
    for i, entry in enumerate(entries):
        # 获取完整路径
        path = os.path.join(directory, entry)

        # 如果是需要排除的文件夹，跳过
        if os.path.isdir(path) and entry in exclude_folders:
            continue

        # 判断是文件还是文件夹
        if i < len(entries) - 1:
            # 如果不是最后一个条目，使用分支符号
            print(padding + "├── " + entry)
            if os.path.isdir(path):
                # 如果是文件夹，递归生成子目录树
                generate_tree(path, padding + "│   ", exclude_folders)
        else:
            # 如果是最后一个条目，使用叶子符号
            print(padding + "└── " + entry)
            if os.path.isdir(path):
                # 如果是文件夹，递归生成子目录树
                generate_tree(path, padding + "    ", exclude_folders)

if __name__ == "__main__":
    # 获取当前目录作为根目录
    root_directory = os.getcwd()
    # 指定需要排除的文件夹
    exclude_folders = [".git", "__pycache__", ".vscode"]
    print(root_directory)
    generate_tree(root_directory, exclude_folders=exclude_folders)