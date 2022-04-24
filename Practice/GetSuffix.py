def getSuffix(filename):
    pointPos = filename.find('.')
    if pointPos != -1:
        return filename[pointPos:]
    else:
        return 'No suffix'
if __name__ == '__main__':
    fileName = input('Enter a file with suffix')
    print(getSuffix(fileName))
