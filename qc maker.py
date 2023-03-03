fileName = input("Enter name of show/feature: ")
print(fileName)
seasonNum = input("Enter number of seasons: ")
print(seasonNum)
epNum = input("Enter number of episodes: ")
print(epNum)

season = 0
ep = 1
line = ''

def lines(fileName, line):
    for x in range((len(fileName)+5)):
        line = line + '-'
    return line


with open('C:\\Users\\wyatt\\OneDrive\\Documents\\QC Work\\'+fileName+'.txt', 'w') as f:
   f.write(fileName + '\n' + lines(fileName,line))
   for x in range(int(seasonNum)):
    season = season + 1
    ep = 1
    for x in range(int(epNum)):
        f.write('\n')
        f.write('\n')
        if (ep >= 10):
           f.write(str(season) + str(ep))
        if (ep < 10):   
            f.write(str(season) + '0' + str(ep))
        ep = ep + 1
        f.write('\n')
        f.write('\n')
        f.write('\n') 
        f.write('\n')  
        f.write(lines(fileName,line))                      
        