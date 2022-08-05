PROG_DESC = """Process the CBSE Gazzetes.

This program can process CBSE gazzetes, given the input format for two lines,
i.e. the name line and the marks line. The format can be provided as arguments,
as mentioned below.

The tool can be used to convert the text files into useful Excel data.

The functions used in this module can also be imported and incorporated into
other programs, thus making it truly extensible.

===COPYRIGHT NOTICE===

Copyright © 2022 Advaith Menon

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in the
Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

H_MODE = """The mode in which the program should operate.

`to_json` - Converts the text file to JSON.
`to_excel` - Converts the JSON file to Excel.
`combined` - Converts the text file to Excel.
"""

H_INPUT_FILE = ("The input file. Type depends upon mode chosen. "
                "File extension must be included in the file name.")

H_OUTPUT_FILE = ("The output file. Type depends upon mode chosen. "
                "File extension must be included in the file name.")
