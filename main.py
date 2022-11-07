from argparse import ArgumentParser
from backends.factory import create_serializer

parser = ArgumentParser()
parser.add_argument("-b", "backend", type=str, default="xml.gz")
parser.add_argument("filename")

def main():
    args = parser.parse_args()
    serializer = create_serializer(args.backend, args.filename)
    serializer.write()


if __name__ == "__main__":
    main()