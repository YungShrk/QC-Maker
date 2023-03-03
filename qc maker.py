showOrMov = input("Show or list of features? ('s' for show, 'f' for features): ")
if showOrMov == 's':
    fileName = input("Enter name of show: ")
    seasonNum = input("Enter number of seasons: ")
    epNum = input("Enter number of episodes: ")    
if showOrMov == 'f':
    fileName = input("Enter name of production company (i.e, 'AMC'): ")    
    epNum = input("Enter number of features: ")
    
    

season = 0
ep = 1
line = ''
s = 's'
f = 'f'
def lines(fileName, line):
    for x in range((len(fileName)+5)):
        line = line + '-'
    return line


if showOrMov == s: #replace this line in orange vvvvvvv
    with open('C:\\Users\\wyatt\\OneDrive\\Documents\\QC Work\\'+fileName+'.txt', 'w') as f:
        f.write(fileName + '\n' + lines(fileName,line))
        for x in range(int(seasonNum)):
            season = season + 1
            ep = 1
            for x in range(int(epNum)):
                f.write('\n\n')
                if (ep >= 10):
                    f.write(str(season) + str(ep))
                if (ep < 10):   
                    f.write(str(season) + '0' + str(ep))
                ep = ep + 1
                f.write('\n\n\n\n')
                f.write(lines(fileName,line))                      
if showOrMov == f: #replace this line in orange vvvvvvv
    with open('C:\\Users\\wyatt\\OneDrive\\Documents\\QC Work\\'+fileName+' Features.txt', 'w') as f:    
        f.write(fileName + ' Features' + '\n' + lines(fileName,line))
        print('Now, one by one, input the names of the features.')
        for x in range(int(epNum)):
            featureName = input("Enter name of feature: ")
            f.write('\n\n')
            f.write(str(featureName))
            f.write('\n\n\n\n')
            f.write(lines(fileName,line))