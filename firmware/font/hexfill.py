# The MIT License (MIT)

# Copyright (c) 2021 Tom J. Sun

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys

height = int(sys.argv[2])

with open(sys.argv[1], "r") as input_file:
    # Read in a hex formatted bitmap font file
    lines = input_file.readlines()
    # Zero out > height pixel width characters since they can't be scaled down
    lines = list(
        map(
            lambda line: line.split(":")[0] + ":" + ("0" * 2 * height) + "\n"
            if len(line) > height * 2 + 6
            else line,
            lines,
        )
    )
    # Pad < height pixel width chars with leading 0s
    lines = list(
        map(
            lambda line: line[:5]
            + ("0" * ((height * 2 + 6) - len(line)))
            + line[5 : len(line)]
            if len(line) < height * 2 + 6
            else line,
            lines,
        )
    )
    # Add missing characters (zero'd out) so the codepoint sequence is contiguous
    i = 0
    while i < len(lines):
        codepoint = int(lines[i].split(":")[0], 16)
        while i < codepoint:
            lines.insert(i, ("%04X" % i) + ":" + ("0" * 2 * height) + "\n")
            i += 1
        i += 1
    print("".join(lines))