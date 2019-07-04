import os
import shutil
#import subprocess
import os


#method to get all the list of files and folders inside the given directory
def getListOfFiles(stringDir):
    # create a list of file and sub directories 
    try:
        listOfFile = os.listdir(stringDir)
    
    except ValueError:
        print("Error! an unkown error occured")
    
   
    return listOfFile  

#copy the files to the specified directory
def copyfiles(filename,copyTo):
    try:
        shutil.copy(filename, copyTo)
        #print(newPath)
    except ValueError:
        print("Error! an unkown error accured")
   
#method to run the bat file
def runBatfiles(path):
    
    try:
        #path = "D:/Users/Bran.mashabela/Desktop/runtest";
        listOfFolders=getListOfFiles(path)

        for folder in listOfFolders:
            os.chdir(path+"/"+folder)
            os.startfile("Lab_Archive.bat")
            
    except ValueError: 
        print("Error! an unkown error occured")
    

def main():
    #the directory of the origional folder
    workingdirName=os.getcwd()
    dirName = workingdirName.replace("\\", "/")
    #dirName = 'C:/work/run bat';
    inputPath = input("Please enter the path to save the new folders: ")
    folderPath = inputPath.replace("\\", "/")
    #folderPath = 'D:/Users/Bran.mashabela/Desktop/runtest/';
    secondElement='';
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    if os.path.isdir(folderPath):

        # Print the files
        for elem in listOfFiles:
            currentfile=elem;
            firstElement=elem[0:8];

            filetoCopy = dirName+"/"+currentfile;
            copyLocation = folderPath+"/"+firstElement+"/"+currentfile;

            try: 
                #create a new folder if the date changes 
                if firstElement != secondElement and firstElement.isnumeric():
                    folderName=folderPath+"/"+firstElement
                    os.mkdir(folderName)
                    
                else:
                    print('Folders not created');

                #list of the specified directories
                listOfFolders=getListOfFiles(folderPath)
                listOfBatfiles=getListOfFiles(dirName+'/Scripts');

                for folder in listOfFolders:
                    if firstElement == folder:
                        #copy files with the same name to the same location
                        copyfiles(filetoCopy,copyLocation);
                    #copy all the files in scripts folder the first parameter is the dir/name of the file and the secon one is the dir/name to copy the files to 
                    copyfiles(dirName+"/Scripts/"+listOfBatfiles[0],folderPath+"/"+firstElement+"/"+listOfBatfiles[0]);
                    copyfiles(dirName+"/Scripts/"+listOfBatfiles[1],folderPath+"/"+firstElement+"/"+listOfBatfiles[1]);
                    copyfiles(dirName+"/Scripts/"+listOfBatfiles[2],folderPath+"/"+firstElement+"/"+listOfBatfiles[2]);
                    copyfiles(dirName+"/Scripts/"+listOfBatfiles[3],folderPath+"/"+firstElement+"/"+listOfBatfiles[3]);
                    copyfiles(dirName+"/Scripts/"+listOfBatfiles[4],folderPath+"/"+firstElement+"/"+listOfBatfiles[4]);
                    
                else:
                    print('files not copied');

            except OSError:  
                print ("Creation of the directory %s failed" % folderPath)
            else:  
                print ("Successfully created the directory %s " % folderPath)
            #assign/update the second value
            secondElement=firstElement
            print("****************")
        #run the bat files in every folder
        runBatfiles(folderPath);
    else:
        print("*********************************")
        print("The path you entered is incorrect!")
        print("*********************************")
        folderPath = input("Please enter the path to save the new folders: ");
        

#run main method
main()