try:
    f = open('Open.txt','r')
    f.write("Write Simple Text")

except IOError:
    print('ERROR : Could not find file or read data')

finally:
    print('THIS IS SAVER')
