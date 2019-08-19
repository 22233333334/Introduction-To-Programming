#   Open a file to read from
f = open("numbers1.txt","r")
g = open("numbers2.txt","r")

#   Create an empty variable to store the contents from the two text files
contentsNumbers1 = ""
contentsNumbers2 = ""

#   Copy contents from the two text files and save in the variable
for line in f:
    contentsNumbers1 = contentsNumbers1 + line
for line in g:
    contentsNumbers2 = contentsNumbers2 + line

#   Close the two files
f.close()
g.close()

#   Splits contents to get into list format
contentsNumbers1 = contentsNumbers1.split()
contentsNumbers2 = contentsNumbers2.split()

#   Combine the contents of the two text files together
contents = (contentsNumbers1 + contentsNumbers2)

#   Sort the contents into numerical order
contents.sort(key=int)

#   Open the third file to write the contents to
ofile = open("allNumbers.txt", "w")
ofile.write(str(contents))

#   Close the third file
ofile.close() 
