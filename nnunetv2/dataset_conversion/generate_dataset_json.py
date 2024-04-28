from typing import Tuple

from batchgenerators.utilities.file_and_folder_operations import save_json, join

def generate_dataset_json(output_folder: str,
                          channel_names: dict,
                          labels: dict,
                          num_training_cases: int,
                          file_ending: str,
                          regions_class_order: Tuple[int, ...] = None,
                          dataset_name: str = None, reference: str = None, release: str = None, license: str = None,
                          description: str = None,
                          overwrite_image_reader_writer: str = None, **kwargs):
    """
    Generates a dataset.json file in the output folder

    channel_names:
        Channel names must map the index to the name of the channel, example:
        {
            0: 'T1',
            1: 'CT'
        }
        Note that the channel names may influence the normalization scheme!! Learn more in the documentation.

    labels:
        This will tell nnU-Net what labels to expect. Important: This will also determine whether you use region-based training or not.
        Example regular labels:
        {
            'background': 0,
            'left atrium': 1,
            'some other label': 2
        }
        Example region-based training:
        {
            'background': 0,
            'whole tumor': (1, 2, 3),
            'tumor core': (2, 3),
            'enhancing tumor': 3
        }

        Remember that nnU-Net expects consecutive values for labels! nnU-Net also expects 0 to be background!

    num_training_cases: is used to double check all cases are there!

    file_ending: needed for finding the files correctly. IMPORTANT! File endings must match between images and
    segmentations!

    dataset_name, reference, release, license, description: self-explanatory and not used by nnU-Net. Just for
    completeness and as a reminder that these would be great!

    overwrite_image_reader_writer: If you need a special IO class for your dataset you can derive it from
    BaseReaderWriter, place it into nnunet.imageio and reference it here by name

    kwargs: whatever you put here will be placed in the dataset.json as well

    """
    has_regions: bool = any([isinstance(i, (tuple, list)) and len(i) > 1 for i in labels.values()])
    if has_regions:
        assert regions_class_order is not None, f"You have defined regions but regions_class_order is not set. " \
                                                f"You need that."
    # channel names need strings as keys
    keys = list(channel_names.keys())
    for k in keys:
        if not isinstance(k, str):
            channel_names[str(k)] = channel_names[k]
            del channel_names[k]

    # labels need ints as values
    for l in labels.keys():
        value = labels[l]
        if isinstance(value, (tuple, list)):
            value = tuple([int(i) for i in value])
            labels[l] = value
        else:
            labels[l] = int(labels[l])

    dataset_json = {
        'channel_names': channel_names,  # previously this was called 'modality'. I didn't like this so this is
        # channel_names now. Live with it.
        'labels': labels,
        'numTraining': num_training_cases,
        'file_ending': file_ending,
    }

    if dataset_name is not None:
        dataset_json['name'] = dataset_name
    if reference is not None:
        dataset_json['reference'] = reference
    if release is not None:
        dataset_json['release'] = release
    if license is not None:
        dataset_json['licence'] = license
    if description is not None:
        dataset_json['description'] = description
    if overwrite_image_reader_writer is not None:
        dataset_json['overwrite_image_reader_writer'] = overwrite_image_reader_writer
    if regions_class_order is not None:
        dataset_json['regions_class_order'] = regions_class_order

    dataset_json.update(kwargs)

    save_json(dataset_json, join(output_folder, 'dataset.json'), sort_keys=False)

output_folder = "/Users/samanthahughes/nnUNet/nnunetv2/nnuNet_raw/Dataset011_LS"
channel_names = {0: 'T1'}
labels= {'background': 0,
'label1': 1,
 'label2': 2,
 'label3': 3,
 'label4': 4,
 'label5': 5,
 'label6': 6,
 'label7': 7,
 'label8': 8,
 'label9': 9,
 'label10': 10,
 'label11': 11,
 'label12': 12,
 'label13': 13,
 'label14': 14,
 'label15': 15,
 'label16': 16,
 'label17': 17,
 'label18': 18,
 'label19': 19,
 'label20': 20,
 'label21': 21,
 'label22': 22,
 'label23': 23,
 'label24': 24,
 'label25': 25,
 'label26': 26,
 'label27': 27,
 'label28': 28,
 'label29': 29,
 'label30': 30,
 'label31': 31,
 'label32': 32,
 'label33': 33,
 'label34': 34,
 'label35': 35,
 'label36': 36,
 'label37': 37,
 'label38': 38,
 'label39': 39,
 'label40': 40,
 'label41': 41,
 'label42': 42,
 'label43': 43,
 'label44': 44,
 'label45': 45,
 'label46': 46,
 'label47': 47,
 'label48': 48,
 'label49': 49,
 'label50': 50,
 'label51': 51,
 'label52': 52,
 'label53': 53,
 'label54': 54,
 'label55': 55,
 'label56': 56,
 'label57': 57,
 'label58': 58,
 'label59': 59,
 'label60': 60,
 'label61': 61,
 'label62': 62,
 'label63': 63,
 'label64': 64,
 'label65': 65,
 'label66': 66,
 'label67': 67,
 'label68': 68,
 'label69': 69,
 'label70': 70,
 'label71': 71,
 'label72': 72,
 'label73': 73,
 'label74': 74,
 'label75': 75,
 'label76': 76,
 'label77': 77,
 'label78': 78,
 'label79': 79,
 'label80': 80,
 'label81': 81,
 'label82': 82,
 'label83': 83,
 'label84': 84,
 'label85': 85,
 'label86': 86,
 'label87': 87,
 'label88': 88,
 'label89': 89,
 'label90': 90,
 'label91': 91,
 'label92': 92,
 'label93': 93,
 'label94': 94,
 'label95': 95,
 'label96': 96,
 'label97': 97,
 'label98': 98,
 'label99': 99,
 'label100': 100,
 'label101': 101,
 'label102': 102,
 'label103': 103,
 'label104': 104,
 'label105': 105,
 'label106': 106,
 'label107': 107,
 'label108': 108,
 'label109': 109,
 'label110': 110,
 'label111': 111,
 'label112': 112,
 'label113': 113,
 'label114': 114,
 'label115': 115,
 'label116': 116,
 'label117': 117,
 'label118': 118,
 'label119': 119,
 'label120': 120,
 'label121': 121,
 'label122': 122,
 'label123': 123,
 'label124': 124,
 'label125': 125,
 'label126': 126,
 'label127': 127,
 'label128': 128,
 'label129': 129,
 'label130': 130,
 'label131': 131,
 'label132': 132,
 'label133': 133,
 'label134': 134,
 'label135': 135,
 'label136': 136,
 'label137': 137,
 'label138': 138,
 'label139': 139,
 'label140': 140,
 'label141': 141,
 'label142': 142,
 'label143': 143,
 'label144': 144,
 'label145': 145,
 'label146': 146,
 'label147': 147,
 'label148': 148,
 'label149': 149,
 'label150': 150,
 'label151': 151,
 'label152': 152,
 'label153': 153,
 'label154': 154,
 'label155': 155,
 'label156': 156,
 'label157': 157,
 'label158': 158,
 'label159': 159,
 'label160': 160,
 'label161': 161,
 'label162': 162,
 'label163': 163,
 'label164': 164,
 'label165': 165,
 'label166': 166,
 'label167': 167,
 'label168': 168,
 'label169': 169,
 'label170': 170,
 'label171': 171,
 'label172': 172,
 'label173': 173,
 'label174': 174,
 'label175': 175,
 'label176': 176,
 'label177': 177,
 'label178': 178,
 'label179': 179,
 'label180': 180,
 'label181': 181,
 'label182': 182,
 'label183': 183,
 'label184': 184,
 'label185': 185,
 'label186': 186,
 'label187': 187,
 'label188': 188,
 'label189': 189,
 'label190': 190,
 'label191': 191,
 'label192': 192,
 'label193': 193,
 'label194': 194,
 'label195': 195,
 'label196': 196,
 'label197': 197,
 'label198': 198,
 'label199': 199,
 'label200': 200,
 'label201': 201,
 'label202': 202,
 'label203': 203,
 'label204': 204,
 'label205': 205,
 'label206': 206,
 'label207': 207,
 'label208':208,
 'label209':209}
num_training_cases= 360
file_ending= ".mha"

generate_dataset_json(output_folder, channel_names, labels, num_training_cases, file_ending)
