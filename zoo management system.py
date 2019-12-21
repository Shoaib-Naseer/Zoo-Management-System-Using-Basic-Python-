check1=0 #creating check to use in loop
check2=0 #creating check to use in loop
check3=0 #creating check to use in loop
check4=0 #creating check to use in loop
opp='a'  #defining the variable
while opp!='c': #defining loop exit condition
    opp=input("WELCOME TO ZOO MANAGEMENT SYSTEM \nIf you want to add record of animals then Please press \'a\' \
    to add record.\nIf you want to edit record then please press \'e\' \nIf you want to View the records then \
    please press \'v\' \nIf you want to search a record then press \'s\' \nIf you want to close the program \
    then please press \'c\' \n :") #asking the user if user want to add,view,search,edit until he closes the program
    if opp=='a' or opp=='e' or opp=='v' or opp=='s' or opp=='c':#applying condition that if user enters any of these keys,then program contniues
        if opp=='a':#if user enters "a" then this condition will be executed
            num=eval(input("How many animals records do you want to enter (max entries= 4)"))#asking user that how many entries user wants to enter
            if num>=1 and num<=4:#applying condition that user must enter entries from 1 to 4
                i=1# creating check for loop
                while num!=i-1:#applying exit condition for loop that when num==i-1 loop terminates
                    if i==1:#checking the value of i and then execute this step
                        animal_name1=input("Enter  1st Animal name :")#taking user input
                        cage_no1=input("Enter 1st Cage number :")#taking user input
                        feed_no1=input("Enter 1st Feed Number :")#taking user input
                        breed_no1=input("Enter 1st breed :")#taking user input
                        record1=("The 1st record of animal is "+str(animal_name1)+" - "+str(cage_no1)+" - "+str(feed_no1)+\
                                 " - "+str(breed_no1))#storing all record of 1 entity in one variable
                        check1=1#applying another check so that we can use it in other functions of this program
                        i+=1#taking increment in i
                    elif i==2:#checking the value of i and then execute this step 
                        animal_name2=input("Enter 2nd Animal name :")#taking user input
                        cage_no2=input("Enter 2nd Cage number :")#taking user input
                        feed_no2=input("Enter 2nd Feed Number :")#taking user input
                        breed_no2=input("Enter 2nd breed :")#taking user input
                        record2="The 2nd record of animal is "+str(animal_name2)+" - "+str(cage_no2)+" - "+str(feed_no2)+\
                                 " - "+str(breed_no2)#storing all record of 1 entity in one variable
                        check2=1#applying another check so that we can use it in other functions of this program
                        i+=1
                    elif i==3:#checking the value of i and then execute this step
                        animal_name3=input("Enter 3rd Animal name :")#taking user input
                        cage_no3=input("Enter 3rd Cage number :")#taking user input
                        feed_no3=input("Enter 3rd Feed Number :")#taking user input
                        breed_no3=input("Enter 3rd breed :")#taking user input
                        record3=("The 1st record of animal is "+str(animal_name3)+" - "+str(cage_no3)+" - "+str(feed_no3)+\
                                 " - "+str(breed_no3))#storing all record of 1 entity in one variable
                        check3=1#applying another check so that we can use it in other functions of this program
                        i+=1
                    else:#if i==4 then this step will executed
                        animal_name4=input("Enter 4th Animal name :")#taking user input
                        cage_no4=input("Enter 4th Cage number :")#taking user input
                        feed_no4=input("Enter 4th Feed Number :")#taking user input
                        breed_no4=input("Enter 4th breed :")#taking user input
                        record4=("The 1st record of animal is "+str(animal_name4)+" - "+str(cage_no4)+" - "+str(feed_no4)+\
                                 " - "+str(breed_no4))#storing all record of 1 entity in one variable
                        check4=1#applying another check so that we can use it in other functions of this program
                        i+=1
            else:#if user enter a number not from above condition then only this step will be executed
               print ("wrong number")
                        
        elif opp=='e':#if user enters e to edit record
                Record_no=eval(input("Enter the record number to be edited"))#taking user input
                if Record_no<=4 and Record_no>=1:#applying condition that user must have to enter numbers from 1 to 4
                    if Record_no==1:#if user enter 1 then only this record will be executed
                        animal_name1=input("Enter  1st Animal name :")#taking user input
                        cage_no1=input("Enter 1st Cage number :")#taking user input
                        feed_no1=input("Enter 1st Feed Number :")#taking user input
                        breed_no1=input("Enter 1st breed :")#taking user input
                        record1="The 1st record of animal is "+str(animal_name1)+" - "+str(cage_no1)+" - "+str(feed_no1)+\
                                 " - "+str(breed_no1)#storing all record of 1 entity in one variable
                    elif Record_no==2:#if user enter 2 then only this record will be executed
                          
                          animal_name2=input("Enter 2nd Animal name :")#taking user input
                          cage_no2=input("Enter 2nd Cage number :")#taking user input
                          feed_no2=input("Enter 2nd Feed Number :")#taking user input
                          breed_no2=input("Enter 2nd breed :")#taking user input
                          record2="The 2nd record of animal is "+str(animal_name2)+" - "+str(cage_no2)+" - "+str(feed_no2)+\
                                 " - "+str(breed_no2)#storing all record of 1 entity in one variable
                    elif Record_no==3:#if user enter 3 then only this record will be executed
                          animal_name3=input("Enter 3rd Animal name :")#taking user input
                          cage_no3=input("Enter 3rd Cage number :")#taking user input
                          feed_no3=input("Enter 3rd Feed Number :")#taking user input
                          breed_no3=input("Enter 3rd breed :")#taking user input
                          record3="The 1st record of animal is "+str(animal_name3)+" - "+str(cage_no3)+" - "+str(feed_no3)+\
                                     " - "+str(breed_no3)#storing all record of 1 entity in one variable
                    else:##if user enter 4 then only this record will be executed
                        
                        animal_name4=input("Enter 4th Animal name :")#taking user input
                        cage_no4=input("Enter 4th Cage number :")#taking user input
                        feed_no4=input("Enter 4th Feed Number :")#taking user input
                        breed_no4=input("Enter 4th breed :")#taking user input
                        record4="The 1st record of animal is "+str(animal_name4)+" - "+str(cage_no4)+" - "+str(feed_no4)+\
                                 " - "+str(breed_no4)#storing all record of 1 entity in one variable
                            
                                                     
                else:#if user doesnt enter number from above condition then only this step will be executed
                    print("Not Found")
        
        elif opp=='v':#if user enters v to view records then this step will be executed
            Record_no=eval(input("which record No do you want to view. please enter record No. :"))#taking user input
            if Record_no>=1 and Record_no<=4:#applying condition so that user must enter value from 1 to 4
                if Record_no==1:#if user enter 1 then only this record will be executed
                    if check1==1:#this will check that whether the record exists or not
                        print (record1)
                    else:
                        print ("Not Found")
                elif Record_no==2:#this will check whether user enter 2
                    if check2==1:#this will check that whether the record exists or not
                        print (record2)
                    else:
                        print ("Not Found")
                elif  Record_no==3:#this will check whether user enter 3
                    if check3==1:#this will check that whether the record exists or not
                        print (record3)
                    else:
                        print ("Not Found")
                elif Record_no==4:#this will check whether user enter 4
                    
                    if check4==1:#this will check that whether the record exists or not
                        print (record4)
                    else:
                        print ("Not Found")
                else:#if user doesnt enter number from given condition then this will executed
                    print ("Record Not Found")
        elif opp=='s':#if user enter s to search record in program
            Record_=input("If you want to search from animal name then press \'a\' \nIf you want to search\
from feed number the press \'f\' \nIf you want to search from breed number press \'b\' \nIf you want to \
search from cage no then press \'c\' \n: ")#taking user input
            if Record_=='a':#if user press a
                animal_search=input("enter animal name :")#taking user input
                if check1==1:#this will check whether record exists and then check from it                    
                    if animal_search==animal_name1:
                        chck1=0
                        print ("Record Find \n",record1)
                    else:
                        chck1=1
                else:
                    chck1=1
                    
                if check2==1:#this will check whether record exists and then check from it
                    if animal_search==animal_name2:
                        chck2=0
                        print ("Record Find \n",record2)
                    else:
                        chck2=2
                else:
                    chck2=2
                if check3==1:#this will check whether record exists and then check from it
                    if animal_search==animal_name3:
                        chck3=0
                        print ("Record Find \n",record3)
                    else:
                        chck3=3
                else:
                    chck3=3
                if check4==1:
                    if animal_search==animal_name4:
                        chck4=0
                        print ("Record Find \n",record4)
                    else:
                        chck4=4
                else:
                    chck4=4
                if chck1==1 and chck2==2 and chck3==3 and chck4==4:#this will check from each record whether it is present or not if all are present then this will execute
                    print ("record not Found")
            if Record_=='b':#if user wants to search from breed
                breed_search=input("enter breed no :")#taking user input
                if check1==1:#this will check whether each record exists and then check from it                    
                    if breed_search==breed_no1:
                        chck1=0
                        print ("Record Find \n",record1)
                    else:
                        chck1=1
                else:
                    chck1=1
                if check2==1:#this will check whether each record exists and then check from it
                    if breed_search==breed_no2:
                        chck2=0
                        print ("Record Find \n",record2)
                    else:
                        chck2=1
                else:
                    chck2=1
                if check3==1:#this will check whether each record exists and then check from it
                    if breed_search==breed_no3:
                        chck3=0
                        print ("Record Find \n",record3)
                    else:
                        chck3=1
                else:
                    chck3=1
                if check4==1:#this will check whether each record exists and then check from it
                    if breed_search==breed_no4:
                        chck4=0
                        print ("Record Find \n",record4)
                    else:
                        chck4=1
                else:
                    chck4=1
                if chck1==1 and chck2==1 and chck3==1 and chck4==1:#this will check from each record whether it is present or not if all are present then this will execute
                    print ("record not Found")
            if Record_=='f':#if user want to search from feed
                feed_search=input("enter feed no :")#taking user input
                if check1==1:#this will check whether each record exists and then check from it                    
                    if feed_search==feed_no1:
                        chck1=0
                        print ("Record Find \n",record1)
                    else:
                        chck1=1
                else:
                    chck1=1
                if check2==1:#this will check whether each record exists and then check from it
                    if feed_search==feed_no2:
                        chck2=0
                        print ("Record Find \n",record2)
                    else:
                        chck2=1
                else:
                    chck2=1
                if check3==1:#this will check whether each record exists and then check from it
                    if feed_search==feed_no3:
                        chck3=0
                        print ("Record Find \n",record3)
                    else:
                        chck3=1
                else:
                    chck3=1
                if check4==1:#this will check whether each record exists and then check from it
                    if feed_search==feed_no4:
                        chck4=0
                        print ("Record Find \n",record4)
                    else:
                        chck4=1
                else:
                    chck4=1
                if chck1==1 and chck2==1 and chck3==1 and chck4==1:#this will check from each record whether it is present or not if all are present then this will execute
                    print ("record not Found")
                
            if Record_=='c':#if user want to search from cage no
                cage_search=input("enter cage number :")#taking user input
                if check1==1:#this will check whether each record exists and then check from it                    
                    if cage_search==cage_no1:
                        chck1=0
                        print ("Record Find \n",record1)
                    else:
                        chck1=1
                else:
                    chck1=1
                if check2==1:#this will check whether each record exists and then check from it
                    if cage_search==cage_no2:
                        chck2=0
                        print ("Record Find \n",record2)
                    else:
                        chck2=1
                else:
                    chck2=1
                if check3==1:#this will check whether each record exists and then check from it
                    if cage_search==cage_no3:
                        chck3=0
                        print ("Record Find \n",record3)
                    else:
                        chck3=1
                else:
                    chck3=1
                if check4==1:#this will check whether each record exists and then check from it
                    if cage_search==cage_no4:
                        chck4=0
                        print ("Record Find \n",record4)
                    else:
                        chck4=1
                else:
                    chck4=1
                if chck1==1 and chck2==1 and chck3==1 and chck4==1:#this will check from each record whether it is present or not if all are present then this will execute
                    print ("record not Found")
                
                    
    else:#if user doesnt enter a valid key from main condition
        print ("you enter envalid key. TrY Again")
                