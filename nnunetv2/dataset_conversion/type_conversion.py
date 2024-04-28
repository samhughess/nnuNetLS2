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


source_dir = '/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset011_LS/masks'
base_dir = '/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset011_LS/labelsTr'
other = '/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset012_target/labelsTr'

files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
f2 = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
print(len(f2), len(files))
test = []
test2 = []
for file in files:
    name, extension = file.split('.')
    if name in training:
        test.append(file)
        shutil.move(os.path.join(source_dir, file), os.path.join(base_dir, file))
    if name in validation:
        test2.append(file)
        shutil.move(os.path.join(source_dir, file), os.path.join(other, file))

print(len(test), len(test2))
    #new_dir = os.path.join(base_dir, 'source')
    #os.makedirs(new_dir, exist_ok=True)

    #shutil.move(os.path.join(source_dir, file), os.path.join(new_dir, file))

print("Files sorted by extension.")
