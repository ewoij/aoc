def get_path(items):
    return '/'.join(items).replace('//', '/')


def build_tree(lines):
    dir_stack = []
    dirs = {}
    file_sizes = {}

    for line in lines:
        if line.startswith("$ cd .."):
            dir_stack.pop()
        elif line.startswith("$ cd "):
            dir_ = line[len("$ cd "):]
            dir_stack.append(dir_)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            item = line[len("dir "):]
            dirs.setdefault(get_path(dir_stack), set()).add(item)
        else:
            size, item = line.split()
            size = int(size)
            dirs.setdefault(get_path(dir_stack), set()).add(item)
            file_sizes[get_path(dir_stack + [item])] = size

    return dirs, file_sizes


def build_dir_sizes(curr, dirs, file_sizes, dir_sizes):
    is_file = get_path(curr) in file_sizes
    if is_file:
        return file_sizes[get_path(curr)]

    total_size = 0
    for item in dirs.get(get_path(curr), set()):
        total_size += build_dir_sizes(curr + [item], dirs, file_sizes, dir_sizes)

    dir_sizes[get_path(curr)] = total_size

    return total_size


lines = open('2022/day/7/input').read().splitlines()

dirs, file_sizes = build_tree(lines)
dir_sizes = {}
build_dir_sizes(['/'], dirs, file_sizes, dir_sizes)

# for d in dir_sizes:
#     if dir_sizes[d] <= 100_000:
#         print(d, dir_sizes[d])
# 
# print(sum(dir_sizes[d] for d in dir_sizes if dir_sizes[d] <= 100_000))
# # 1_325_919

disk_space = 70_000_000
used_space = dir_sizes['/']
free_space = disk_space - used_space
min_space_needed = 30_000_000
space_to_cleanup = min_space_needed - free_space

print("disk_space", disk_space)
print("used_space", used_space)
print("free_space", free_space)
print("min_space_needed", min_space_needed)
print("space_to_cleanup", space_to_cleanup)

for v in sorted(dir_sizes[d] for d in dir_sizes if dir_sizes[d] >= space_to_cleanup):
    print(v)
