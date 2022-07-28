# coding=utf-8

def verify_status_code(code, expected_code, content):
    if code/100 == expected_code/100:
        print("Test OK: code response is: "+ str(code) + ", request successed")
        return True          
    elif code/100 == 5:
        print("Test KO: code response is: "+ str(code) + ", request failed, because server error. See details:"+ str(content))
        return False
    elif code/100 == 4:
        print("Test KO: code response is: "+ str(code) + ", request failed. See details: "+ str(content))
        return False
    elif code/100 == 2:
        print("Test KO: code response is: "+ str(code) + ", request failed. See details: "+ str(content))
        return False    
    else:
        print("Test KO: request failed for any reasons")
        return False

def verify_body_response(content,value):
    try:
        assert str(value) in str(content)
        print("Test OK: content is exact. See details: "+ str(content))
        return True
    except:
        print("Test KO: content isn't exact. See details: "+ str(content))
        return False

    


       




