First copy the website of the youtube video you want to handle with, then go to following website:
http://downsub.com
Enter the link of video you want to download then download the subtitles. 

Still not finish yet, 

the srt file contains time and line number in it, we need to write an python file to remove them

import re
import sys


def mipmap(filename):
    with open(filename+".bak", "w") as targetf:
        lines = []
        with open(filename) as sourcef:
            for line in sourcef:
                line = line.strip()
                if not line:
                    continue

                if re.search(r"^\d+", line):
                    continue

                line, _ = re.subn(r"<.*?>", " ", line)
                lines.append(line)
        targetf.write("".join(lines))


if __name__ == "__main__":
    mipmap(sys.argv[1])