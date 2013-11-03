###############
# CSV to ARFF #
###############
import csv
from time import sleep

class convert(object):

    content = []
    name = ''

    def __init__(self):
        self.csvInput()
        self.arffOutput()
        print '\nFinished.'

    #import CSV
    def csvInput(self):

        user = raw_input('Enter the CSV file name: ')

        #remove .csv
        if user.endswith('.csv') == True:
            self.name = user.replace('.csv', '')
            
        print 'Opening CSV file.'     
        try:
            with open(user, 'rb') as csvfile:
               lines = csv.reader(csvfile, delimiter = ',')
               for row in lines:
                   self.content.append(row)
            csvfile.close()
            sleep(2) #sleeps added for dramatic effect!
            
        #just in case user tries to open a file that doesn't exist
        except IOError:
            sleep(2)
            print 'File not found.\n'
            self.csvInput()
            
    #export ARFF
    def arffOutput(self):
        print 'Converting to ARFF file.\n'
        title = str(self.name) + '.arff'
        new_file = open(title, 'w')

        ##
        #following portions formats and writes to the new ARFF file
        ##

        #write relation
        new_file.write('@relation ' + str(self.name)+ '\n\n')

        #get attribute type input
        for i in range(len(self.content[0])-1):
            attribute_type = raw_input('Is the type of ' + str(self.content[0][i]) + ' numeric or nominal? ')
            new_file.write('@attribute ' + str(self.content[0][i]) + ' ' + str(attribute_type) + '\n')

        #create list for class attribute
        last = len(self.content[0])
        class_items = []
        for i in range(len(self.content)):
            name = self.content[i][last-1]
            if name not in class_items:
                class_items.append(self.content[i][last-1])
            else:
                pass  
        del class_items[0]
    
        string = '{' + ','.join(sorted(class_items)) + '}'
        new_file.write('@attribute ' + str(self.content[0][last-1]) + ' ' + str(string) + '\n')

        #write data
        new_file.write('\n@data\n')

        del self.content[0]
        for row in self.content:
            new_file.write(','.join(row) + '\n')

        #close file
        new_file.close()
        sleep(2)

    
#####    
run = convert()
