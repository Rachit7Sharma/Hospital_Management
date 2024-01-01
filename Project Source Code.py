import pymysql as x
import random
from random import randrange
import datetime
from datetime import timedelta

try:
    db=x.connect(host="localhost", user="root", password="amazingspiderman2", db="hospital")

    cur=db.cursor()


    print("Connection was established succesfully","\n")
        

except:

    db=x.connect(host="localhost", user="root", password="amazingspiderman2")
    cur=db.cursor()

    cur.execute("create database hospital;")
    db.commit()




def Patient():
    while True:
        print("\n")
        print("Welcome User, How can I help you today?","\n")
        print("1. Registering the details of the Patient")
        print("2. Scheduling an appointment")
        print("3. Display the List of our Doctors available for you 24/7")
        print("4. Display the Services offered by our Hospital")
        print("5. Modify appointment details")
        print("6. Logout","\n")
        p=int(input("Please enter your choice: "))
        print("                                                                                                                                               ")
        

        if p==1:
            print("                                                                                                                                              ")
            Aadhar_No=int(input("Enter Aadhar Number of the Patient: "))
            Name=input("Enter Patient's Name: ")
            Age=int(input("Enter Patient's Age: "))
            Gender=input("Enter Patient's Gender:  ")
            Phone_No=int(input("Enter Contact Number: "))
            cur.execute("use hospital;")

   
            m="insert into Patient(Aadhar_No,Patient_Name,Age,Gender,Phone_No) values(%s,%s,%s,%s,%s);"
            print("                                                                                                                                              ")

            try:
                cur.execute(m,(Aadhar_No,Name,Age,Gender,Phone_No))
                db.commit()
                print("Record added successfully")
                    

            except:
                print("Unable to add record")
        

        elif p==2:
            print("                                                                                                                                              ")
            Aadhar_No=(input("Enter Aadhar Number of the Patient: "))
            n="select Aadhar_No,Doctor_Required,Date_Scheduled from Appointment;"
            rr=cur.execute(n)
            rows=cur.fetchall()
            db.commit()

            for i in rows:
                if i[0]==Aadhar_No:
                    print("                                                                                                                                        ")
                    print("Welcome User, How can I guide you today","\n")
                    print("1. Schedule appointment with a Doctor")
                    print("2. Schedule appointment for a Test","\n")
                    h=int(input("Please enter your choice: "))

                    if h==1:
                        print("                                                                                                                                    ")
                        print("The following Doctors are available","\n")
                        print("1. Neurologist")
                        print("2. Orthopedist")
                        print("3. Rheumatologist")
                        print("4. Cardiologist")
                        print("5. Psychiatrist")
                        print("6. ENT Specialist","\n")
                        j=int(input("Please enter the code for the Doctor: "))

                        if j==1:
                            Doctor_Name="Neurologist"

                        elif j==2:
                            Doctor_Name="Orthopedist"

                        elif j==3:
                            Doctor_Name="Rheumatologist"

                        elif j==4:
                            Doctor_Name="Cardiologist"

                        elif j==5:
                            Doctor_Name="Psychiatrist"

                        elif j==6:
                            Doctor_Name="ENT Specialist"

                        else:
                            print("Please select a valid option")

                        cur.execute("use hospital;")

                        start_date=datetime.date(2022, 3, 4)
                        end_date=datetime.date(2022, 4, 4)
                        t= end_date - start_date
                        d= t.days
                        random_number_of_days = random.randrange(d)
                        Date_Scheduled=start_date + datetime.timedelta(days=random_number_of_days)
                            

                        m="insert into Appointment(Aadhar_No,Doctor_Required,Date_Scheduled) values (%s,%s,%s);"
                        print("                                                                                                                                              ")

                        
                        try:
                            cur.execute(m,(Aadhar_No,Doctor_Name,Date_Scheduled))
                            db.commit()
                            print("Appointment Scheduled successfully on",Date_Scheduled)
                            break   

                        except:
                            print("Unable to schedule the appointment, Please try again later")
                            break
                            
                            

                    elif h==2:
                        print("                                                                                                                                    ")
                        print("The following Facilities are available","\n")
                        print("1. X-Ray")
                        print("2. MRI")
                        print("3. CT Scan")
                        print("4. Endoscopy")
                        print("5. Dialysis")
                        print("6. Ultrasound")
                        print("7. EEG")
                        print("8. ENMG")
                        print("9. ECG","\n")
                        j=int(input("Please enter the code for the Facility: "))
                        Doctor_Name="Lab Technician"
                        cur.execute("use hospital;")

                        m="insert into Appointment(Aadhar_No,Doctor_Required,Date_Scheduled) values (%s,%s,%s);"
                        print("                                                                                                                                              ")


                        start_date=datetime.date(2022, 3, 4)
                        end_date=datetime.date(2022, 4, 4)
                        t= end_date - start_date
                        d= t.days
                        random_number_of_days = random.randrange(d)
                        Date_Scheduled=start_date + datetime.timedelta(days=random_number_of_days)

                        
                        try:
                            cur.execute(m,(Aadhar_No,Doctor_Name,Date_Scheduled))
                            db.commit()
                            print("Appointment Scheduled successfully on",Date_Scheduled)
                            break    

                        except:
                            print("Unable to schedule the appointment, Please try again later")
                            break
                        

                
                    else:
                        print("Please select a valid option")

                else:
                    print("\n","Please register the Patient first")
                        

            

        elif p==3:
            cur.execute("use hospital;")
            n="select * from Doctors;"
            try:
                rr=cur.execute(n)
                rows=cur.fetchall()
                db.commit()
                print("_"*50)
                print("Doctor's Name","\t\t","Area of Specialization")
                print("_"*50)

                for i in rows:
                    print(i[0]+"\t\t"+i[1])
                    print("_"*50)
                

            except:
                print("Unable to fetch records")

        elif p==4:
            cur.execute("use hospital;")
            n="select * from Services;"
            try:
                rr=cur.execute(n)
                rows=cur.fetchall()
                db.commit()
                print("_"*20)
                print("Available Services")
                print("_"*20)

                for i in rows:
                    print(i[0])
                    print("_"*20)
                

            except:
                print("Unable to fetch records")
                

        elif p==5:
            print("                                                                                                                                              ")
            Aadhar_No=(input("Enter Aadhar Number of the Patient: "))
            cur.execute("use hospital;")
            n="select Aadhar_No,Doctor_Required,Date_Scheduled from Appointment;"
            rr=cur.execute(n)
            rows=cur.fetchall()
            db.commit()
            for i in rows:
                if i[0]==Aadhar_No:
                    print("\n","Welcome User, the following Appointment Details can be modified","\n")
                    print("1. Doctor/Facility chosen")
                    print("2. Appointment Date","\n")
                    j=int(input("Please enter your choice: "))

                    if j==1:
                        print("\n","Please specify whether you want to reschedule your appointment for","\n")
                        print("1. Health checkup with another Doctor")
                        print("2. A Test","\n")
                        d=int(input("Please enter the code corresponding to your choice: "))

                        if d==1:
                            print("                                                                                                                                    ")
                            print("The following Doctors are available","\n")
                            print("1. Neurologist")
                            print("2. Orthopedist")
                            print("3. Rheumatologist")
                            print("4. Cardiologist")
                            print("5. Psychiatrist")
                            print("6. ENT Specialist","\n")
                            h=int(input("Please enter the code for the Doctor: "))

                            if h==1:
                                Doctor_Name="Neurologist"

                            elif h==2:
                                Doctor_Name="Orthopedist"

                            elif h==3:
                                Doctor_Name="Rheumatologist"

                            elif h==4:
                                Doctor_Name="Cardiologist"

                            elif h==5:
                                Doctor_Name="Psychiatrist"

                            elif h==6:
                                Doctor_Name="ENT Specialist"

                            else:
                                print("Please select a valid option")

                            try:
                                m="Update Appointment set Doctor_Required=%s where Aadhar_No=%s;"
                                cur.execute(m,(Doctor_Name,Aadhar_No))
                                db.commit()
                                print("\n","Your Appointment has been rescheduled with",Doctor_Name)
                                break
                            
                            except:
                                print("\n","Unable to reschedule your appointment, Please try again later")
                                break

                        elif d==2:
                            print("                                                                                                                                    ")
                            print("The following Facilities are available","\n")
                            print("1. X-Ray")
                            print("2. MRI")
                            print("3. CT Scan")
                            print("4. Endoscopy")
                            print("5. Dialysis")
                            print("6. Ultrasound")
                            print("7. EEG")
                            print("8. ENMG")
                            print("9. ECG","\n")
                            s=int(input("Please enter the code for the Facility: "))
                            Doctor_Name="Lab Technician"
                            try:
                                m="Update Appointment set Doctor_Required=%s where Aadhar_No=%s;"
                                cur.execute(m,(Doctor_Name,Aadhar_No))
                                db.commit()
                                print("\n","Your Appointment has been rescheduled for the selected Test")
                                break
                            
                            except:
                                print("\n","Unable to reschedule your appointment, Please try again later")
                                break

                        else:
                            print("\n","Please select a valid option")
                            break
                        

                    elif j==2:
                        start_date=datetime.date(2022, 3, 4)
                        end_date=datetime.date(2022, 4, 4)
                        t= end_date - start_date
                        d= t.days
                        random_number_of_days = random.randrange(d)
                        Date_Scheduled=start_date + datetime.timedelta(days=random_number_of_days)

                        print("                                                                                                                                  ")
                        try:
                            m="Update Appointment set Date_Scheduled=%s where Aadhar_No=%s;"
                            cur.execute(m,(Date_Scheduled,Aadhar_No))
                            db.commit()
                            print("Your Appointment has been rescheduled for",Date_Scheduled)
                            break
                        
                        except:
                            print("Unable to reschedule your appointment, Please try again later")
                            break
                        
                    else:
                        print("\n","Please select a valid option")

                else:
                    print("Sorry, the Patient is not registered")

                                    

            
        elif p==6:
            break

        else:
            print("Please select a valid option")

            
        
              
def Doctor():
    print("Welcome Doctor, Kindly login through your respective ID to proceed","\n")

    ID=input("Enter your ID: ")
    print("                                                                                                                                               ")
    Passwd=int(input("Enter your Password: "))
    print("                                                                                                                                               ")

    if Passwd==123:
        print("Login Successful","\n")
        try:
            m="select Patient_Name,Age,Gender,Date_Scheduled from Patient,Appointment where Patient.Aadhar_No=Appointment.Aadhar_No and Doctor_Required=%s;"
            rows=cur.execute(m,(ID))
            rr=cur.fetchall()
            db.commit()
            print("\n")
            print("Appointments scheduled are","\n")
            print("_"*100)
            print("Patient_Name","\t\t","Age","\t\t","Gender","\t\t","Date_Scheduled")
            print("_"*100)

            for i in rr:
                print(i[0]+"\t\t\t"+str(i[1])+"\t\t\t"+i[2]+"\t\t\t"+str(i[3]))
                print("_"*100)

        except:
            print("No appointments scheduled for this month")
        
        

    else:
        print("Login Failed, Try again later")

        

while True:
    print("                                                                                                                                               ")
    print("Kindly select from the options below","\n")
    print("1. Patient Login")
    print("2. Doctor Login")
    print("3. Exit the Module","\n")
    c=int(input("Please enter your choice: "))
    print("                                                                                                                                               ")
    

    if c==1:
        Patient()

    elif c==2:
        Doctor()

    elif c==3:
        break

    else:
        print("Please select a valid option")
cur.close()
db.close()

print("Thank You for choosing us","\n")
print("Stay Safe,Stay Healthy!!")
        
    
    
