# coding=utf-8
from re import T
import unittest
import Api_Actions
import allure
from allure_commons.types import AttachmentType
import Verifications_pytest


class TrackerDetect1_GETMethod(unittest.TestCase):

    '''Test verifies the get method status code'''
    @allure.severity(allure.severity_level.BLOCKER)   
    def test01_verify_get_status_code(self):
        if Verifications_pytest.verify_status_code(Api_Actions.get_method_getInfos()['status'],200,Api_Actions.get_method_getInfos()['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the get method status code",attachment_type=AttachmentType.TEXT)
            allure.attach(str(Api_Actions.get_method_getInfos()['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(Api_Actions.get_method_getInfos()['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else: 
            allure.attach("Test KO",name = "Test case: verify the get method status code",attachment_type=AttachmentType.TEXT)
            allure.attach(Api_Actions.get_method_getInfos()['status'], name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(Api_Actions.get_method_getInfos()['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False

class TrackerDetect2_PUTMethod(unittest.TestCase):

    '''Test verifies the put method status code when passing valid values'''
    @allure.severity(allure.severity_level.CRITICAL) 
    def test02_verify_put_status_code(self):
        my_dict = Api_Actions.put_method_getInfos("main_key02", "value02")
        if Verifications_pytest.verify_status_code(my_dict['status'],200,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code when passing valid values",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when passing valid values",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''    
        Api_Actions.delete_method("main_key02")

    '''Test verifies the content of the valid put method''' 
    @allure.severity(allure.severity_level.CRITICAL)
    def test03_verify_put_content(self):
        my_dict = Api_Actions.put_method_getInfos("main_key03", "value03")
        if Verifications_pytest.verify_body_response(my_dict['content'],"main_key03") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the valid put method",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key03", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the valid put method",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key03", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key03")

    '''Test verifies the put method status code when passing sames values'''
    @allure.severity(allure.severity_level.CRITICAL) 
    def test04_verify_put_status_code_sames_values(self):
        Api_Actions.put_method("main_key04", "value04")
        my_dict = Api_Actions.put_method_getInfos( "main_key04", "value04")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code when passing sames values",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when passing sames values",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key04")

    '''Test verifies the put method content when passing sames values''' 
    @allure.severity(allure.severity_level.CRITICAL)
    def test05_verify_put_content_sames_values(self):
        Api_Actions.put_method("main_key04Bis", "value04Bis")
        my_dict = Api_Actions.put_method_getInfos( "main_key04Bis", "value04Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"value already exist") == True:
            allure.attach("Test OK",name = "Test case: verify the put method content when passing sames values",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key04Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method content when passing sames values",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key04Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key04Bis")

    '''Test verifies the put method status code when passing blank "value"''' 
    @allure.severity(allure.severity_level.CRITICAL)
    def test06_verify_put_status_code_blank_value(self):
        my_dict=Api_Actions.put_method_getInfos("main_key05", "")
        if Verifications_pytest.verify_status_code(my_dict['status'],200,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code when passing blank 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when passing blank 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key05")

    '''Test verifies the content of the put method when passing blank "value"''' 
    @allure.severity(allure.severity_level.CRITICAL)
    def test07_verify_put_content_blank_value(self):
        my_dict=Api_Actions.put_method_getInfos("main_key05Bis", "")
        if Verifications_pytest.verify_body_response(my_dict['content'],"main_key05Bis") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the put method when passing blank 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key05Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method when passing blank 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key05Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''    
        Api_Actions.delete_method("main_key05Bis")

    '''Test verifies the put method status code when passing blank "main_key"'''
    @allure.severity(allure.severity_level.CRITICAL) 
    def test08_verify_put_status_code_blank_main_key(self):
        my_dict = Api_Actions.put_method_getInfos("", "value06")
        if Verifications_pytest.verify_status_code(my_dict['status'],200,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code when passing blank 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when passing blank 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''    
        Api_Actions.delete_method("")

    '''Test verifies the content of the put method when passing blank "main_key"''' 
    @allure.severity(allure.severity_level.CRITICAL)
    def test09_verify_put_content_blank_value(self):
        my_dict = Api_Actions.put_method_getInfos("", "value06Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"value06Bis") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the put method when passing blank 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(str(my_dict['content']), name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value06Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method when passing blank 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(str(my_dict['content']), name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value06Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False
        '''Return to initial state'''    
        Api_Actions.delete_method("")  

    '''Test verifies the put method status code whithout passing the "main_key"'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test10_verify_put_status_code_without_main_key(self):
        my_dict = Api_Actions.put_method_getInfos_without_parameter("value", "value07")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT) 
            assert False

    '''Test verifies the content of the put method whithout passing the "main_key"'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test11_verify_put_content_without_main_key(self):
        my_dict = Api_Actions.put_method_getInfos_without_parameter("value", "value07Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"main_key") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the put method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False

    '''Test verifies the put method status code whithout passing the "value"'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test12_verify_put_status_code_without_value(self):
        my_dict = Api_Actions.put_method_getInfos_without_parameter("main_key", "main_key08")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the put method status code whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT) 
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False

    '''Test verifies the content of the put method whithout passing the "value"'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test13_verify_put_content_without_main_key(self):
        my_dict = Api_Actions.put_method_getInfos_without_parameter("main_key", "main_key08Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"value") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the put method whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False

    '''Test verifies the put method status code when put exactly 10 values in the store'''
    '''Before run this test make sure that any value is in the store'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test14_verify_put_status_code_ten_values(self):
        Api_Actions.put_method_several_times(10)
        my_dict = Api_Actions.put_method_getInfos("main_key09", "value09")
        if my_dict['status'] == 400:
            allure.attach("Test OK",name = "Test case: verify the put method status code when put exactly 10 values in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("It's not possible to set 11 items in the store", name = "Comment",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when put exactly 10 values in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach("It's possible to set 11 items in the store", name = "Comment",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False 
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(10)

    '''Test verifies the content of the put exactly 10 values in the store'''
    '''Before run this test make sure that any value is in the store'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test15_verify_put_content_ten_values(self):
        Api_Actions.delete_method("main_key09")
        Api_Actions.put_method_several_times(10)
        my_dict = Api_Actions.put_method_getInfos("main_key09Bis","value09Bis")
        if  "reached" in str(my_dict['content']):
            allure.attach("Test OK",name = "Test case: verify the content of the put method when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: reached", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: reached", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(10)

    '''Test verifies the put method status code when reached quota'''
    '''Before run this test make sure that any value is in the store'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test16_verify_put_status_code_over_quota(self):
        Api_Actions.delete_method("main_key09Bis")
        Api_Actions.put_method_several_times(11)
        my_dict = Api_Actions.put_method_getInfos("main_key09_1", "value09_1")
        if my_dict['status'] == 400:
            allure.attach("Test OK",name = "Test case: verify the put method status code when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("It's not possible to set 12 items in the store", name = "Comment",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the put method status code when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach("It's possible to set 12 items in the store", name = "Comment",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False 
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(11)
        Api_Actions.delete_method("main_key09_1")         

    '''Test verifies the content of the put method when reached quota'''
    '''Before run this test make sure that any value is in the store'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test17_verify_put_content_over_quota(self):
        Api_Actions.put_method_several_times(11)
        my_dict = Api_Actions.put_method_getInfos("main_key09Bis_1", "value09Bis_1")
        if "reached" in str(my_dict['content']):
            allure.attach("Test OK",name = "Test case: verify the content of the put method when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: reached", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the put method when reached quota",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: reached", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method_several_times(11)
        Api_Actions.delete_method("main_key09Bis_1")

class TrackerDetect3_DELETEMethod(unittest.TestCase):   

    '''Test verifies the delete method status code when passing an existing main_key parameter'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test18_verify_delete_valid_value(self):
        Api_Actions.put_method("main_key10", "value10")
        my_dict = Api_Actions.delete_method_getInfos("main_key10")
        if Verifications_pytest.verify_status_code(my_dict['status'],200,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the delete method status code when passing an existing main_key parameter",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test OK",name = "Test case: verify the delete method status code when passing an existing main_key parameter",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False

    '''Test verifies the delete method content when passing an existing main_key parameter'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test19_verify_delete_valid_value(self):
        Api_Actions.put_method("main_key10Bis", "value10Bis")
        my_dict = Api_Actions.delete_method_getInfos("main_key10Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"value10Bis") == True:
            allure.attach("Test OK",name = "Test case: verify the delete method content when passing an existing main_key parameter",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value10Bis", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the delete method content when passing an existing main_key parameter",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value10", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False

class TrackerDetect4_POSTMethod(unittest.TestCase):                    

    '''Test verifies the post method status code when passing existing main_key'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test20_verify_post_status_code(self):
        Api_Actions.put_method("main_key11", "value11")
        my_dict = Api_Actions.post_method_getInfos("main_key11", "post_value11")
        if Verifications_pytest.verify_status_code(my_dict['status'],200,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the post method status code when passing existing main_key",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the post method status code when passing existing main_key",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("200", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key11")

    '''Test verifies the post method content when passing existing main_key'''
    @allure.severity(allure.severity_level.CRITICAL)
    def test21_verify_post_content(self):
        Api_Actions.put_method("main_key12", "value12")
        my_dict = Api_Actions.post_method_getInfos("main_key12", "post_value12")
        if Verifications_pytest.verify_body_response(my_dict['content'],"post_value12") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the valid post method",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key03", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the valid post method",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key03", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key12")

    '''Test verifies the post method status code if the main_key is not in the store'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test22_verify_post_status_code_key_not_in_store(self):
        Api_Actions.put_method("main_key13", "value13")
        my_dict = Api_Actions.post_method_getInfos("kuku", "value13")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the post method status code if the main_key is not in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the post method status code if the main_key is not in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key13")

    '''Test verifies the post method content if the main_key is not in the store''' 
    @allure.severity(allure.severity_level.BLOCKER)
    def test23_verify_post_content_key_not_in_store(self):
        Api_Actions.put_method("main_key14", "value14")
        my_dict = Api_Actions.post_method_getInfos("kukuBis", "value14")
        if Verifications_pytest.verify_body_response(my_dict['content'],"not exist") == True:
            allure.attach("Test OK",name = "Test case: verify the post method content if the main_key is not in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: not exist", name = "Expected response details",attachment_type=AttachmentType.TEXT)
        else:
            allure.attach("Test KO",name = "Test case: verify the post method content if the main_key is not in the store",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: not exist", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert False    
        '''Return to initial state'''
        Api_Actions.delete_method("main_key14")

    '''Test verifies the post method status code whithout passing the "main_key"'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test24_verify_post_status_code_without_main_key(self):
        Api_Actions.put_method_getInfos("main_key15", "value15")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("value","value15")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the post method status code whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the post method status code whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT) 
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key15")

    '''Test verifies the content of the post method whithout passing the "main_key"'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test25_verify_post_content_without_main_key(self):
        Api_Actions.put_method_getInfos("main_key15Bis", "value15Bis")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("value","value15Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"main_key") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the post method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the post method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: main_key", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False
        '''Return to initial state'''
        Api_Actions.delete_method("main_key15Bis")

    '''Test verifies the post method status code whithout passing the "value"'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test26_verify_post_status_code_without_value(self):
        Api_Actions.put_method_getInfos("main_key16", "value16")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("main_key","main_key16")
        if Verifications_pytest.verify_status_code(my_dict['status'],400,my_dict['content']) == True:
            allure.attach("Test OK",name = "Test case: verify the post method status code whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the post method status code whithout passing the 'value'",attachment_type=AttachmentType.TEXT)
            allure.attach("400", name = "Expected response",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT) 
            assert False            
        '''Return to initial state'''
        Api_Actions.delete_method("main_key16")

    '''Test verifies the content of the post method whithout passing the "value"'''
    @allure.severity(allure.severity_level.BLOCKER)
    def test27_verify_post_content_without_value(self):
        Api_Actions.put_method_getInfos("main_key16Bis", "value16Bis")
        my_dict = Api_Actions.post_method_getInfos_without_parameter("main_key","main_key16Bis")
        if Verifications_pytest.verify_body_response(my_dict['content'],"value") == True:
            allure.attach("Test OK",name = "Test case: verify the content of the post method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value", name = "Expected response details",attachment_type=AttachmentType.TEXT)
            assert True
        else:
            allure.attach("Test KO",name = "Test case: verify the content of the post method whithout passing the 'main_key'",attachment_type=AttachmentType.TEXT)
            allure.attach(str(my_dict['status']), name = "Response",attachment_type=AttachmentType.TEXT) 
            allure.attach(my_dict['content'], name = "Response details",attachment_type=AttachmentType.TEXT)
            allure.attach("Content must contains: value", name = "Expected response details",attachment_type=AttachmentType.TEXT) 
            assert False   
        '''Return to initial state'''
        Api_Actions.delete_method("main_key16Bis")