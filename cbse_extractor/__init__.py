import argparse
import json

import cbse_extractor.dextractor as dext
import cbse_extractor.excelifier as efir
import cbse_extractor.helpstrs as h

def main():
    parser = argparse.ArgumentParser(description=h.PROG_DESC,
                                     formatter_class=\
                                          argparse.RawTextHelpFormatter)
    parser.add_argument("-m", "--mode", dest="op_mode",
                        default="combined",
                        help=h.H_MODE)
    parser.add_argument('-i', "--input-file", dest='input_file',
                        required=True,
                        help=h.H_INPUT_FILE)
    parser.add_argument('-o', "--output-file", dest='output_file',
                        required=True,
                        help=h.H_OUTPUT_FILE)
    parser.add_argument('-sd', '--subject-data', dest="subdata_file",
                        default='cbse_subjects.json',
                        help = ("Subject Data JSON file"))
    parser.add_argument('-t1', '--template-1', dest="templ_1",
                        default=dext.TEMPLATE1[:-2],
                        help = ("Subject Data JSON file"))
    parser.add_argument('-t2', '--template-2', dest="templ_2",
                        default=dext.TEMPLATE2[:-2],
                        help = ("Subject Data JSON file"))
    

    args = parser.parse_args()

    if args.op_mode == "to_json":
        dext.perform(args)
    elif args.op_mode == "to_excel":
        efir.perform(args)
    elif args.op_mode == "combined":
        with open(args.input_file, "r", newline="\r\n") as f:
            data = dext.parse_file(f, (args.templ_1+"\r\n",
                                       args.templ_2+"\r\n"))

        with open(args.subdata_file, "r") as f:
            subjects = json.load(f)
            
        ld = efir.convert_to_subcol(data, subjects)
        # print(json.dumps(ld, indent=4))
        efir.save_to_file(ld, args.output_file)
    else:
        raise argparse.ArgumentTypeError(f"Invalid mode '{args.op_mode}'")
