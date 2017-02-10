
#Daily Reminder Program
#-----------------------------------------------------------------------------
#Names- Jarrod McGee & Jose Munoz
#Group- Decimus
#Course-Computer Science 1411 
#Date- 11/22/2015
#---------------------------------
#
#############################################################################
#WARNING                                                                    #
#-------                                                                    #
#YOU HAVE TO RUN THIS PROGRAM THROUGH PYTHON LAUNCHER FOR WINDOWS (CONSOLE) #
#IT WILL NOT WORK THROUGH THE IDLE RUN PROGRAM AS ONE OF THE MODULES        #
#REQUIRES USE OF THE WINDOWS CONSOLE FOR THE MODULE TO WORK CORRECTELY      #
#THANKS!                                                                    #
#############################################################################
#Program Description
#-------------------
#This program basically lets you put in/delete/view events that you have
#and then it will alert you and remind you when this event does come up.
#
#Input-
#------
#The menuchoice and then the event that they want to add or view or delete
#
#Output-
#-------
#The event is deleted or addded or view and will wait to output the alarm
#for that event
#
#Sequence In Code-
#-----------------
#0)Open the intoduction to get user information (will never open again)
#1)Open main menu and title and get user choice on menu
#2)check if any events have passed if so sounds alarm
#3)follow the users choice and open coresponding function
#4)after going through each choice return to updated menu
#5)keep looping from 1-5
#
#Test Cases-
#-----------
#Input- Under menu choose 1 to add event then add an event under the same day
#       that is set for one minute from current time
#Output-Will sound alarm at the main menu exactly at that time
#--
#Input- Under menu choose 3 to view events
#
#Output-prints all added events to the screen 
#--
#
#Modules Added-
#--------------
#datetime- module that allows the print and minipulatation of date and time
#          functions so that we can print the date and time of each event to the user
#winsound- this module as it looks like is Window Sounds module and allows the user of
#          the windows beep function that is what the alarm sound is.
#time- this module is over time it is fairly common and allow the user to print times and etc.
#msvcrt- fairly less common module, it allows the user of the kbhit() function that is inside the
#       module and it works that if the program is waiting for the user input it will run code
#       while waiting which let the program constantly check if events had past.
#
#
#Teamwork Division-
#------------------
#Jarrod McGee- displaymenu(), checkevents(), menuchoice()
#Jose Munoz- introduction(),deleter(),displaytime(), along with GUI implementation
#Other functions coded together or small functions
#
#Program Files-
#--------------
#All the program files will write themselves, if at anytime you want to reset all
#thw whole program just delete the files and it will fully reset.
#
#
#------------------------------------------------------------------------------




#takes a function of datetime which can get current time and time of
#future dates in a tuple
from datetime import datetime
#used to play the beeping alarm sound
import winsound
#just to convert time and get time
import time
#this module is the module that uses msvcrt.kbhit() function
#that function will run other functions while waiting for user input
#for further details look at the display menu function below
import msvcrt

def titleblock():
    #just prints the title with asci art
    print("""
                                                                                                                                                                                                                               
  ____        _ _         ____                _           _             ____                                      
 |  _ \  __ _(_) |_   _  |  _ \ ___ _ __ ___ (_)_ __   __| | ___ _ __  |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  
 | | | |/ _` | | | | | | | |_) / _ \ '_ ` _ \| | '_ \ / _` |/ _ \ '__| | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
 | |_| | (_| | | | |_| | |  _ |  __/ | | | | | | | | | (_| |  __/ |    |  __/| | | (_) | (_| | | | (_| | | | | | |
 |____/ \__,_|_|_|\__, | |_| \_\___|_| |_| |_|_|_| |_|\__,_|\___|_|    |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                  |___/                                                                 |___/                                                                                                                                                                                                                                                             
---------------------------------------------------------------------------------------------------------------------
    """                                                                                                                                                                                                                                        
    )

def introduction():
    #this is the introduction it will only run on the first time a user
    #EVER opens the program, it will then write it to a file and then
    #never ask the user the info again unless the file is deleted
    #this basically just gets there name with some fluff included
    try:
        
        tryfile=open("name.txt","r")
        tryfile.close()
    except FileNotFoundError:
        time.sleep(1)
        print("Thanks for using our program, before we get started lets get some information.")
        time.sleep(1)
        name=input("What is your name?")
        while name=="":
            name=input("Please Insert A Valid Name")
        time.sleep(1)
        namefile=open("name.txt","w")
        namefile.write(name)
        namefile.close
        input("What is your time zone?")
        time.sleep(1)
        print("\nThis program is the Daily Reminder Program, it is designed to reminds you of events throughout your day while you are on your desktop.\nThis will alert you on each event you add\n")

    

def displaytime(name):
    #just makes the little display time window in the main menu
    #the one that says Welcome (name) and heres the time
    now=datetime.now()
    YEAR=now.year
    MONTH=now.month
    DAY=now.day
    time.sleep(2)
    print("-"*25)
    NAME=""
    for line in name:
        NAME+=line
    print("Welcome",NAME+"!")
    time.sleep(.5)
    print("The Date is:",str(MONTH)+"/"+str(DAY)+"/"+str(YEAR))
    counter=0
    time.sleep(.5)
    while counter<1:
            
        now=datetime.now()
        HOUR=now.hour
        MINUTE=now.minute
        if MINUTE in [0,1,2,3,4,5,6,7,8,9]:
            MINUTE=str(MINUTE)
            MINUTE="0"+MINUTE
        SECOND=now.second
        if HOUR>12 and HOUR!=0:
            HOUR-=12
            sideofday="PM"
        elif HOUR==0:
            HOUR+=12
            sideofday="AM"
        else:
            sideofday="AM"
        print("Time:",str(HOUR)+":"+str(MINUTE),sideofday)
        counter+=1
        time.sleep(.5)
        print("-"*25)


def displaymenu():
    #This is the main display menu it is VERY IMPORTANT as almost every
    #function relies on the use and output of this function
    time.sleep(2)
    print("\n----\nMENU\n----")
    print("What would you like to do?")
    formattedmenu="{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}{:<4s}"
    #prints menu of choices
    formatmenu=formattedmenu.format("","1)Add an event\n","","2)Delete an event\n","","3)View current events\n","","4)Update time\n","","5)EXIT\n")
    print(formatmenu)
    time.sleep(1)
    #VERY IMPORTANT:
    ##This print is supposed to make the user think they are inputing something
    ###in reality it is not an input but instead just a buffer state for the
    ####msvcrt.kbhit() to run its course and go through the check events function
    ###basically while the user has not inputed a keyboard stroke it will constantly
    ##run and check if the events time is less than current time and if it is
    #it will prompt the events to alarm (this is inside the checkevents function)
    print("Insert choice to Continue the program and Stop Waiting for Events!")
    while msvcrt.kbhit():
        msvcrt.getch()
        break
    while not msvcrt.kbhit():
        checkevents()
    menuchoice=input("Choice:")
    winsound.Beep(500,700)
    totalchoices=["1","2","3","4","5"]
    #just makes sure they input a real choice
    while menuchoice not in totalchoices:
        time.sleep(.3)
        print("That is not an option, try again")
        time.sleep(.3)
        menuchoice=input("What is your new Choice?(input the number)")
    time.sleep(1)
    #saves that menuchoice to a file so it can still be looked at in other functions
    menu=open("menuchoice.txt","w")
    menu.write(menuchoice)
    menu.close()





        

def menuchoices(choicefile):

    #This basically takes that menuchoice from the last function and decides which path to run down
    ##as if the user decided to go with choice 1 it would run down the choice one path and then in
    ###the end reload the menu
    
    choice=""
    #get that menuchoice
    for choices in choicefile:
        choice+=choices



    ###############
    #ADD EVENT    #
    ###############
    if choice == "1":
        try:
            x=1
            time.sleep(1)
            #just for visuals
            pro="\nProcessing"
            while x<10:
                if x==1:
                    
                    print(pro,end="")
                print(".",end="")
                time.sleep(.1)
                x+=1
            print("\n\n---------\nADD EVENT\n---------")
            #this uses the datetime function and then uses the now part of it to get the current time
            #then it gets the hour of now and minute and day and year and month. This is basically
            #so that it can check if the user inputs a event before this time and date and also
            #so that it can be added to a tuple later
            now=datetime.now()
            HOUR=now.hour
            MINUTE=now.minute
            DAY=now.day
            YEAR=now.year
            MONTH=now.month
            correct=1
            #user inputs events
            while correct==1:
                eventtitle=input("\nWhat is the event?")
                eventtoday=input("Is the event occuring on this day?")
                #if event is not today as for the actual date
                if eventtoday=="n" or eventtoday=="no":
                    eventdate=input("Alright so what day is it? (month/day/year)")
                    #split the date and put into a list so it can be filtered out
                    EVENTDATE=eventdate.split("/")
                    #takes the month day and year out of that list and makes own value
                    eventmonth=EVENTDATE[0]
                    eventday=EVENTDATE[1]
                    eventyear=EVENTDATE[2]
                #now if the event was today then we dont need to input a different date just put in todays
                if eventtoday=="y" or "yes" or "sure" or "yeah":
                    eventyear=YEAR
                    eventmonth=MONTH
                    eventday=DAY
                #asks for hour and minute
                eventtime=input("Sounds good. What time is it occuring? (hour:minute)")
                #splits hour and minute apart so they are in a list and can be strained
                EVENTTIME=eventtime.split(":")
                #ask am or pm as the hours are assumed to be put in military time so changes must
                #be made to fit with this
                eventmid=input("AM or PM?")
                EVENTMID=eventmid
                #gets hour and minute from inputs
                eventhour=int(EVENTTIME[0])
                eventminute=int(EVENTTIME[1])
                #if they put in PM add 12 to meet back up with military time
                if EVENTMID=="PM" or EVENTMID=="pm":
                    eventhour+=12
                #if not then just leave it be unless it is midnight then subtract 12 
                if eventmid=="AM" or eventmid=="am":
                    if eventhour==12:
                        eventhour-=12
                #this is the fancy time that is seen inside choice three with the month str and day and all that    
                currenttime=time.asctime()
                #this create a tuple of the events time characteristics as the time.asctime() takes tuples as an
                #input if it is not now (year,month,day,hour,minute,,,,)
                timetuple=(int(eventyear),int(eventmonth),int(eventday),int(eventhour),int(eventminute),0,0,0,0)
                #inputs the tuple to get fancy time of event
                realeventtime=time.asctime(timetuple)
                #this gets the seconds since january 1st,1970 that the event will be, it is easier to compare to float numbers
                #than it is to compare two strings with integers
                timetimetuple=(time.mktime(timetuple))
                #same but with currenttime
                timetimecurrent=(time.time())
                #if the event has already passed tell them its wrong, else add it
                
                print("Event Added Correctly")
                #this is what we want to print of event time
                eventprinttime=(time.asctime(timetuple))
                counter2=0
                
                eventprinttime=eventprinttime.split(" ")
                eventsPRINTtime=""

                #formats it
                for stuff in eventprinttime:
                    if counter2==0:
                        counter2+=1
                    else:
                        eventsPRINTtime+=stuff+" "
                        counter2+=1
                #writes the events and their timestamps
                #into files for use elsewhere
                exacttimefile=open("timestamps.txt","a")
                exacttimefile.write(str(timetimetuple)+"\n")
                exacttimefile.close()
                formatevent="{:<35s}{}"
                formatedevent=formatevent.format(eventtitle+"-",eventsPRINTtime)
                eventsfile=open("events.txt","a")
                eventsfile.writelines("\n"+formatedevent)
                eventsfile.close()
                correct-=1
                print("\n"*2)
                updatemain()
        #if any problems occur tell them input invalid and go back to menu
        except ValueError:
            print("Input Invalid, redirecting back to main menu!")
            updatemain()
        except IndexError:
            print("Input Invalid, redirecting back to main menu!")
            updatemain()
        



    ################
    #Delete a event#
    ################
    elif choice == "2":
        
        try:
            #user puts in value they want to delete
            deletechoice=input("Please Input the Number the event is!")
            eventsfile=open("events.txt","r")
            timestamps=open("timestamps.txt","r")
            COUNTER=0
            eventsfilelist=[]
            #goes in file and deletes it
            for filelines in eventsfile:
                if COUNTER==int(deletechoice):
                    COUNTER+=1
                                       
                if COUNTER!=int(deletechoice):
                    
                    eventsfilelist.append(filelines)
                    COUNTER+=1
                    
            #print(eventsfilelist)
            eventsfile.close()
            eventsfile=open("events.txt","w")
            eventsfile.writelines(eventsfilelist)
            #print(eventsfilelist)
            eventsfile.close()
            eventsfile=open("events.txt","w")
            newlinecounter=0
            bob=[]
            for liners in eventsfile:
                if liners== "\n" and newlinecounter==0:
                    newlinecounter+=1
                    bob.append(liners)
                if liners=="\n" and newlineccounter!=0:
                    newlinecounter+=1
                else:
                    bob.append(liners)
                    newlinecounter+=1
                    if newlinecounter==10:
                        break
            print("get here?")
            eventsfile.writelines(bob)
            eventsfile.close()
            print("Wer gettomga oigej")
            dele=int(deletechoice)
            print(dele)
            counter10=0
            filerlineslist=[]
            #goes in file and delete it
            for filerlines in timestamps:
                if counter10==dele:
                    counter10+=1
                    continue
                elif counter10 != dele:
                    filerlineslist.append(filerlines)
                    counter10+=1
                    continue
            #print(filerlineslist)
            timestamps.close()
            timestamps=open("timestamps.txt","w")
            timestamps.writelines(filerlineslist)
            timestamps.close()
            print("Event Number:", deletechoice, " was Deleted")
            updatemain()
        except ValueError:
            time.sleep(1.3)
            updatemain()





    #####################
    #View current events#
    #####################
    elif choice == "3":
        #pretty much just opens events text file and prints it in an enumerate format
        try:
            
            eventsfile=open("events.txt","r")
            writtenevents=""
            listevents=[]
            for eachline in eventsfile:
                listevents.append(eachline)
            #print(listevents)
            ticker1=0
            print("\n--------------\nCurrent Events\n--------------\n")
            for value,key in enumerate(listevents):
                if ticker1==0:
                    ticker1+=1
                    continue
                
                if ticker1!=0:
                    print(str(value)+")",key)
                    ticker1+=1
            
            #print(writtenevents)
            eventsfile.close()
            reopenmain=input("\nDo you wish to go back to the menu?")
            if reopenmain=="y" or reopenmain=="yes" or reopenmain=="sure" or reopenmain=="yeah":
                print("\n")
                updatemain()
            else:
                print("\nAlright, program will return to menu in 30 seconds")
                time.sleep(30)
                updatemain()
        except FileNotFoundError:
            time.sleep(1)
            print("No Events Found")
            
            print("Please add events")
            time.sleep(1)
            print("Returning To Main Menu...")
            time.sleep(2)
            updatemain()
        #shows all events




    #################
    #Update menu    #
    #################
    elif choice == "4":
        #just reloads the time in the welcome section that prints above the main menu choices part
        #of the program
        print("\n"*2)
        print("*"*25)
        print("*"*25)
        print("\n"*2)
        print("\nUPDATED TIME\n")
        updatemain()
        #update times

        
    ######
    #QUIT#
    ######
    elif choice == "5":
        quit()
        #quits



def checkevents():
    #this program is what runs in the main menu while it is waiting for a keyboard stroke
    #it will contantly loop through the function looking for if any of the events time have
    #already past and if it does it will sound the alarm and then run the deleter() function
    #which will just go back into the file and then delete the event title and timestamps
    #from all the files so they never have to be dealth with again.
    try:
        
        CURRENTTIME=time.time()
        timestamps=open("timestamps.txt","r")
        stampslist=[]
        #look at all the timestamps and take out the newlines and make them floats, not strings
        for stamps in timestamps:
            stamps=stamps.replace("\n","")
            stamps=float(stamps)
            #put it in this list
            stampslist.append(stamps)
        timestamps.close()
        eventsfile=open("events.txt","r")
        eventslist=[]
        #look at all the events in the eventsfile and put it in a list
        for events in eventsfile:
            eventslist.append(events)
        eventsfile.close()

        
        counter100=1
        eventring=[]

        #look at the list of stamps and if the stamp has passed then take that counter number on how
        #many times it had to loop through and add that as the "event ring" which is basically which
        #line the event was on with a index of zero
        for stampers in stampslist:
            if stampers<float(CURRENTTIME):
                eventring.append(counter100+1)
                counter100+=1
                break
            else:
                counter100+=1
        eventsfile=open("events.txt","r")
        
        counter91=1
        eventsringing=[]

        #look at each event to get one that corresponds to the timestamp
        #puts that eventline in eventsringing
        for linenum in eventsfile:
            if counter91 in eventring:
                eventsringing.append(linenum)
            counter91+=1
        

        #look through each value of eventsringing
        for eventprint in eventsringing:
            #print the event that is going off
            print("This Event has passed:\n",eventprint)
            #another false input that only looks like an input but really is just
            #waiting for a key stroke
            print("Press ENTER to end alarm!")
            #sets the starting frequency of beep
            beeper=150
            counter21=1
            #while keyboard is hit into the getch break from the loop
            while msvcrt.kbhit():
                msvcrt.getch()
                break
            #while the keyboard is waiting for input and is not having a keyboad inputed
            #play the alarm for 1000 time and keep looping through the alarm while increasing
            #and decreasing the frequency but keeping it under 300 frequency
            while not msvcrt.kbhit():
                winsound.Beep(beeper,1000)
                if beeper>300:    
                    beeper-=120
                else:
                    beeper+=110
                time.sleep(.5)
        #if their is in fact anything that event has proct then open the deleter and input the choices
           #into the deleter function and delete those from the text files.
        if len(eventsringing)>=1:
            for thering in eventring:
                deleter(thering)
    
                
                
    #if they cant find the files as in the user has never put in events then just
            #pass the function
    except FileNotFoundError:
        pass

def updatemain():
    #this is the same a displaymenu for the most part but is more modular and can
    #be reimplemented over and over without any error as the normal menu would cause
        introduction()
        realnames=open("name.txt","r")
        displaytime(realnames)
        realnames.close()
        displaymenu()
        menuchoicefile=open("menuchoice.txt","r")
        menuchoices(menuchoicefile)
        menuchoicefile.close()

def deleter(deletechoice):
        #same things as the delete function under menuchoice() function in choice 2, the only difference is
        #that instead of user input it is done automatically without any user interaction and the deletechoice
        #is the line that the timestamp is on -1 and then the program can interpret this and delete it from
        #each file
        eventsfile=open("events.txt","r")
        timestamps=open("timestamps.txt","r")
        COUNTER=1
        eventsfilelist=[]
        for filelines in eventsfile:
            if COUNTER==int(deletechoice):
                COUNTER+=1
                continue
            else:
                eventsfilelist.append(filelines)
                COUNTER+=1
        eventsfile.close()
        eventsfile=open("events.txt","w")
        eventsfile.writelines(eventsfilelist)
        eventsfile.close()
        counter10=1
        filerchoice=int(deletechoice)-1
        filerlineslist=[]
        for filerlines in timestamps:
            if counter10==int(filerchoice):
                counter10+=1
            else:
                filerlineslist.append(filerlines)
                counter10+=1
        timestamps.close()
        timestamps=open("timestamps.txt","w")
        timestamps.writelines(filerlineslist)
        timestamps.close()
            
        updatemain()
        
def main():
    #just run everything that needs running at the start
    titleblock()
    introduction()
    realnames=open("name.txt","r")
    displaytime(realnames)
    realnames.close()
    displaymenu()
    menuchoicefile=open("menuchoice.txt","r")
    menuchoices(menuchoicefile)
    menuchoicefile.close()
#run main
main()

