import os

#gives you a list of each file in the directory
files = os.listdir()
print(files)

#gives you current working directory
now = os.getcwd()
print(now)

#join the cwd to file to make the path
for file in files:
    print(os.path.join(now,file))


#note that os.path.join() can take multiple arguments such as
fake_dir = os.path.join('c:', 'users', 'folder', 'file.txt')
print(fake_dir)