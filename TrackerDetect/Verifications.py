# coding=utf-8
from datetime import datetime

date_hour = datetime.now().strftime("%d/%m/%y %H:%M")

file_log = open("File_Test_TrackerDetect.txt", "w")
file_log.write("Tests of the CRUD operation of a rest API \n")
file_log.write("Date and time of the log file generation : {0}".format(date_hour))
file_log.write("     by Shoshana Benhamou\n")
file_log.write(" \n")

def verify_status_code(code, expected_code, content):
    if code/100 == expected_code/100:
        print("Test OK: code response is: "+ str(code) + ", request successed")
        file_log.write("    Test OK: code response is: "+ str(code) + ", request successed\n")         
    elif code/100 == 5:
        print("Test **KO**: code response is: "+ str(code) + ", request failed, because server error. See details:"+ str(content))
        file_log.write("    Test **KO**: code response is: "+ str(code) + ", request failed, because server error. See details:"+ str(content))
        file_log.write(" \n")
    elif code/100 == 4:
        print("Test **KO**: code response is: "+ str(code) + ", request failed, because server error. See details:"+ str(content))
        file_log.write("    Test **KO**: code response is: "+ str(code) + ", request failed. See details: "+ str(content))
        file_log.write(" \n")
    elif code/100 == 2:
        print("Test **KO**: code response is: "+ str(code) + ", request failed, because not expected response. See details:"+ str(content))
        file_log.write("    Test **KO**: code response is: "+ str(code) + ", request failed because not expected response. See details: "+ str(content))
        file_log.write(" \n")    
    else:
        print("Test **KO**: request failed for any reasons.")
        file_log.write("    Test **KO**: request failed for any reasons.")
        file_log.write(" \n")

def verify_body_response(content,value):
    try:
        assert str(value) in str(content)
        print("Test OK: content is exact. See details: "+ str(content))
        file_log.write("    Test OK: content is exact. See details: "+ str(content))
        file_log.write(" \n")
    except:
        print("Test **KO**: content isn't exact. See details: "+ str(content))
        file_log.write("    Test **KO**: content isn't exact. See details: "+ str(content))
        file_log.write(" \n")