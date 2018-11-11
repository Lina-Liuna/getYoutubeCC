import re
import sys


def mipmap(filename):
    with open(filename+".bak", "w") as targetf:
        lines = []
        with open(filename) as sourcef:
            for line in sourcef:
                line = line.strip().lower()
                if not line:
                    continue

                if re.search(r"^\d+", line):
                    continue
                

                line, _ = re.subn(r"<.*?>", " ", line)

                lines.append(line)
        targetf.write("".join(lines))


if __name__ == "__main__":
    mipmap(sys.argv[1])
