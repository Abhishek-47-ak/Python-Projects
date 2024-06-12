#random story rpg
#hp mechanics

import random
# mc="Yato"
# enemy="Shadow Dragon"
# buffs=['Spine of Stellar Dragon','Fleur Cannon','Orchards Bounty','Will of the cavalry',"Harmonic symphony"]
# enemymoveset=["Grudge","Astral barrage","Scion of the war torn land","NightGlare"]

def Story():
    print("The warrior of liberation 'YATO' was returning home after the successful conquest of the realm of Shadows")
    print("He arrived at a crossroads and wondered which path he should take\n")
    ch1=random.randint(1,3)
    if ch1==1:
        print('"The left path seems to be abandoned,Lets try this", he thought as his hunger from adventure never died out')
        print("As the hero took forth through the path, he soon found himself in a spooky forest.\nThis reminded him of the bitter struggles in the realm of shadows.")
        print("But as he was sneaking by he fell down into an underground cave,\n which even with his superhuman vision, went undetected")
        return ch1
    else:
        print("\n'The path to the right seems to be used often', he mumbled to himself. Weary from his travels he wished to rest in a village\n and so he chose the road to his right.")
        print("\nJust as he had predicted the hero stumbled into a quiet village.\n Most of the residents where indoors and only a few shops had any traces of human presence")
        print("\nThe hero went to the town square where a village elder stood gazing at the sky.\n Before him was a stellar artifact that didnt match his surroundings.")
        return ch1
    

def Buffs(c):
    if c==1:
        print("Surprisingly the cave was a hidden alter upon which a sacred treasure shone and a text engraved")
        buffs=['Spine of Stellar Dragon','Fleur Cannon']
        ch2=random.choice(buffs)
        print(f"[[The hero obtained the {ch2}]]")
        print(f"The engraving read...'Beneath this alter lies a ruin where the Shadow dragon lies, waiting to be resurected.\n Oh hero who came upon this {ch2} by chance, slay the evil dragon and bring about peace once more to this forest'")
        return ch2
    else:
        print("The elder with a single look found the gleam back in his eyes.'Its you,the profecised hero.\n Youhave came to slay the evil dragon'")
        print("The elder explained the plight brought about by the evil Shadow Dragon and the profecy where a hero fit to wield the weapon of the gods would slay him.\n Yato tries to lift the artifact and lo he has been chosen")
        buffs=['Orchards Bounty','Harmonic symphony']
        ch2=random.choice(buffs)
        print(f"[[The hero obtained the {ch2}]]")
        print(f"The elder send the hero to the vile dragons alter across the forest and the {ch2} in hand he stepsinto the forest of the evil dragon.")
        return ch2

def Battle(c2):
    print('\n\n---------------------COMBAT BEGIN-----------------------------')
    ehp=100
    php=100
    turn=0
    i=True
    #MOVESET MECHANICS
    ssdr=0          ##
    hs=0            ##
    grudge=0        ##
    woct=0          ##
    ng=0            ##
    ##################
    print(f"YATO the hero has branded the artifact {c2}")
    while i==1:
        turn+=1
        print("Turn ",turn)
        mit=0   #mitigator
        mult=0  #multiplier
        dmg=random.randint(1,26)
        if turn%2==0:
            #yato's turn
            print(f"Yato deals {dmg} dmg")
            if c2=="Orchards Bounty":
                heal=random.randint(5,11)
                php=php+heal
                mult=11-heal
                print(f"yato heals +{heal}")
                dmg=dmg+(int(mult/100)*dmg)
            elif c2=="Harmonic symphony":
                dmg=dmg+hs
                hs=0
            elif c2=="Spine of Stellar Dragon":
                rand=random.randint(0,2)
                if rand==1:
                    dmg=dmg+(int(dmg/2))
                else:
                    ssdr=35  #%
            elif c2=="Fleur Cannon":
                rand=random.randint(15,26)
                dmg=dmg+(int(rand/100)*dmg)
                php=php+5
                print("Yato heals +5")
            #Will of cavalry trigger
            woc=random.randint(1,11)
            if woc==3 or woc==7:
                rand=random.randint(1,4)
                if rand==1:
                    print("Yato heals +10")
                    php=php+10
                elif rand==2:
                    dmg=dmg+(int(5/100)*dmg)
                else:
                    woct=10 #%
            #mitigations
            dmg=dmg-(int(grudge/100)*dmg)
            dmg=dmg-(int(ng/100)*dmg)
            #final dmg:-
            ehp=ehp-dmg
            print(f"shadow dragon suffers {dmg} damage; {ehp}HP left\n")
        else:
            #shadow's turn
            print(f"Shadow dragon charges {dmg} instances of dmg")
            drch=random.randint(1,5)
            if drch==1: #grudge
                print("Shadow dragon unleashes- GRUDGE")
                grudge=random.randint(10,31)
                dmg=dmg+(30-grudge)
            elif drch==2: #Astral barrage
                print("Shadow dragon unleashes- ASTRAL BARRAGE")
                dmg=dmg+(int(20/100)*dmg)
                ehp=ehp+5
                print("Shadow dragon heals +5")
            elif drch==3: #Scion of the war torn land
                print("Shadow dragon unleashes- SCION OF THE WAR TORN LAND")
                dmg=dmg*2
            else: #nightglare
                print("Shadow dragon unleashes- NIGHTGLARE")
                ng=random.randint(50,71) #%
                ehp=ehp+(ng//10)
                print(f"Shadow dragon heals {ng//10}")
                #ivide continue
            if c2=="Spine of Stellar Dragon":
                dmg=dmg-(int(ssdr/100)*dmg)
                ssdr=0
            elif c2=="Harmonic symphony":
                mit=random.randint(50,71)
                dmg=dmg-(int(mit/100)*dmg)
                hs=int((100-mit)/3)
            dmg=dmg-(int(woct/100)*dmg)
            woct=0
            #final damage
            php-=dmg
            print(f"Yato suffers {dmg} damage; {php}HP left\n")


        if php<0:
            i=0
            win=2
            return win
        elif ehp<0:
            i=0
            win=1
            return win

        
run=Story()
buff=Buffs(run)
win=Battle(buff)   
if win==1:
    print("\n\nYato won the dual")
else:
    print("\n\nThe evil Shadow dragon triumphs")  



   #spine of stellar dragon-random chance to increase damage done by 50% or mitigate 35% damage taken
   #fleur cannon- increases dmg by 15-35% per hit and heals 5hp
   #orchards bounty- heals randomly 5-10 hp and deals (11-heal)% extra dmg
   #harmonic symphony- mitigates damage by 50-70% and increases dmg by (100-mitigation/3)

   #Will of the cavalry- randomly occurs: either heals 10hp;increases 5% dmg;mitigates 10% dmg

   #Grudge- mitigates dmg by 10-30% and increases dmg by (30-mitigation)
   #Astral barrage- increases dmg by 20% and heals 5hp
   #Scion of the war torn land- increases dmg by 2x
   #Nightglare- mitigates 50-75% dmg and heals (mitigation//10)hp


     #BUg FIXES:
          #check if hp=0 before healing using partial buff
          #balancing issues
                #harmonic symphony op- dmg neft
                #forest relics are trash needs buff