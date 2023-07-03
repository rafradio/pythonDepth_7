import sys
from DirsAndFiles import DirsAndFiles as DF

def main(args):
    data = args[1] if len(args) > 1 else 'txt'
    df = DF(data)
    df.createSecondDir()
    df.copyDirs('firstdir')

if __name__ == '__main__':
    main(sys.argv)