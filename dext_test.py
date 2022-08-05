import sys
import argparse
import parse
import json

TEMPLATE1="{:8d}   {:<} {:3d}     {:3d}     {:3d}     {:3d}     {:3d}              {} {} {}    {:.4}                      \r\n"
TEMPLATE2 = "                                                                {:3d}  {:.2} {:3d}  {:.2} {:3d}  {:.2} {:3d}  {:.2} {:3d}  {:.2}        \r\n"

def parse_file(fname=sys.argv[1], templ=(TEMPLATE1, TEMPLATE2)):
    with open(fname, "r", newline="\r\n") as f:
        dic = {}

        prev = None
        for row in f.readlines():
            res1 = parse.parse(templ[0], row)
            res2 = parse.parse(templ[1], row)
            
            if res1:
                subdic = {
                        "name": res1[1],
                        "subjects": dict.fromkeys(res1[2:7]),
                        "grades": res1[7:10],
                        "status": res1[10]
                    }
                dic[res1[0]] = subdic
                prev = res1[0]
            elif res2 and prev:
                i = 0
                for sub in dic[prev]["subjects"]:
                    # print(prev)
                    dic[prev]["subjects"][sub] = (res2[i], res2[i+1])
                    i += 2
                prev = None
            # else:
                # prev = None

    return dic

def main():
    parser = argparse.ArgumentParser(description='Process CBSE ranklists.')
    parser.add_argument('-i', "--input-file", dest='input_file',
                        help="Input file (CBSE provided TXT)")
    parser.add_argument('-o', "--output-file", dest='output_file',
                        help=("Output file (generated JSON, use `json` module to "
                              "unserialize in Python"))

    args = parser.parse_args()

    data = parse_file(args.input_file)

    with open(args.output_file, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
    
