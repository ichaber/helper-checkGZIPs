#!/usr/local/bin/python3
import gzip, os, argparse, zlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    processFolder(args.directory, args.verbose)

def processFolder(dirWithGzip, verbose):
    with os.scandir(dirWithGzip) as entries:
      for entry in entries:
          if entry.is_file():
            if verbose:
              print('Checking: ', entry.name)
            if not isValidGZIPFile(entry):
              print('###File seems to be a bad gz file: ', entry.name)

def isValidGZIPFile(gzFilePath):

    try:
        with gzip.open(gzFilePath, 'r') as openFile:
            #Run through file and see if we can process it.
            fileContent = openFile.read()
            if fileContent != '':
                openFile.close()
                return True
            else:
                return False
    except (OSError, EOFError, zlib.error) as error:
        return False


if __name__ == "__main__":
    main()
