#write in file using operations function    
with open('sample.txt', 'r')  as file
file.write("Hi I am Gyan and I am 6009 years old.")
file.close()

#split file into words
with open('sample.txt', 'r')
    data = file.readings()
    print("Word in this file are...")
    for line in data:
        word = line.split()
        print(word)
    file.close