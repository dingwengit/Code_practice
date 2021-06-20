"""
A folder can have files and sub-folders

write a function to return file size for a given folder

# get all sizes for all folders
"""


class FileSystem:
    def __init__(self, name, size=0, isFolder=False):
        self.name, self.size, self.isFolder, self.sub_folders = name, size, \
                                                                isFolder, []


def get_all_sizes(node):
    if not node.isFolder:
        return node.size
    if len(node.sub_folders) == 0:
        return 0

    node.size = sum(get_all_sizes(item) for item in node.sub_folders)
    return node.size


root = FileSystem("root", isFolder=True)
root.sub_folders.append(FileSystem("file1", 10))
root.sub_folders.append(FileSystem("file2", 10))
root.sub_folders.append(FileSystem("file3", 10))
sub_folder1 = FileSystem("sub_folder1", isFolder=True)
sub_folder1.sub_folders.append(FileSystem("file1", 5))
sub_folder1.sub_folders.append(FileSystem("file2", 5))
sub_folder1.sub_folders.append(FileSystem("file3", 5))
sub_folder2 = FileSystem("sub_folder2", isFolder=True)
root.sub_folders.append(sub_folder1)
root.sub_folders.append(sub_folder2)

print(get_all_sizes(root))
