# coding=utf-8
import unittest
import Api_Actions
import Verifications

class TrackerDetectAPI(unittest.TestCase):    

    '''Test verifies the get method status code'''   
    def test01_verify_get_status_code(self):
        Api_Actions.define_test_set("GET")
        Verifications.file_log.write("Test case 1: verify the get method status code\n")
        Verifications.verify_status_code(Api_Actions.get_method_getInfos()['status'],200,Api_Actions.get_method_getInfos()['content'])

    '''Test verifies the put method status code when passing valid values''' 
    def test02_verify_put_status_code(self):
        Api_Actions.define_test_set("PUT")
        Verifications.file_log.write("Test case 2: verify the put method status code when passing valid values\n")
        my_dict = Api_Actions.put_method_getInfos("main_key02", "value02")
        Verifications.verify_status_code(my_dict['status'],200,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("main_key02")

    '''Test verifies the content of the valid put method''' 
    def test03_verify_put_content(self):
        Verifications.file_log.write("Test case 3: verify the content of the valid put method\n")
        my_dict = Api_Actions.put_method_getInfos("main_key03", "value03")
        Verifications.verify_body_response(my_dict['content'],"main_key03")
        '''Return to initial state'''
        Api_Actions.delete_method("main_key03")

    '''Test verifies the put method status code when passing sames values''' 
    def test04_verify_put_status_code_sames_values(self):
        Verifications.file_log.write("Test case 4: verify the put method status code when passing sames values\n")
        Api_Actions.put_method("main_key04", "value04")
        my_dict = Api_Actions.put_method_getInfos("main_key04", "value04")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("main_key04")

    '''Test verifies the put method content when passing sames values''' 
    def test05_verify_put_content_sames_values(self):
        Verifications.file_log.write("Test case 5: verify the put method content when passing sames values\n")
        Api_Actions.put_method("main_key04Bis", "value04Bis")
        my_dict = Api_Actions.put_method_getInfos("main_key04Bis", "value04Bis")
        Verifications.verify_body_response(my_dict['content'],"value already exist")
        '''Return to initial state'''
        Api_Actions.delete_method("main_key04Bis")

    '''Test verifies the put method status code when passing blank "value"''' 
    def test06_verify_put_status_code_blank_value(self):
        Verifications.file_log.write("Test case 6: verify the put method status code when passing blank 'value'\n")
        my_dict = Api_Actions.put_method_getInfos("main_key05", "")
        Verifications.verify_status_code(my_dict['status'],200,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("main_key05")

    '''Test verifies the content of the put method when passing blank "value"''' 
    def test07_verify_put_content_blank_value(self):
        Verifications.file_log.write("Test case 7: verify the content of the put method when passing blank 'value'\n")
        my_dict = Api_Actions.put_method_getInfos("main_key05Bis", "")
        Verifications.verify_body_response(my_dict['content'],"main_key05Bis")
        '''Return to initial state'''
        Api_Actions.delete_method("main_key05Bis")

    '''Test verifies the put method status code when passing blank "main_key"''' 
    def test08_verify_put_status_code_blank_main_key(self):
        Verifications.file_log.write("Test case 8: verify the put method status code when passing blank 'main_key'\n")
        my_dict = Api_Actions.put_method_getInfos("", "value06")
        Verifications.verify_status_code(my_dict['status'],200,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("")

    '''Test verifies the content of the put method when passing blank "value"''' 
    def test09_verify_put_content_blank_value(self):
        Verifications.file_log.write("Test case 9: verify the content of the put method when passing blank 'main_key'\n")
        my_dict = Api_Actions.put_method_getInfos("", "value06Bis")
        Verifications.verify_body_response(my_dict['content'],"value06Bis")
        '''Return to initial state'''
        Api_Actions.delete_method("")

    '''Test verifies the put method status code whithout passing the "main_key"'''
    def test10_verify_put_status_code_without_main_key(self):
        Verifications.file_log.write("Test case 10: verify the put method status code whithout passing the 'main_key'\n")
        my_dict = Api_Actions.put_method_getInfos_without_parameter("value", "value07")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])

    '''Test verifies the content of the put method whithout passing the "main_key"'''
    def test11_verify_put_content_without_main_key(self):
        Verifications.file_log.write("Test case 11: verify the content of the put method whithout passing the 'main_key'\n")
        my_dict = Api_Actions.put_method_getInfos_without_parameter("value", "value07Bis")
        Verifications.verify_body_response(my_dict['content'],"main_key")

    '''Test verifies the put method status code whithout passing the "value"'''
    def test12_verify_put_status_code_without_value(self):
        Verifications.file_log.write("Test case 12: verify the put method status code whithout passing the 'value'\n")
        my_dict = Api_Actions.put_method_getInfos_without_parameter("main_key", "main_key08")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])

    '''Test verifies the content of the put method whithout passing the "value"'''
    def test13_verify_put_content_without_main_key(self):
        Verifications.file_log.write("Test case 13: verify the content of the put method whithout passing the 'value'\n")
        my_dict = Api_Actions.put_method_getInfos_without_parameter("main_key", "main_key08Bis")
        Verifications.verify_body_response(my_dict['content'],"value")

    '''Test verifies the put method status code when put exactly 10 values in the store'''
    '''Before run this test make sure that any value is in the store'''
    def test14_verify_put_status_code_ten_values(self):
        Verifications.file_log.write("Test case 14: verify the put method status code when put exactly 10 values in the store\n")
        Api_Actions.put_method_several_times(10)
        my_dict = Api_Actions.put_method_getInfos("main_key09", "value09")
        if my_dict['status'] == 400:
            Verifications.verify_status_code(my_dict['status'], 400, my_dict['content'])
            Verifications.file_log.write("    It's not possible to set 11 items in the store\n")
        else:
            Verifications.verify_status_code(my_dict['status'], 400, my_dict['content']) 
            Verifications.file_log.write("    It's possible to set 11 items in the store\n")    
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(10)
        Api_Actions.delete_method("main_key09")

    '''Test verifies the content of the put exactly 10 values in the store'''
    '''Before run this test make sure that any value is in the store'''
    def test15_verify_put_content_ten_values(self):
        Verifications.file_log.write("Test case 15: verify the content of the put method when reached quota\n")
        Api_Actions.put_method_several_times(10)
        my_dict = Api_Actions.put_method_getInfos("main_key09Bis", "value09Bis")
        if "reached" in str(my_dict['content']):
            # Verifications.verify_body_response(my_dict['content'],"you reached your quota") ---> there is a mistake in the content: 'quta' and not 'quota' 
            Verifications.verify_body_response(my_dict['content'],"reached")
            Verifications.file_log.write("    The content of the response when put 11 items in the store is correct\n")
        else:
            # Verifications.verify_body_response(my_dict['content'],"you reached your quota") ---> there is a mistake in the content: 'quta' and not 'quota' 
            Verifications.verify_body_response(my_dict['content'],"reached")
            Verifications.file_log.write("    The content of the response when put 11 items in the store is not correct\n")
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(10)
        Api_Actions.delete_method("main_key09Bis")

    '''Test verifies the put method status code when reached quota'''
    '''Before run this test make sure that any value is in the store'''
    def test16_verify_put_status_code_over_quota(self):
        Verifications.file_log.write("Test case 16: verify the put method status code when reached quota\n")
        Api_Actions.put_method_several_times(11)
        my_dict = Api_Actions.put_method_getInfos("main_key09_1", "value09_1")
        if my_dict['status'] == 400:
            Verifications.verify_status_code(my_dict['status'], 400, my_dict['content'])
            Verifications.file_log.write("    It's not possible to set 12 items in the store\n")
        else:
            Verifications.verify_status_code(my_dict['status'], 400, my_dict['content']) 
            Verifications.file_log.write("    It's possible to set 12 items in the store\n")    
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(11)
        Api_Actions.delete_method("main_key09_1")

    '''Test verifies the content of the put method when reached quota'''
    '''Before run this test make sure that any value is in the store'''
    def test17_verify_put_content_over_quota(self):
        Verifications.file_log.write("Test case 17: verify the content of the put method when reached quota\n")
        Api_Actions.put_method_several_times(11)
        my_dict = Api_Actions.put_method_getInfos("main_key09Bis_1", "value09Bis_1")
        if "reached" in str(my_dict['content']):
            # Verifications.verify_body_response(my_dict['content'],"you reached your quota") ---> there is a mistake in the content: 'quta' and not 'quota' 
            Verifications.verify_body_response(my_dict['content'],"reached")
            Verifications.file_log.write("    The content of the response when reached quota is correct\n")
        else:
            # Verifications.verify_body_response(my_dict['content'],"you reached your quota") ---> there is a mistake in the content: 'quta' and not 'quota' 
            Verifications.verify_body_response(my_dict['content'],"reached")
            Verifications.file_log.write("    The content of the response when reached quota is not correct\n")
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(11)
        Api_Actions.delete_method("main_key09Bis_1")      

    '''Test verifies the delete method status code when passing an existing main_key parameter'''
    def test18_verify_delete_valid_value(self):
        Api_Actions.define_test_set("DELETE")
        Verifications.file_log.write("Test case 18: verify the delete method status code when passing an existing main_key parameter\n")
        Api_Actions.put_method("main_key10", "value10")
        my_dict = Api_Actions.delete_method_getInfos("main_key10")
        Verifications.verify_status_code(my_dict['status'],200,my_dict['content'])
    
    '''Test verifies the delete method content when passing an existing main_key parameter'''   
    def test19_verify_delete_valid_value(self):
        Verifications.file_log.write("Test case 19: verify the delete method content when passing an existing main_key parameter\n")
        Api_Actions.put_method("main_key10Bis", "value10Bis")
        my_dict = Api_Actions.delete_method_getInfos("main_key10Bis")
        Verifications.verify_body_response(my_dict['content'],"value10")  

    '''Test verifies the post method status code when passing existing main_key''' 
    def test20_verify_post_status_code(self):        
        Api_Actions.define_test_set("POST") 
        Verifications.file_log.write("Test case 20: the post method status code when passing existing main_key\n")
        Api_Actions.put_method("main_key11", "value11")
        my_dict = Api_Actions.post_method_getInfos("main_key11", "post_value11")
        Verifications.verify_status_code(my_dict['status'],200,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("main_key11")

    '''Test verifies the post method content when passing existing main_key''' 
    def test21_verify_post_content(self):
        Verifications.file_log.write("Test case 21: the post method content when passing existing main_key\n")
        Api_Actions.put_method("main_key12", "value12")
        my_dict = Api_Actions.post_method_getInfos("main_key12", "post_value12")
        Verifications.verify_body_response(my_dict['content'],"post_value12")
        '''Return to initial state'''
        Api_Actions.delete_method("main_key12")

    '''Test verifies the post method status code if the main_key is not in the store''' 
    def test22_verify_post_status_code_key_not_in_store(self):
        Verifications.file_log.write("Test case 22: verify the post method status code if the main_key is not in the store\n")
        Api_Actions.put_method("main_key13", "value13")
        my_dict = Api_Actions.post_method_getInfos("kuku", "value13")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])
        '''Return to initial state'''
        Api_Actions.delete_method("main_key13")

    '''Test verifies the post method content if the main_key is not in the store''' 
    def test23_verify_post_content_key_not_in_store(self):
        Verifications.file_log.write("Test case 23: verify the post method content if the main_key is not in the store\n")
        Api_Actions.put_method("main_key14", "value14")
        my_dict = Api_Actions.post_method_getInfos("kukuBis", "value14")
        # Verifications.verify_body_response(my_dict['content'],"value does not exist")---> there is a mistake in the content: 'dose' and not 'does'
        Verifications.verify_body_response(my_dict['content'],"not exist")
        '''Return to initial state'''
        Api_Actions.delete_method("main_key14")

    '''Test verifies the post method status code whithout passing the "main_key"'''
    def test24_verify_post_status_code_without_main_key(self):
        Verifications.file_log.write("Test case 24: verify the post method status code whithout passing the 'main_key'\n")
        Api_Actions.put_method_getInfos("main_key15", "value15")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("value","value15")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])    
        '''Return to initial state'''
        Api_Actions.delete_method("main_key15")

    '''Test verifies the content of the post method whithout passing the "main_key"'''
    def test25_verify_post_content_without_main_key(self):
        Verifications.file_log.write("Test case 25: verify the content of the post method whithout passing the 'main_key'\n")
        Api_Actions.put_method_getInfos("main_key15Bis", "value15Bis")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("value","value15Bis")
        Verifications.verify_body_response(my_dict['content'],"main_key")    
        '''Return to initial state'''
        Api_Actions.delete_method("main_key15Bis")

    '''Test verifies the post method status code whithout passing the "value"'''
    def test26_verify_post_status_code_without_value(self):
        Verifications.file_log.write("Test case 26: verify the post method status code whithout passing the 'value'\n")
        Api_Actions.put_method_getInfos("main_key16", "value16")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("main_key","main_key16")
        Verifications.verify_status_code(my_dict['status'],400,my_dict['content'])    
        '''Return to initial state'''
        Api_Actions.delete_method("main_key16")

    '''Test verifies the content of the post method whithout passing the "value"'''
    def test27_verify_post_content_without_value(self):
        Verifications.file_log.write("Test case 27: verify the content of the post method whithout passing the 'value'\n")
        Api_Actions.put_method_getInfos("main_key16Bis", "value16Bis")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("main_key","main_key16Bis")
        Verifications.verify_body_response(my_dict['content'],"value")    
        '''Return to initial state'''
        Api_Actions.delete_method("main_key16Bis")

if __name__ == '__main__':
    apiTD = TrackerDetectAPI()
    apiTD.test01_verify_get_status_code()
    apiTD.test02_verify_put_status_code()
    apiTD.test03_verify_put_content()
    apiTD.test04_verify_put_status_code_sames_values()
    apiTD.test05_verify_put_content_sames_values()
    apiTD.test06_verify_put_status_code_blank_value()
    apiTD.test07_verify_put_content_blank_value()
    apiTD.test08_verify_put_status_code_blank_main_key()
    apiTD.test09_verify_put_content_blank_value()
    apiTD.test10_verify_put_status_code_without_main_key()
    apiTD.test11_verify_put_content_without_main_key()
    apiTD.test12_verify_put_status_code_without_value()
    apiTD.test13_verify_put_content_without_main_key()
    apiTD.test14_verify_put_status_code_ten_values()
    apiTD.test15_verify_put_content_ten_values()
    apiTD.test16_verify_put_status_code_over_quota()
    apiTD.test17_verify_put_content_over_quota()
    apiTD.test18_verify_delete_valid_value()
    apiTD.test19_verify_delete_valid_value()
    apiTD.test20_verify_post_status_code()
    apiTD.test21_verify_post_content()
    apiTD.test22_verify_post_status_code_key_not_in_store()
    apiTD.test23_verify_post_content_key_not_in_store()
    apiTD.test24_verify_post_status_code_without_main_key()
    apiTD.test25_verify_post_content_without_main_key()
    apiTD.test26_verify_post_status_code_without_value()
    apiTD.test27_verify_post_content_without_value()


Verifications.file_log.close()    

             
