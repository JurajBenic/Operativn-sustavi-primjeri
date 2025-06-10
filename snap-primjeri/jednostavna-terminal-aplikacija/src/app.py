import argparse
import re
import textstat  # Requires: pip install textstat

def main():
    parser = argparse.ArgumentParser(description="Simple text transformation tool")
    parser.add_argument("text", help="Text to transform")
    parser.add_argument("--upper", action="store_true", help="Convert text to uppercase")
    parser.add_argument("--lower", action="store_true", help="Convert text to lowercase")
    parser.add_argument("--reverse", action="store_true", help="Reverse the text")
    parser.add_argument("--capitalize", action="store_true", help="Capitalize the text")
    parser.add_argument("--remove-digits", action="store_true", help="Remove all digits from the text")
    parser.add_argument("--wordcount", action="store_true", help="Count the number of words in the text (using textstat)")

    args = parser.parse_args()
    result = args.text

    if args.upper:
        result = result.upper()
    if args.lower:
        result = result.lower()
    if args.capitalize:
        result = result.capitalize()
    if args.reverse:
        result = result[::-1]
    if args.remove_digits:
        result = re.sub(r'\d+', '', result)

    print("Transformed text:", result)

    if args.wordcount:
        # textstat does not require extra downloads
        print("Word count (textstat):", textstat.lexicon_count(result, removepunct=True))

if __name__ == "__main__":
    main()