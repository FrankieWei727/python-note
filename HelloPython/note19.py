# files

from pathlib import Path

# Absolute path
path = Path("ecommerce")
print(path.exists())
# make a new directory
# print(path.mkdir())
# remove directory
# print(path.rmdir())


# Relative path

path1 = Path()
for file in path1.glob('*.py'):
    print(file)

