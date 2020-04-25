import os

def func_correction(input_file):
    read_file = open(input_file, "r")

    output_file = open("temp.srt", "w")

    text = False

    for line in read_file:
        try:
            if type(int(line)) == int and text == False:
                output_file.write(line)

            else:
                output_file.write("")
                text = False

        except:
            if len(line) > 1:

                output_file.write(line)
                text = True
            else:
                output_file.write(line)

    output_file.close()

    os.rename(r"./temp.srt", input_file)

def main():
    dirName = input("Insert the root folder you want to change .srt files: \n\n")

    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    # Subtitle correction
    n = 0
    for elem in listOfFiles:
        file_extension = elem.split(".")[-1]
        if file_extension == "srt":
            func_correction(elem)
            n+=1
    print(n,"corrected files")


if __name__ == '__main__':
    main()