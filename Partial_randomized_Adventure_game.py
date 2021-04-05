import random as ran
name=input("Enter character name:")
og,gob,dem=0,0,0
item=0
done=[]
hp=600
que=[f"{name} encounters a broken hallway that leads to the gem",f"{name} finds a black enchanted rope which is winded up around the gem",f"{name} finds a seedling and an pond of poison that can even melt iron"]
wea=["sword","bow","shield"]
print(f"{name} is the hero of the great kingdom Leaf\nHe has to go save the world by finding the hidden treasure located in the forest of Dare that can heal anything under the sky\notherwise the world might suffer human extinction due to the CO19 virus")
print(f"{name} enters the forest Dare")
while item==0 and hp>0:
  mon=ran.randrange(1,4)
  if mon == 1 and og!=1:
    if gob==1 or dem==1:
        print(f"Moving Forward after the last battle")
    print(f"{name} encounters an Orgre");
    pon=wea[ran.randrange(0,len(wea)-1)]
    print(f"{name} pulls out a {pon}")
    act=input(f"Will {name} react to the monster or will the hero run?(act/run)")
    if act=="act" and pon=="bow":
        print(f"{name} reacts and....deafeats the Orgre by shoting a blazing arrow right across the the monster's forehead")
        og=1;
        print(f"{name} recieves a Ruby gem by the Fire spirt of the Forest")
        if gob!=1 and dem!=1:
             mon = ran.randrange(2,4)
        elif gob==1:
             mon = 3
        else:
             mon = 2 
    elif act=="run":
      print(f"{name} was able to escape")
      print(f"After escaping {name} finds the Spirit Tomb of Fire\n {name} enters the temple")
      while True:
         prox=ran.randrange(0,len(que))
         if prox not in done:
            n=prox
            break
            
      print(f"After some wandring {que[n]}")
      if n==0:
        print("The ceiling looks very strong")
        ans=input("What weapon will you use(sword/bow/shield)")
        if ans=="bow":
          print(f"{name} used his rope arrow spell to swing to get the gem")
          og=1
        else:
          print(f"{name} failed")
          hp=0
      elif n==1:
        print(f"{name} notices some dark aura coming out of it")
        ans=input("What weapon will you use(sword/bow/shield)")
        if ans=="sword":
          print(f"{name} used his holy sword to cancel out the dark aura and cuts open the string to get the gem")
          og=1
        else:
          print(f"{name} failed")
          hp=0
      else:
        print("'Poison helps to grow'")
        ans=input("What weapon will you use(sword/bow/shield)")
        if ans=="shield":
          print(f"{name} used his unmeltable shields as a utensil to pour the poison from the ocean on the seedling")
          print("The seedling grew and became a gem")
          print(f"{name} plucks the gem")
          og=1
        else:
          print(f"{name} failed")
          hp=0
      done.append(n)

    else:
        hp=hp-100
        print(f"{name} lost 100 health points")
        print(f"{name} decided to flee from the battle")
        continue  
  if mon==2 and gob!=1:
        if dem==1 or og==1:
            print(f"Moving Forward after the last battle")
        print(f"{name} encounters an Goblin King");
        pon=wea[ran.randrange(0,len(wea)-1)]
        print(f"{name} pulls out a {pon}")
        act=input(f"Will {name} react to the monster or will the hero run?(act/run)")
        if act=="act" and pon=="shield":
            print(f"{name} reacts and....deafeats the Goblin king by the reflective damage done by the shield")
            gob=1;
            print(f"{name} receives an Emerald gem by the Wind spirit")
            if og!=1 and dem!=1:
              mon = ran.randrange(1,4,2)
            elif og==1:
              mon = 3
            else:
              mon = 1   
          
        elif act=="run":
            print(f"{name} was able to escape")
            print(f"After escaping {name} finds the Spirit Tomb of Wind\n {name} enters the temple")
            while True:
                prox=ran.randrange(0,len(que))
                if prox not in done:
                    n=prox
                    break
            print(f"After some wandring {que[n]}")
            if n==0:
              print("The ceiling looks very strong")
              ans=input("What weapon will you use(sword/bow/shield)")
              if ans=="bow":
                print(f"{name} used his rope arrow spell to swing to get the gem")
                gob=1
              else:
                print(f"{name} failed")
                hp=0
            elif n==1:
              print(f"{name} notices some dark aura coming out of it")
              ans=input("What weapon will you use(sword/bow/sheild)")
              if ans=="sword":
                print(f"{name} used his holy sword to cancel out the dark aura and cuts open the string to get the gem")
                gob=1
              else:
                print(f"{name} failed")
                hp=0
            else:
              print("'Poison helps to grow'")
              ans=input("What weapon will you use(sword/bow/sheild)")
              if ans=="shield":
                print(f"{name} used his unmeltable shields as a utensil to pour the poison from the ocean on the seedling")
                print("The seedling grew and became a gem")
                print(f"{name} plucks the gem")
                gob=1
              else:
                print(f"{name} failed")
                hp=0
            done.append(n)  
        else:
            hp=hp-100
            print(f"{name} lost 100 health points")
            print(f"{name} decided to flee from the battle")
            continue

  if mon==3 and dem!=1:
          if gob==1 or og==1:
              print(f"Moving Forward after the last battle")
          print(f"{name} encounters an Arch Demon");
          pon=wea[ran.randrange(0,len(wea)-1)]
          print(f"{name} pulls out a {pon}")
          act=input(f"Will {name} react to the monster or will the hero run?(act/run)")
          if act=="act" and pon=="sword":
              print(f"{name} reacts and....deafeats the Arch Demon by the Holy damage done by the sword")
              dem=1;
              print(f"{name} recieves a Sapphire gem by the spirit of time")
              if og!=1 and gob!=1:
                mon = ran.randrange(2,0,-1)
              elif gob==1 and og!=1:
                mon = 1
              elif gob==1 and og!=1 :
                mon = 2   
          
          elif act=="run": 
              print(f"{name} was able to escape")
              print(f"After escaping {name} finds the Spirit Tomb of Time\n {name} enters the temple")
              while True:
                  prox=ran.randrange(0,len(que))
                  if prox not in done:
                      n=prox
                      break
              print(f"After some wandring {que[n]}")
              if n==0:
                print("The ceiling looks very strong")
                ans=input("What weapon will you use(sword/bow/shield)")
                if ans=="bow":
                  print(f"{name} used his rope arrow spell to swing to get the gem")
                  dem=1
                else:
                  print(f"{name} failed")
                  hp=0
              elif n==1:
                print(f"{name} notices some dark aura coming out of it")
                ans=input("What weapon will you use(sword/bow/shield)")
                if ans=="sword":
                  print(f"{name} used his holy sword to cancel out the dark aura and cuts open the string to get the gem")
                  dem=1
                else:
                  print(f"{name} failed")
                  hp=0 
              else:
                print("'Poison helps to grow'")
                ans=input("What weapon will you use(sword/bow/sheild)")
                if ans=="shield":
                  print(f"{name} used his unmeltable shield as a utensil to pour the poison from the ocean on the seedling")
                  print("The seedling grew and became a gem")
                  print(f"{name} plucks the gem")
                  dem=1
                else:
                  print(f"{name} failed")
                  hp=0
              done.append(n)
          else:
              hp=hp-100
              print(f"{name} lost 100 health points")
              print(f"{name} decided to flee from the battle")
              continue
             
  if gob+og+dem==3:
        print(f"Reaching the end of the Forest {name} finds a Ancient Seal")
        print(f"The gems start reacting to the seal, {name} places all the gems on the seal")
        print(f"{name} recives the the hidden orb that can cure anything")
        print(f"{name} used it to save the village and was remembered as a Legend")
        item=1;
if hp<=0:
  print("You Died")        
