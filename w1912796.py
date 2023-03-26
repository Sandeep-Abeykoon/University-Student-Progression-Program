# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# UOW Student ID: w1912796
# IIT Student ID: 20210057
# Date: 16/04/2022 


# Defining functions
def student_progress(pro_coun,pro_mt_coun,mod_r_coun,excl_coun,progr_list,file_object,mode):
    """This function handles the student progression"""

   # Initializing the local variables 
    pass_credit = 0
    defer_credit = 0
    fail_credit = 0
    result = ""

    # Getting the marks and validation
    while True:
        pass_credit = input_validation("pass")
        defer_credit = input_validation("defer")
        fail_credit = input_validation("fail")

        if (pass_credit + defer_credit + fail_credit) == 120:
            break
        print("\nTotal incorrect\n")
            
    # Printing the progression
    if pass_credit == 120:
        result = "Progress"
        print("\n" + result)
        pro_coun+=1
        
    elif pass_credit == 100:
        result = "Progress(module trailer)"
        print("\n" + result)
        pro_mt_coun+=1
        
    elif fail_credit >= 80:
        result = "Exclude"
        print("\n" + result)
        excl_coun+=1
        
    else:
        result = "Module retriever"
        print("\n" + result)
        mod_r_coun+=1
        
    print('\n',('-' * 70),"\n")

    # appending data into the list
    progr_list.append([result,"-",str(pass_credit) + ", " + str(defer_credit) + ", " + str(fail_credit)])

    if file_mode == True:
        # Writing rhe data into the text file
        file_object.write(result + " - " + str(pass_credit) + ", " + str(defer_credit) + ", " + str(fail_credit) + "\n")
    
    return pro_coun,pro_mt_coun,mod_r_coun,excl_coun,progr_list




def input_validation (name):
    """This function is get, validate and return the marks"""

    # Initialzing the local varables
    credit_range = [0,20,40,60,80,100,120]
    
    while True:
        try:
            marks = int(input("Enter the credits at " + name + "\t: "))
            if marks in credit_range:
                break
            print("Out of range\n")
        except ValueError:
            print("Integer required\n")
    return marks




def hori_histogram(progress):
    """This function is to represent the student progression using a Horizontal Histogram"""
    
    #Initializing local variables
    headings = ["Progress","Trailer","Retriever","Excluded"]
    total_students = sum(progress)
        
    print("\n--------------------------------------------------------------------\n")
    print("   HORIZONTAL HISTOGRAM \n")

    # Printing the histogram using a for loop
    for i in range(4):
        print(headings[i],progress[i],"\t:",("*" * progress[i]))
    print("\n",total_students,"Outcomes in total")
    print("\n----------------------------------------------------------------------\n")



    
def verti_histogram(progress):
    """This function is to represent the student progression using a Vertical Histogram"""

    # Initializing local variables
    list_max = max(progress)
    total_students = sum(progress)
    
    print("\t\t   VERTICAL HISTOGRAM\n")
    print("Progress",progress[0],"\tTrailing",progress[1],"\tRetriever",progress[2],"\tExcluded",progress[3])
    
    # Printing the histogram using a nested for loop
    for i in range (1,(list_max + 1)):
        for x in progress:
            if x >= i:
                print("    *", end = "\t\t")
            else:
                print("     ", end = "\t\t")
        print()
    print("\n",total_students,"Outcomes in total")
    print("\n----------------------------------------------------------------------\n")



    
def list_print(progr_list):
    """This function is to print the list_data"""

    print("   LIST OUTPUT \n")
    for data in progr_list:
        print(*data)    # refered https://stackoverflow.com/ to print liss without brackets    
    print("\n----------------------------------------------------------------------\n")



    
def file_print():
    """This function is to print the data from the text file"""

    file_object = open("progression_data.txt",'r')
    
    print("   TEXTFILE OUTPUT \n") 

    # Printing the data from the text file
    for data in file_object:
        print(data[:-1])
    print("\n----------------------------------------------------------------------\n")
        
    file_object.close()



    
def staff(file_mode):
    """This function runs the program for the staff version"""

    # Initializing the local variables
    prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = 0,0,0,0,[]
    file_object = ""

    # Opening the file object if file mode == True
    if file_mode == True:
        file_object = open("progression_data.txt",'w')
    
    while True:
        print("\n\n",('-' * 10),"STAFF VERSION",('-' * 10),"\n")
        prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = student_progress(prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list,file_object,file_mode)
                    
        print("\nWould you like to enter another set of data ?\n")

        while True:
            option = input("Enter 'y' for yes or 'n' to quit and view the results : ").lower()            
            if option == 'y' or option == 'n':
                break
            else:
                print("Please enter a valid option\n")
        if option == 'n':
            if file_mode == True:
                file_object.close()
            break
    return prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list 
 
    

# Initializing the variables
option = ""
option_list = ['1','2','3','4','5']
progr_list = []
file_object = ""
file_mode = 0
prog_coun = 0
prog_mt_coun = 0
mod_ret_coun = 0
exclude_coun = 0

# Menu
while True:    
    print("\n\n",('-' * 15),"UNIVERSITY PROGRESIION PROGRAM",('-' * 15),"\n\n\n\t1 ----> MAIN VERSION\n\t2 ----> VERTICAL HISTOGRAM(extension)\n\t3 ----> LIST/TUPLE/DIRECTOTY (extension)\n\t4 ----> TEXT FILE (extension)\n\t5 ----> QUIT\n\n")

    # Getting and validating user option
    while True:
        option = input("Enter your option : ")
        if option in option_list:
            break
        else:
            print("Please enter a valid option\n")
    print("\n")

    # Main version
    if option == '1':
        option == None
        
        while True:
            print("\t1 ----> STUDENT VERSION\n\t2 ----> STAFF VERSION\n\t3 ----> RETURN TO MAIN MENU\n\n")

            # Getting and validating user option
            while True:
                option = input("Enter your option : ")
                if option in option_list[:3]:
                    break
                else:
                    print("Please enter a valid input\n")

            # Student Version
            if option == '1':
                option = None
                file_mode = False
                print("\n\n",('-' * 10),"STUDENT VERSION",('-' * 10),"\n")
                student_progress(prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list,file_object,file_mode)
                    

            # Staff Version
            elif option == '2':
                option == None
                file_mode = False
                prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = staff(file_mode)
                hori_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])

            else:
                option = None
                break


    #VERTICAL HISTOGRAM(extension) Version 
    elif option == '2':
        option = None
        file_mode = False
        prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = staff(file_mode)
        hori_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        verti_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        
    #LIST/TUPLE/DIRECTOTY (extension) version
    elif option == '3':
        option = None
        file_mode = False
        prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = staff(file_mode)
        hori_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        verti_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        list_print(progr_list)
        
    #TEXT FILE (extension) version
    elif option == '4':
        option = None
        file_mode = True
        prog_count,prog_mt_coun,mod_ret_coun,exclude_coun,progr_list = staff(file_mode)
        hori_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        verti_histogram([prog_coun,prog_mt_coun,mod_ret_coun,exclude_coun])
        list_print(progr_list)
        file_print()

    # Exiting the program
    else:
        option = None
        break

print("Thank you for using our student progression program")
        
        
        
        

                
               
                

        
