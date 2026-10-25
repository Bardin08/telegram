"""Check generated themes against the parsers of the apps that load them.

tdesktop: ReadPaletteValues in Telegram/SourceFiles/window/themes/window_theme.cpp
reads `name: value;` entries after stripping comments and rejects the whole
file on the first malformed entry.

Android: getThemeFileValues in TMessagesProj/.../ActionBar/Theme.java splits
each line at `=` without trimming and reads colours with Color.parseColor,
which takes #rrggbb or #aarrggbb. Lines without `=` are silently ignored.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = re.compile(r"[A-Za-z0-9_]+")
ANDROID_LINE = re.compile(r"[A-Za-z0-9_]+=#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{8})")


def strip_comments(text):
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    return re.sub(r"//[^\n]*", " ", text)


def skip_space(data, pos):
    while pos < len(data) and data[pos].isspace():
        pos += 1
    return pos


def tdesktop_error(text):
    data = strip_comments(text)
    pos = skip_space(data, 0)
    while pos < len(data):
        name = NAME.match(data, pos)
        if not name:
            return f"could not read a name at {data[pos:pos + 30]!r}"
        pos = skip_space(data, name.end())
        if pos == len(data) or data[pos] != ":":
            return f"expected ':' after {name.group()!r}"
        pos = skip_space(data, pos + 1)
        if pos < len(data) and data[pos] == "#":
            pos += 1
        value = NAME.match(data, pos)
        if not value:
            return f"expected a value for {name.group()!r}"
        pos = skip_space(data, value.end())
        if pos == len(data) or data[pos] != ";":
            return f"expected ';' after {name.group()!r}"
        pos = skip_space(data, pos + 1)
    return None


def android_error(text):
    for number, line in enumerate(text.splitlines(), 1):
        if line and not ANDROID_LINE.fullmatch(line):
            return f"line {number} is not key=#rrggbb or key=#aarrggbb: {line!r}"
    return None


CHECKS = {"*.tdesktop-palette": tdesktop_error, "*.attheme": android_error}


def main():
    failed = False
    checked = 0
    for pattern, check in CHECKS.items():
        for path in sorted(ROOT.glob(f"src/*/{pattern}")):
            checked += 1
            error = check(path.read_text())
            if error:
                failed = True
                print(f"{path.relative_to(ROOT)}: {error}")
    if checked == 0:
        print("no generated desktop or Android themes found")
        return 1
    print(f"checked {checked} files")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
