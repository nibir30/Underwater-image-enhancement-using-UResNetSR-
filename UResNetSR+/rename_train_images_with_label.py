import os

# folder = r'D:\Thesis\modified_euvp\Paired\underwater_dark\trainB\\'
folder = r'D:\Thesis\UResnet-master\UResnet-master\xxx\path\label\input\\'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + file_name.split(".")[0] + "_label." + file_name.split(".")[1]
    # Renaming the file
    os.rename(source, destination)
    count += 1
