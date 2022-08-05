import sys
import argparse
import parse
import json


TEMPLATE = "{} {:.3} {}\r\n"

def parse_file(f, templ=TEMPLATE):
    dic = {}

    for row in f.readlines():
        res = parse.parse(templ, row)

        if res:
            dic[res[1]] = res[2]

    return dic


def perform(args):
    with open(args.input_file, "r", newline="\r\n") as f:
        data = parse_file(f)

    with open(args.output_file, "w") as f:
        json.dump(data, f, indent=4)


def main():
    parser = argparse.ArgumentParser(description='Process CBSE sublists.')
    parser.add_argument('-i', "--input-file", dest='input_file',
                        required=True,
                        help="Input file (CBSE provided TXT)")
    parser.add_argument('-o', "--output-file", dest='output_file',
                        required=True,
                        help=("Output file (generated JSON, use `json` "
                              "module to unserialize in Python"))

    args = parser.parse_args()

    perform(args)


if __name__ == "__main__":
    main()
    
