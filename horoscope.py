#JASMINE IRANI
#Code for Checking Horoscope
#filename: horoscope.py
#checking type of s
#s = int(input("Pick your sign number and press Enter\n"))
#print(s)
#print(type(s))

next=True
#while loop
while next==True: #boolean var next
    print('''
    1)Aries
    2)Leo
    3)Cancer
    4)Pisces
    5)Scorpio
    6)Taurus
    7)Sagittarius
    8)Gemini
    9)Virgo
    10)Libra
    11)Capricorn
    12)Aquarius
    ''')

    #s is typecasted from string to int
    s = int(input("Pick your sign number and press Enter\n"))
    
    #conditional statement 
    if s==1:
        print("\nAries-Limited capital will not prove an obstacle in putting a project on the road. Support of family members is assured in whatever you undertake.There is every likelihood of bagging a prized job for those associated with the management field. Connoisseurs of good food can come across some more gastronomic delights! You are likely to get within reach of whatever you are trying to achieve on the academic front. Prepare thoroughly for a long journey to avoid hassles. Some of you may plan to buy a house or a car soon.")

    elif s==2:
        print("\nLeo-A family member studying out of town or abroad may become a source of worry. Impressing the interviewer will be important for the job seekers. It will be prudent to shift into the saving mode on the financial front. Achieving the impossible is in store for some on the academic front. Value of property owned by you is likely to escalate. Taking some time off for a break will act as a soothing balm to the mind.")

    elif s==3:
        print("\nCancer-You will benefit by taking a break from your regular exercise routine. Child or sibling may make you proud by his or her achievements. It will be prudent to keep a watchful eye on a business colleague. Your financial prudence will help keep the coffers brimming. Outstanding performance can be expected by some on the academic front. You may get the chance to turn an official trip into a family vacation. Acquiring a new property is on the cards.")

    elif s==4:
        print("\nPisces-Watch your step on the financial front, as someone may sweet-talk you out of money. Putting off work for some other day will just not work on the professional front. Those ailing for long can expect a miraculous recovery. Your wish is likely to get fulfilled on the academic front, provided you take timely action. Expect some good loving care from spouse today! A comfortable journey to a distant place is in the offing for some. Visiting the site of your new home is possible.")

    elif s==5:
        print("\nScorpio-Getting your money back from someone may require efforts, but get back, you will! Less work will enable you to take some time off for yourself. Health conscious will discover some new route to fitness. Additional domestic chores if not planned properly may leave you fatigued. Overconfidence on the academic front needs curbing, as things may not turn out the way you want them to. Young couples may enroll for an adventure trip and enjoy the thrills.")
        
    elif s==6:
        print("\nTaurus-A new source of income is likely to open up and promises to make you financially secure. Fitness mantra of a friend will do wonders for your health. Happy time is foreseen at work as you tackle your job efficiently. Parents or a family member is likely to breathe down your neck and may monitor your actions closely. You will fare well on the academic front and manage to remain amongst the frontrunners. You will need to fine tune you’re travelling time with others to reach a venue together. Deal in property only with well-established dealers.")

    elif s==7:
        print("\nSagittarius-A property issue is likely to be resolved amicably. Performing well on the academic front will not pose much difficulty for you. Less work will enable you to take some time off for yourself. Don’t let anyone bulldoze you into spending money on something that you don’t exactly need. Condition of someone close can show rapid improvement. Steer clear of spouse’s firing line, as he or she may suffer from mood swings. A good opportunity to spend some time in a tourist destination is likely to come your way.")

    elif s==8:
        print("\nGemini-You will need to remain guarded, as you may be taken for a ride on the monetary front. Things that were going wrong on the work front will begin to improve. Those doing their bit to shed weight will succeed beyond their expectations! Homemakers will find time to achieve much on the domestic front. Academic aspirations of those pursuing higher studies are likely to be met. Those forced to travel frequently may do right to make the journey comfortable. You may go in for purchase of a property.")

    elif s==9:
        print("\nVirgo-An exciting time in a family gathering is foreseen. Avoid offending someone by your actions at work. Money well spent may give you inner satisfaction. Someone may extend a helping hand in making you learn new fitness techniques. You may take a step nearer to acquiring property. You are likely to hold your own in a competitive situation on the academic front. Arrange for someone to look after your assets, if you are planning to move out for a longer duration.")

    elif s==10:
        print("\nLibra-Your sympathetic touch will alleviate the problems of a family elder. Consistent performance will pave the way for promotion. Try not to overstep the budget, as it may become difficult to meet unforeseen monetary requirements. Chances of leaving an exercise regime midway cannot be ruled out for some. Those pursuing higher studies have a bright chance of getting recruited on the campus. Preparation for an overseas business trip is likely to start now. Getting a lucrative offer on property is possible.")

    elif s==11:
        print("\nCapricorn-An exciting time in a family gathering is foreseen. Avoid offending someone by your actions at work. Money well spent may give you inner satisfaction. Someone may extend a helping hand in making you learn new fitness techniques. You may take a step nearer to acquiring property. You are likely to hold your own in a competitive situation on the academic front. Arrange for someone to look after your assets, if you are planning to move out for a longer duration.")

    elif s==12:
        print("\nAquarius-Unnecessarily worrying about your health will serve no purpose. A difference of opinion with the elders may make you ponder about something in mind. Day appears to be especially favourable for those associated with banking or engineering. Raising capital for a commercial venture will not pose much difficulty. Chances of getting hoodwinked in a property deal look real. You may become indispensable for someone’s success on the academic front. Speed and comfort is foreseen for those undertaking a long journey.")

    else:
        print("\nWrong Option")
        
    #updating next variable
    next=True if input("\nWould you like to continue(Y/N)")=='Y' else False

    #one new feature-exit message for user
    if next==False:
        print("\nThank you for using our application, have a nice day")
