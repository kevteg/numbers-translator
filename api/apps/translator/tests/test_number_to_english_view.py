from django.test import TestCase
from django.test import Client
from rest_framework import status


class TestNumberToEnglishView(TestCase):
    number = 1289
    endpoint = "/num_to_english"
    number_text = "one thousand two hundred eighty nine"
    client = Client()

    def __verify_response(self, response):
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["status"], "ok")
        self.assertEqual(json_response["num_in_english"], self.number_text)

    def test_get_view(self): 
        """Successful get request"""
        response = self.client.get(self.endpoint, {"number": self.number})
        self.__verify_response(response)

    def test_post_view(self): 
        """Successful post request"""
        response = self.client.post(self.endpoint, {"number": self.number})
        self.__verify_response(response)

    def test_wrong_field(self): 
        """Number is not being sent"""
        response = self.client.get(self.endpoint, {"not_number": self.number})
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json_response["status"], "error")
        self.assertEqual(json_response["num_in_english"], None)
        self.assertIn("field is required", json_response["error_description"])

    def test_wrong_number(self): 
        """Number field is not a valid integer"""
        response = self.client.get(self.endpoint, {"number": "not a number"})
        json_response = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json_response["status"], "error")
        self.assertEqual(json_response["num_in_english"], None)
        self.assertIn("valid integer is required", json_response["error_description"])

    def test_put_view(self): 
        """Method not implemented"""
        response = self.client.put(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_view(self): 
        """Method not implemented"""
        response = self.client.delete(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_view(self): 
        """Method not implemented"""
        response = self.client.delete(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
