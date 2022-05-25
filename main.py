import re


class TEXT:
    END = '\033[0m'
    BOLD = '\033[1m'


def bold(intext: str):
    return str(TEXT.BOLD + intext + TEXT.END)


def bionic(intext):
    out = list()
    for item in intext.split(" "):
        if len(item) <= 3:
            x = re.search('^.', item)
            y = re.sub(x.group(0), bold(x.group(0)), item)
            out.append(y)
        elif len(item) > 3:
            x = re.search('^(.*?)[AEIOUaeiou]{0,}..(.*?)[AEIOUaeiou]{0,}', item)
            y = re.sub(x.group(0), bold(x.group(0)), item)
            out.append(y)
    return " ".join(out)