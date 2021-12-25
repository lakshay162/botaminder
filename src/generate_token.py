from __future__ import print_function
import time
import os

print('==============================')
print('+ BOTAMINDER TOKEN GENERATOR +')
print('==============================')
print('''This script can be used to generate the token used to update the arduino with latest time and events\
in a quick fashion.\n''')

print("modes available:\n1. manual\n2. eventsonly\n3. healthonly\n4. silent\n")

mode, mode1 = "",""

def ask_for_mode():
    global mode, mode1
    mode=input('enter user mode:').lower()
    mode1 = mode


def manual():
    s_name=[]
    s_st=[]
    s_et=[]
    global mode
    
    def writeprofile():
        lt=(time.localtime(time.time())[3:6])
        profname=input('enter the profile name:')
        profiles=os.listdir(os.path.join(os.getcwd(),'profiles'))
        profiles.pop(profiles.index('.gitkeep'))
        def writing():
            no=int(input('enter the number of events: '))
            print('\n\n')
            for i in range(no):
                q='enter the title of event '+str(i+1)+':'
                name=input(q)
                st=(input('enter start time seperated by ":" :').split(':'))
                et=(input('enter end time seperated by ":" :').split(':'))
                print('\n\n')
                s_name.append(name)
                s_st.append(st)
                s_et.append(et)
            n='"'+s_name[0]+'"'
            st1='(long)'+str(int(s_st[0][0]))+'*3600+(long)'+str(int(s_st[0][1]))+'*60'
            et1='(long)'+str(int(s_et[0][0]))+'*3600+(long)'+str(int(s_et[0][1]))+'*60'
            for i in s_name[1:]:
                n+=','+'"'+i+'"'
            for i in s_st[1:]:
                st1+=','+'(long)'+str(int(i[0]))+'*3600+(long)'+str(int(i[1]))+'*60'
            for i in s_et[1:]:
                et1+=','+'(long)'+str(int(i[0]))+'*3600+(long)'+str(int(i[1]))+'*60'    
            file = open(os.path.join(os.getcwd(),'profiles',profname+".txt"), 'w')
            file.write('COPY THIS TOKEN TO ARDUINO SKETCH')
            file.write('\n\n\n')
            file.write('long time[3] = {'+str(int(lt[0]))+','+str(int(lt[1]))+','+str(int(lt[2]))+'};\n')
            file.write('int events = '+str(no)+';\n')
            file.write('String eventName['+str(no)+'] = {'+n+'};\n')
            file.write('long eventStartTime['+str(no)+'] = {'+st1+'};\n')
            file.write('long eventEndTime['+str(no)+'] = {'+et1+'};\n')
            file.write('int eventScrollingSpeed = 4;'+'\n'+\
                       'long waterReminder = (long)3*3600;'+'\n'+\
                       'long breakReminder = (long)4*3600;'+'\n'+\
                       'long eveningBreak = (long)17*3600;\n')
            
            file = open(os.path.join(os.getcwd(),'profiles',profname+'.txt'), 'r')
            print(file.read())
            print('String userMode = "'+mode+'";')
            print('\n\n')
            file.close()
        if not profiles:
            writing()
        else:
            if profname+'.txt' not in profiles:
                print(profname)
                writing()
            else:
                print('profile already exists enter a new name')
                writeprofile()
    
    def chooseprofile():
        profiles= os.listdir(str(os.path.join(os.getcwd(),'profiles')))
        profiles.pop(profiles.index('.gitkeep'))
        count=1
        print('select the profile from the list below:\n')
        for i in profiles:
            print(str(count)+'. '+i)
            count+=1
        profname=int(input('enter the number of the profile:'))
        if profname-1 < len(profiles):
            file=open(os.path.join(os.getcwd(),'profiles',profiles[profname-1]))
            print(file.read())
            print('String userMode = "'+mode+'";')
            file.close()
            print('\n\n')
        else:
            print('\n\nyou entered wrong input, please try again.\n---------------------------------\n')
            chooseprofile()
        
            
    print('Please select an option from the list : ','\n','1 --> choose a profile','\n','2 --> create a new profile','\n',\
          '3 --> input manually')

    profileoption= input('select the option:') 
    if profileoption=='1' or profileoption=='choose a profile':
        profiles=os.listdir(str(os.join.path(os.getcwd(),'profiles')))
        profiles.pop(profiles.index('.gitkeep'))
        if not profiles:
            print('\n\nno profiles found try again\n\n')
            manual()
        chooseprofile()   
    elif profileoption=='2' or profileoption=='create a new profile':
        writeprofile()
    elif profileoption=='3' or profileoption=='input manually':
        no=int(input('enter the number of events'))
        print('\n\n')
        for i in range(no):
            q='enter the title of event '+str(i+1)+':'
            name=input(q)
            st=(input('enter start time seperated by ":" :'))
            et=(input('enter end time seperated by ":" :'))
            print('\n\n')
            s_name.append(name)
            s_st.append(st.split(':'))
            s_et.append(et.split(':'))
        n='"'+s_name[0]+'"'
        st1='(long)'+str(int(s_st[0][0]))+'*3600+(long)'+str(int(s_st[0][1]))+'*60'
        et1='(long)'+str(int(s_et[0][0]))+'*3600+(long)'+str(int(s_et[0][1]))+'*60'
        for i in s_name[1:]:
            n+=','+'"'+i+'"'
        for i in s_st[1:]:
            st1+=','+'(long)'+str(int(i[0]))+'*3600+(long)'+str(int(i[1]))+'*60'
        for i in s_et[1:]:
            et1+=','+'(long)'+str(int(i[0]))+'*3600+(long)'+str(int(i[1]))+'*60'
            
        lt=(time.localtime(time.time())[3:6])
        print("COPY THIS TOKEN TO ARDUINO SKETCH")
        print('\n\n\n') 
        print('long time[3] = {'+str(int(lt[0]))+','+str(int(lt[1]))+','+str(int(lt[2]))+'};')
        print('int events = ',no,';')
        print('String eventName[',no,'] = {',n,'};')
        print('long eventStartTime[',no,'] = {',st1,'};')
        print('long eventEndTime[',no,'] = {',et1,'};')
        print('int eventScrollingSpeed = 4;'+'\n'+\
            'long waterReminder = (long)3*3600;'+'\n'+\
            'long breakReminder = (long)4*3600;'+'\n'+\
            'long eveningBreak = (long)17*3600;')
        print('String userMode = "'+mode+'";')
        print('\n\n')
    else:
        manual()



ask_for_mode()

if mode == "manual" or mode == "1":
    mode = "manual"
    manual()

elif mode == "healthonly" or mode == "3":
    mode = "health"
    print("HEALTH MODE SELECTED")
    print("======================")
    print("Only Health events will ring a alarm.")
    mode1 = input("Select one of the methods to fetch events:\n1. manual\n\nSelect One: ").strip()
    if mode1 == "manual" or mode1 == "1":
        manual()
    
    else:
        print("Wrong Input.. TRY AGAIN")

elif mode == "eventsonly" or mode == "2":
    mode='events'
    print("Events ONLY MODE SELECTED")
    print("======================")
    print("Only Calendar events will ring a alarm.")
    mode1 = input("Select one of the methods to fetch events:\n1. manual\n\nSelect One: ").strip()
    if mode1 == "manual" or mode1 =="1" :
        manual()
   
    else:
        print("Wrong Input.. TRY AGAIN")

elif mode == "silent" or mode == "4":
    mode='silent'
    print("SILENT MODE SELECTED")
    print("====================")
    mode1 = input("NO EVENTS WILL RING AN ALARM.\nIf you want your events to be available in the arduino to display, \
    Select one of the methods to fetch events:\n1. manual\n\nSelect One or leave blank to use the project as a desk clock: ").strip()
    if mode1 == "":
        print('\n\n\n\n')
        lt=(time.localtime(time.time())[3:6])
        print('COPY THIS CODE TO ARDUINO.\n\n\n')
        print('long time[3] = {'+str(int(lt[0]))+','+str(int(lt[1]))+','+str(int(lt[2]))+'};')
        print('int events = 1;')
        print('String eventName[1] = {"No Events"};')
        print('long eventStartTime[1] = {(long)86399};')
        print('long eventEndTime[1] = {(long)86399};')
        print('int eventScrollingSpeed = 4;'+'\n'+\
              'long waterReminder = (long)86399;'+'\n'+\
              'long breakReminder = (long)86399;'+'\n'+\
              'long eveningBreak = (long)86399;')
        print('String userMode = "'+'silent'+'";')
        print('\n\n')
    elif mode1 == "manual" or  mode1=="1":
        manual()
    
    else:
        print("Wrong Input. TRY AGAIN")
        
else:
    print("WRONG INPUT! SELECT ONE OF THE ABOVE!!!\ntry again")
    
        
    
    

