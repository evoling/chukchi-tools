#!/usr/bin/env python3
"""
Convert Chukchi IPA transcription to Cyrillic orthography or back
"""
import argparse
import fileinput
import sys
import warnings

# Destination for warning messages
WARNINGS = sys.stderr # open("transliteration-warnings.txt", "w")

# Add everything here that you want to allow to pass through without
# transliteration
IGNORE_CHARS = {".", ",", "-", "?"}

def main():
    global fail
    def fail(word):
        warnings.showwarning('failed',
                TransliterationWarning, 
                fileinput.filename(),
                fileinput.filelineno(),
                file=WARNINGS)

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--to-cyrillic", dest="funct", action="store_const",
            const=to_cyrillic, default=to_ipa, help="""Convert IPA
            transcription into Cyrillic orthography [default: Cyrillic
            to IPA]""")
    parser.add_argument("files", metavar="FILE", nargs="*", help="""Input
            files. Leave empty to read from stdin""")
    args = parser.parse_args()

    for line in fileinput.input(files=args.files):
        for word in line.strip().split():
            print(args.funct(word), end=" ")
        print()
    return


class TransliterationError(Exception):
    pass

class TransliterationWarning(Warning):
    pass

# this is overridden in the main() function by a warning
def fail(msg):
    raise TransliterationError(msg)


CONSONANTS = {
        "в":"w",
        "г":"ɣ",
        "й":"j",
        "к":"k",
        "ԓ":"l",
        "м":"m",
        "н":"n",
        "п":"p",
        "р":"r",
        "с":"c",
        "т":"t",
        "у":"u",
        "ч":"c",
        "ӄ":"q",
        "ӈ":"ŋ",
        }

SOFT_CONSONANTS = {"ԓ", "ч"}

UNJOTATED_VOWELS = {
        "э":"e",
        "у":"u",
        "а":"a",
        "о":"o",
        "и":"i",
        "ы":"ə",
        }

JOTATED_VOWELS = {
        "е":"e",
        "ю":"u",
        "я":"a",
        "ё":"o",
        }

VOWELS = UNJOTATED_VOWELS.keys() | JOTATED_VOWELS.keys()

HARDSOFT = {"ъ", "ь"}

ALTERNATE_ORTHOG = { # for normalisation
        "қ":"ӄ",
        "ӊ":"ӈ",
        "ң":"ӈ",
        "ӆ":"ԓ",
        "л":"ԓ",
        "’":"'",
        }

def reverse_dict(D):
    return dict(zip(D.values(), D.keys()))

IPA_JOTATED_VOWELS = reverse_dict(JOTATED_VOWELS)
IPA_UNJOTATED_VOWELS = reverse_dict(UNJOTATED_VOWELS)
IPA_VOWELS = IPA_UNJOTATED_VOWELS.keys()
IPA_CONSONANTS = reverse_dict(CONSONANTS)
IPA_CONSONANTS["c"] = "ч" #  make sure we've got the right default allograph

def normalise(s, mapping=ALTERNATE_ORTHOG):
    s = s.lower()
    for key, value in mapping.items():
        s = s.replace(key, value)
    return s

def to_ipa(s):
    prev_char = None
    result = list()
    for char in normalise(s):
        if char in UNJOTATED_VOWELS:
            if prev_char in HARDSOFT:
                result.append("ʔ")
                result.append(UNJOTATED_VOWELS[char])
            else:
                result.append(UNJOTATED_VOWELS[char])
        elif char in JOTATED_VOWELS:
            if prev_char in SOFT_CONSONANTS:
                result.append(JOTATED_VOWELS[char])
            elif prev_char in {None, "'"} | HARDSOFT | VOWELS:
                result.append("j")
                result.append(JOTATED_VOWELS[char])
            else:
                fail(s)
                return s
                
        elif char in CONSONANTS:
            result.append(CONSONANTS[char])
        elif char == "'":
            result.insert(-1, "ʔ") 
        elif char in HARDSOFT:
            pass
        elif char in IGNORE_CHARS:
            result.append(char)
        else:
            fail(s)
            return s
        prev_char = char
    return "".join(result)

def to_cyrillic(s):
    result = list()
    append_apostrophe = False
    for i, char in enumerate(s):
        if i == 0:
            prev_char = None
        else:
            prev_char = s[i-1]
        try:
            next_char = s[i+1]
        except IndexError:
            next_char = None

        # GLOTTAL STOP
        if char == "ʔ":
            assert next_char in IPA_VOWELS
            if prev_char in IPA_VOWELS or prev_char is None:
                # do nothing yet: write apostrophe after next char
                append_apostrophe = True
                pass
            elif prev_char in  {"l","c"}:
                result.append("ь")
            else:
                result.append("ъ")

        # VOWELS
        elif char in IPA_VOWELS:
            if prev_char == "ʔ":
                result.append(IPA_UNJOTATED_VOWELS[char])
                if append_apostrophe:
                    result.append("'")
                    append_apostrophe = False
            elif prev_char in {"l", "j"} and char in set("eaou"):
                result.append(IPA_JOTATED_VOWELS[char])
            elif prev_char == "c" and char == "e":
                result.append(IPA_JOTATED_VOWELS[char])
            else:
                result.append(IPA_UNJOTATED_VOWELS[char])

        # JOT
        elif char == "j":
            if next_char in IPA_VOWELS:
                if next_char in {"i", "ə"}:
                    result.append("й")
                else:
                    if prev_char in  {"l","c"}:
                        result.append("ь")
                    elif prev_char in IPA_CONSONANTS:
                        result.append("ъ")
            else:
                result.append("й")

        # CH
        elif char == "c":
            if next_char == "q":
                result.append("с") # CYRILLIC SMALL LETTER ЕS
            else:
                result.append("ч")

        # OTHER CONSONANTS
        elif char in IPA_CONSONANTS:
            result.append(IPA_CONSONANTS[char])

        # PUNCTUATION and WHATNOT
        elif char in IGNORE_CHARS:
            results.append(char)

        else:
            fail(s)
            return s

    return "".join(result)

if __name__ == "__main__":
    main()
