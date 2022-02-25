import sys
import os
import pyttsx3
import datetime
import pandas,tkinter.messagebox
try:
    import pywhatkit,wikipedia
except:
    print('No Internet connected to work with some of the features in Funnyx, but works some features')
print('Welcome to Funnyx Command Client')
while True:
    cmd=input("fcc >")
    if 'EXIT' in cmd:
        print('\nThank you for using us\nBy Funnyx')
        break
    elif 'WIKI' in cmd:
        x=cmd.replace('WIKI','')
        wiki=wikipedia.summary(x)
        print('\n\tYou Wikied : %s \n'%(x),'\n',wiki,'\n')
    elif 'SAY' in cmd:
        x=cmd.replace('SAY','')
        speaker=pyttsx3.init()
        print('Command you entered : %s'%(x))
        speaker.say(x)
        speaker.runAndWait()
    elif 'TIME' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
    elif 'DATE' in cmd:
        x=datetime.datetime.now().date()
        print(x)
    elif 'OPEN' in cmd:
        x=cmd.replace('OPEN','')
        print('\tOpening %s'%(x))
        try:
            os.system(x)
        except:
            print('The file %s not found'%(x))
    elif 'PLAY' in cmd:
        x=cmd.replace('PLAY','')
        pywhatkit.playonyt(x)
    elif 'SEARCH' in cmd:
        x=cmd.replace('SEARCH','')
        pywhatkit.search(x)
    elif 'ABOUT' in cmd:
        print('Funnyx Command Client\nBy Padmanabh PV')
    elif 'HELP' in cmd:
        index=['DATE','OPEN <command>','PLAY <command>',
               'HELP','SAY <command>','TIME','ABOUT','WIKI <command>','SEARCH <command>','EXIT']
        data=['Shows the current date','Opens the current file','Plays musics/videos from Youtube(requires internet conn.)',
              'Help client for Funnyx','Says the input command you entered','Shows the current time',
              'Sows About Funnyx','Collect data from wikipedia (requires internet conn.)','Opens your browser and shows the search(requires internet conn.)',
              'Exits from Funnyx']
        print('Some of the features require internet connection\n\n')
        print(pandas.Series(data,index))
    else:
        print('The command does not match any criteria,type "HELP" for more info')
