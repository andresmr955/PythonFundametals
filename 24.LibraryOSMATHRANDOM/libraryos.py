import os
##current working directory
##This is to get the current directory
cwd = os.getcwd()
print(f'Directory of current work {cwd}')

#List files .txt
#"This is the longest way"

'''

txt_files = []
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(file)

print(txt_files)

print(f'Found .txt files: {txt_files}')

'''


##This the right code
txt_files = [file for r, d, f in os.walk('.') for file in f if file.endswith('.txt')]
print(f'Files txt are {txt_files}')


os.rename(r'c:\Users\andre\OneDrive\Desktop\PLATZI2025\PYTHON\21.handlingtxtFiles\tale.txt', 
          r'c:\Users\andre\OneDrive\Desktop\PLATZI2025\PYTHON\21.handlingtxtFiles\talered.txt')
print("File renamed")

##show me again after modifications
txt_files = [file for r, d, f in os.walk('.') for file in f if file.endswith('.txt')]
print(f'Files txt are {txt_files}')