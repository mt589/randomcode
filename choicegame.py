def startstory():
    gender= input ("Pick your player: Boy or Girl")
    if gender == "Girl" or gender == "girl":
        scenario = input ("Pick a scenerio: school or social")
        if scenario == "school" or scenario== "School":
            choice1 = input ("You, the girl, started the conversation with the boy sitting behind her. The teacher yells at the boy. Would you take the blame or allow the teacher to yell at the boy? Answer yes or no")
            if choice1 == "yes" or choice1 == "Yes":
                print ("That is the ethical thing to do. Teachers tend to overlook girls misbehavior, and compliment their good behavior.")
            if choice1 == "no" or choice1 == "No" :
                print ("These types of choices of not taking the blame for actions is one of the reasons for the different treatment between boys and girls. Make sure to take responisbility for your actions in order to gain respect from peers because it is harder for girls to gain respect.")
            print ("Research shows that teachers treat boys and girls differently. Teachers compliment girls good behavior and boys correct knowledge more than girls correct knowledge and boys good behavior. This might teach children that they should have different opportunities because of their gender.")
            choice7= input ("Do you want to play again? answer yes or no?")
            if choice7 == "yes" or choice7 == "Yes":
                startstory()
        if scenario == "social" or scenario == "Social":
            choice3 = input ("You ended up breaking up with your boyfriend and then dating another guys 3 weeks later. People started rumors about you behind your back and you did not hear about them yet. Would you stay quiet about the whole situation? Answer yes or no")
            if choice3 == "yes" or choice3 == "Yes":
                print ("This is probably the best choice. Do not bring more attention to the sitation")
            if choice3 == "no" or choice3 == "No":
                print ("Rethink this decision and make sure you are ready for rummors to start because that is just the nature of the world even though it is not nice")
            choice4 = input ("You started to hear the rumors that people said about you and the boy started most of them. They called you slut and two timer, in addition to other mean names. However, the boy did the exact same thing, he started dating someone a little over 3 weeks after the breakup and nobody started runmors about him. Do you start a rumor about him? Answer yes or no")
            if choice4 == "yes" or choice4 == "Yes" :
                print ("Do not start a rumor it is not worth being mean. Just ignore the rumors about yourself and it will all blowover soon. Be the bigger person")
            if choice4 == "no" or choice4 == "No":
                print ("Alright!!! you picked the better decision. Hopefully all the rumors will subside and it was very brave of you to do what would make you happy even though there would be backlash.")
            print ("A lot of times girls get criticized for their relationship choices, while boys are congratualted for dating multiple women. This stigma needs to stop")
            choice7= input ("Do you want to play again? answer yes or no?")
            if choice7 == "yes" or choice7 == "Yes":
                startstory()

    if gender == "Boy" or gender == "boy" :
        scenario = input ("Pick a scenerio: school or social")
        if scenario == "school" or scenario == "School":
            choice2 = input ("You, the boy, gave the wrong answer in class after a girl also gave the wrong answer. The teacher criticized the girl for getting the answer wrong, but after you got it wrong she said nice try. After class you saw the girl crying. Would you mention something to the teacher that it made the girl feel bad and maybe the teacher should give more equal feedback to boys and girls? Answer yes or no")
            if choice2 == "yes" or choice2 == "Yes":
                print ("Teachers tend to overlook guys wrong answer in order to keep them invested in class. It is good that you would do that because it is hard to be criticized on wrong information instead of someone just try and help you understand.")
            if choice2 == "no" or choice2 == "No":
                print ("This is an understandable response because it can be hard to face the teacher. Maybe go over to the girl and explain the information to her. In class, try to even out the feedback and say good try")
            print ("Research shows that teachers treat boys and girls differently. Teachers compliment girls good behavior and boys correct knowledge more than girls correct knowledge and boys good behavior. This might teach children that they should have different opportunities because of their gender.")
            choice7= input ("Do you want to play again? answer yes or no?")
            if choice7 == "yes" or choice7 == "Yes":
                startstory()
        if scenario == "social" or scenario == "Social":
            choice5 = input ("Your friend's girlfriend ended up breaking up with him. He started dating another girl 3 weeks later. Do you congratulate him? Answer yes or no")
            if choice5 == "yes" or choice5 == "Yes":
                print ("Of course you would congratulate him he is a solid player")
            if choice5 == "no" or choice5 == "No":
                print ("It's not that you would not congratulate him it's that you just hope he's happy.")
            choice6 = input ("You know that he started rumors about the girl he was with. Do you tell him to stop the rumors?")
            if choice6 == "yes" or choice6 == "Yes":
                print ("That is very brave and a good ethical decision.")
            if choice6 == "no" or choice6 == "No" :
                print ("Although it will be very difficult maybe rethink this decision and stop the rumors")
            print ("Boys are normally praised for dating multiple women in a short period of time. However girls are looked down upon in these situations. This needs to stop")
            choice7= input ("Do you want to play again? answer yes or no?")
            if choice7 == "yes" or choice7 == "Yes":
                startstory()

startstory()
