import csv
import os
import shutil
with open('/Users/samanthahughes/nnUNet/overview.csv', newline='') as csvfile:
    training = []
    validation = []
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        r1 = ', '.join(row)
        id = ""
        for c in r1:
            if c not in {','}:
                id+=c
            else:
                break
        if 'training' in r1:
            training.append(id)
        elif 'validation' in r1:
            validation.append(id)


source_dir = '/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset011_LS/labelsTr'
base_dir = '/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset011_LS/labelsTr'

files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
print(files)
for file in files:
    name, extension = file.split('.')
    print(extension)
    if name not in validation:
        continue
    new_dir = os.path.join(base_dir, 'source')
    os.makedirs(new_dir, exist_ok=True)

    shutil.move(os.path.join(source_dir, file), os.path.join(new_dir, file))

print("Files sorted by extension.")
