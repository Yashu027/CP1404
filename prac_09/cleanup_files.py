import os


def main():

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            fixed_filename = get_fixed_filename(filename)
            print(fixed_filename)


def get_fixed_filename(filename_with_extension):
    data = filename_with_extension.split(".")
    filename = data[0]
    length_of_filename = len(filename)
    index = 1
    while index < length_of_filename:
        current_character = filename[index]
        previous_character = filename[index - 1]
        if current_character.isupper() and previous_character.isalpha():
            filename = filename[:index] + " " + filename[index:]
            length_of_filename = len(filename)
            index += 1
        index += 1
    if len(data) == 2:
        filename = filename.strip().title() + "." + data[1].lower()
    return filename.replace(" ", "_")


if __name__ == '__main__':
    main()
