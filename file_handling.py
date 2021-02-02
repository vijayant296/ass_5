import sys

def createNewFile(filename):

    #Function to create new file
    try:
        file = open(filename,'x')
        file.close()
    except FileExistsError as error:
        print(error)

def writeToFile(filename,filecontent):

    #To open the file and write the content to it. Also prints the recent incremental data.
    try:
        with open(filename,'a+') as f:
            pos = f.tell()
            f.write('\n' + filecontent)
            f.seek(pos)
            print(f.read())
    except Exception as e:
        print("Exception while writing "+str(e))
    finally:
        f.close()

def readFile(filename):

    #Reads the content of the file
    try:
        with open(filename,'r') as f:
            print(f.read())
    except:
        print("Exception while reading the file.")
    finally:
        f.close()

def searchData(data,filename):

    #Searches for a string in the file.
    try:
        with open(filename,'r') as f:
            for line in f:
                if data in line:
                    print(data + " is found")
                    break

            else:
                print(data+" is not found")
    except:
        print("Exception while searching for the data.")
    finally:
        f.close()

def writeToAnotherFile(source,destination):

    # Copies the content of source file to the destination file.
    try:
        with open(source, 'r') as s, open(destination, 'a') as d:
            for line in s:
                # append content to second file
                d.write(line)
    except:
        print("Exception while copying contents")
    finally:
        s.close()
        d.close()


if __name__ == "__main__":

    print("Choices for operation are: \n 1.Create a new file\n 2.Write a content to the file and read incremental data\n 3.Open and read a file content\n "
          "4.Search a string in the file\n 5.Copy one file content to another file\n 6.Exit")

    case = int(input("Enter your choice of opeartion in digit:----->"))

    if case == 1:
        filename = input("enter name of the file to be created:------> ")
        createNewFile(filename)

    elif case == 2:
        filecontent = input("Enter the content to be written on the file:----->  ")
        filename = input("Enter the filename where content needs to be written:-------> ")
        writeToFile(filename,filecontent)

    elif case == 3:
        filename = input("Enter the filename to be read:------> ")
        readFile(filename)

    elif case == 4:
        data = input("Enter the string to be searched:--------> ")
        filename = input("Enter the filename to be searched:------> ")
        searchData(data,filename)

    elif case == 5:
        filename = input("Enter the filename to be copied:------> ")
        dest = input("Enter the filename where the content needs to be written:-----------> ")
        writeToAnotherFile(filename,dest)

    elif case == 6:
        sys.exit()

    else:
        print("Invalid case entered. Please enter the correct choice of operation.")