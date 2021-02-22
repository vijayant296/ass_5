Knowledge of file handling.

Problem Statement:
-------------------
Write sample file handling program that covers file operations like Create a new file, Open an existing file, Read file contents, Search data on a file, Write into a new file, Close a file.
e.g. 
Program Statement: Read incremental data from one or more files of at least 2 types of data exists in a directory. Save incremantal data to one specific type of target file.  Program to run in loop. 
Dir: type1_file1.txt, type2_file2.txt, type1_file2.txt, type1_file3.txt
Target file: type1.txt, type2.txt
Input: provide input directory or one or more files, time interval, provide exception word lists.
Screen output: Display total and incremental number of words written to target file. Total Exception words and words in incremental data. Show incremental content written to target file.

File Handling Operations

1.Create a file: Opening a file in "x" mode creates a file and returns error if the file exist.

Open a file: We use open () function in Python to open a file in read or write mode.

     open(filename, mode)
     
     - Mode:
      1. “ r “, for reading.
      2. “ w “, for writing.
      3. “ a “, for appending.
      4. “ r+ “, for both reading and writing
2.Read from file: The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.

     file.read([size])
3.Write to a file: The write() write the specified text or bytes to the file. It overwrites the previous data in file.

     file.write('content to write')
4.Append to a file: Opening the file in 'a' or 'a+' mode positions the handle at the end of the file. The data being written will be inserted at the end, after the existing data.

Python File Methods
There are various methods available with the file object. Some of them have been used in the above examples.

Here is the complete list of methods in text mode with a brief description:

Method	Description
close()	Closes an opened file. It has no effect if the file is already closed.
detach()	Separates the underlying binary buffer from the TextIOBase and returns it.
fileno()	Returns an integer number (file descriptor) of the file.
flush()	Flushes the write buffer of the file stream.
isatty()	Returns True if the file stream is interactive.
read(n)	Reads at most n characters from the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Writes the string s to the file and returns the number of characters written.
writelines(lines)	Writes a list of lines to the file.
