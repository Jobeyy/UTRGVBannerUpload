import unittest
from unittest.mock import patch
from helper import *
import csv
import customtkinter


class TestDataValidity(unittest.TestCase):
    def setup(self):
        self.root = customtkinter.CTk()

    def tearDown(self):
        self.root.destroy()

    @patch('customtkinter.filedialog.askopenfilename', return_value='testzips.csv')
    def test_zipcode(self,mock_askopenfilename):
        with open(mock_askopenfilename, "r") as csvfile:
            reader = csv.reader(csvfile)
            dataset = list(reader)
            

        pass

    def test_address(self):

        pass
    
    def test_city_state(self):

        pass


