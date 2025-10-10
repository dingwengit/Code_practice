"""
A folder can have files and sub-folders

write a function to return file size for a given folder

# get all sizes for all folders

root(d)
  f1
  f2
  f3
  sf1(d)
     f1
     f2
     f3
     sf2(d)
"""
class item:
    def __init__(self, name, size=0):
        self.name, self.size = name, size

class folder:
    def __init__(self, files=[], sub_folders=[]):
        self.files = files
        self.sub_folders = sub_folders

def get_all_sizes(fd):
    total_size = 0
    total_size += sum([f.size for f in fd.files])
    for s_f in fd.sub_folders:
        total_size += get_all_sizes(s_f)
    return total_size

f1 = folder(files=[item("file1", 10), item("file1", 10)])
f2 = folder(files=[item("file2", 3), item("file2", 3)])
r = folder(files=[item("file2", 2), item("file2", 3)], sub_folders=[f1, f2])

print(get_all_sizes(r))
