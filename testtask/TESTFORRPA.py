from pathlib import Path
paths = sorted(Path('.').glob('**/*.*'))

paths1 = []

for i in paths:

    paths1.append(str(i))

fullpath = []

for i in paths1:

    d = i.split('\\')
    fullpath.append(d)


NumberOfLines = list(range(0,len(paths)))

FolderName = []
FullFileName = []    


for element in fullpath:

    if len(element) == 1:

        FolderName.append('testtask')
        FullFileName.append(element[0])

    else:

        FolderName.append(element[len(element) - 2]) 
        FullFileName.append(element[len(element) - 1])   
 


extentionNameReversed = ''
extentionNameFinal = []
FileNameFinal = []

for FileName in FullFileName:

    reversedName = reversed(FileName)
    extentionNameReversed = ''
    
    for ReversedElement in reversedName:

        extentionNameReversed += ReversedElement
        
        
        if ReversedElement == '.':

            extentionNameFinal.append(extentionNameReversed[::-1])
            if (len(FileName) - len(FileName)) == 0:
                FileNameFinal.append(FileName)
            else:
                FileNameFinal.append(FileName[:len(FileName) - len(extentionNameReversed)]) 

            break


fullpath = {'Номер строки':NumberOfLines, 'Папка':FolderName,'Название':FileNameFinal, 'Расширение':extentionNameFinal}

import pandas as pd
df = pd.DataFrame(fullpath)
df.to_excel('result.xlsx')
