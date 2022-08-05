import json
import argparse
from collections import defaultdict

import pandas as pd

# from cbse_converter.dextractor import parse_file as parse_text


def convert_to_linear_dict(records, no_of_subjects=5):
    # The columns
    roll = []
    gender = []
    name = []
    subjs = []
    marks = []
    grades = []

    for i in range(no_of_subjects):
        subjs.append([])
        marks.append([])
        grades.append([])
    
    grade1 = []
    grade2 = []
    grade3 = []
    result = []

    for roll_no, data in records.items():
        roll.append(roll_no)
        gender.append(data["gender"])
        name.append(data["name"])

        subdatav = tuple(data["subjects"].values())
        subdatak = tuple(data["subjects"].keys())
        for i in range(no_of_subjects):
            subjs[i].append(subdatak[i])
            marks[i].append(subdatav[i][0])
            grades[i].append(subdatav[i][1])

        grade1.append(data["other_grades"][0])
        grade2.append(data["other_grades"][1])
        grade3.append(data["other_grades"][2])
            
        result.append(data["status"])

    retdict = {}

    retdict["Roll No"] = roll
    retdict["Sex"] = gender
    retdict["Name"] = name

    for i in range(no_of_subjects):
        retdict[f"SubjectCode_{i+1}"] = subjs[i]
        retdict[f"Marks_{i+1}"] = marks[i]
        retdict[f"Grade_{i+1}"] = grades[i]

    retdict["EC_Grade1"] = grade1
    retdict["EC_Grade2"] = grade2
    retdict["EC_Grade3"] = grade3

    retdict["Result"] = result

    return retdict


def convert_to_subcol(records, subjects):
    # The columns
    roll = []
    gender = []
    name = []
    # subjs = {}

    # Flag to ignore empty cols
    s_flag = set()
    
    marks = {}
    grades = {}

    for i in subjects:
        # i is subject code
        # subjs[i] = []
        marks[i] = []
        grades[i] = []
    
    grade1 = []
    grade2 = []
    grade3 = []
    result = []

    for roll_no, data in records.items():
        roll.append(roll_no)
        gender.append(data["gender"])
        name.append(data["name"])

        # subdatav = tuple(data["subjects"].values())
        subdatak = tuple(data["subjects"].keys())

        for scode in subjects:
            if scode in subdatak:
                marks[scode].append(data["subjects"][scode][0])
                grades[scode].append(data["subjects"][scode][1])

                # flag
                s_flag.add(scode)
            else:
                marks[scode].append(None)
                grades[scode].append(None)

        grade1.append(data["other_grades"][0])
        grade2.append(data["other_grades"][1])
        grade3.append(data["other_grades"][2])
            
        result.append(data["status"])

    retdict = {}

    retdict["Roll"] = roll
    retdict["Gender"] = gender
    retdict["Name"] = name

    for scode in subjects:
        if scode in s_flag:
            sname = subjects[scode]

            retdict[f"{sname}_({scode})_Marks"] = marks[scode]
            retdict[f"{sname}_({scode})_Grades"] = grades[scode]
        

    retdict["EC_Grade1"] = grade1
    retdict["EC_Grade2"] = grade2
    retdict["EC_Grade3"] = grade3

    retdict["Result"] = result

    return retdict


def save_to_file(data, filename):
    df = pd.DataFrame(data)

    
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()


def perform(args):
    with open(args.input_file, "r") as f:
        data = json.load(f)

    if args.op_mode == "1":
        ld = convert_to_linear_dict(data)
    elif args.op_mode == "2":
        with open(args.subdata_file, "r") as f:
            subjects = json.load(f)
        ld = convert_to_subcol(data, subjects)
    
    # print(json.dumps(ld, indent=4))
    save_to_file(ld, args.output_file)


def main():
    parser = argparse.ArgumentParser(description='Process CBSE ranklists.')
    parser.add_argument('-i', "--input-file", dest='input_file',
                        required=True,
                        help="Input file (Generated JSON)")
    parser.add_argument('-o', "--output-file", dest='output_file',
                        required=True,
                        help=("Output file (generated XLSX, use `pandas` "
                              "module to unserialize in Python"))
    parser.add_argument('-m', '--mode', dest="op_mode",
                        default='1',
                        help = ("1 - Old mode, 2 - New mode"))
    parser.add_argument('-d', '--subject-data', dest="subdata_file",
                        default='cbse_subjects.json',
                        help = ("Subject Data JSON file"))

    args = parser.parse_args()

    perform(args)
    """
    with open(args.input_file, "r") as f:
        data = json.load(f)

    ld = convert_to_linear_dict(data)
    # print(json.dumps(ld, indent=4))
    save_to_file(ld, args.output_file)
    """


if __name__ == "__main__":
    main()
