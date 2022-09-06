import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    print(f"Now I need to process the records in {args.fastq}")

    for line in args.fastq:
        if line.startswith('@'):
            print(line[1:].strip())
            
if __name__ == '__main__':
    main()
