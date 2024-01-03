import smtplib
import time

def sendMail(mailId,content):
    #Creating SMTP pipeline object along with port
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("Your Mail Id", "Your password")

    # message to be sent
    message = content
    
    errorMailIds=[]

    for recvMailId in mailId:
        try:
            # sending the mail
            s.sendmail("Your Mail Id", recvMailId, message)
            time.sleep(10)
            
            print(f"{recvMailId} mail sent")
        except Exception:
            errorMailIds.append(recvMailId)

    # terminating the session
    s.quit()

    #return list of mails that are not processed.
    return errorMailIds

try:
    option=int(input("options: \n\t[1] For single sender \n\t[2] For multiple sender \nchoice the options for senders: "))
    
    if(option==1):
        mailId=input("Enter that mailId to send: ")
        content=input("Enter the content of mail need to send ")
        #pass mailId as list for easy to access that mail's along with common sentMail logic
        result=sendMail([mailId],content)

    elif(option==2):
        mailId=input("Enter that mailId's to send seprated by (,) {mail1,mail2,...}: ").split(',')
        content=input("Enter the content of mail need to send ")
        result=sendMail(mailId,content)

    else:
        print("Invalid option")

    if(len(result)==0):
        print("All mail's are send successfully....")
    else:
        print("Error with these mailId's. Please check out those mailId's once again.")
        for mailId in result:
            print(mailId)

except Exception as e:
    print("Invalid input. Please enter 1 or 2 (1/2)")
