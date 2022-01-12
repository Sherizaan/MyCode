username = input("Enter username:")
print("Username is: " + username)
#"a" - Append - will append to the end of the file

#"w" - Write - will overwrite any existing content
f = open("TextFile.txt", "a")
#\n means new line
f.write("\n"+username)
f.close()

