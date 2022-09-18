import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        os.rename(filename, "{}/{}".format(extension, filename))
        print("{} is moved to {} folder.".format(filename, extension))


main()
