#!/usr/bin/python3
"""
Tests for Base_Model Class
"""
from genericpath import exists
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel
    """
    @classmethod
    def setUpClass(self):
        """
        Sets up objects
        """
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        my_dict = self.bm2.to_dict()
        self.bm3 = BaseModel(**my_dict)

    @classmethod
    def tearDownClass(self):
        """
        Tears down objects.
        """
        del self.bm1
        del self.bm2
        storage.save()


    def test_init(self):
        """
        Test inits
        """
        self.assertTrue(self.bm1.id, exists)
        self.assertTrue(self.bm2.created_at, exists)
        self.assertTrue(self.bm3.updated_at, exists)

    def test_str(self):
        """
        Tests __str__ method
        """
        print_bm = "[{}]({}) {}".format\
            (self.bm3.__class__.__name__, \
                self.bm3.id, self.bm3.__dict__)
        self.assertEqual(self.bm3.__str__(), print_bm)

    def test_save(self):
        """
        Tests save method
        """
        self.bm1.save()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_to_dict(self):
        """
        Tests to_dict method
        """
        bm1_dict = self.bm1.to_dict()
        self.assertEqual(bm1_dict['__class__'], 'BaseModel')
        self.assertEqual(bm1_dict['created_at'],
                         self.bm1.created_at.isoformat())
        self.assertEqual(bm1_dict['updated_at'],
                         self.bm1.updated_at.isoformat())
        self.assertEqual(bm1_dict['id'], self.bm1.id)
        # test looking for attr that doesn't exist
        with self.assertRaises(AttributeError):
            getattr(self.bm1, 'NonExistentKey')
        # set attr and test it
        self.bm1.Job = "Code Monkey"
        self.assertTrue(self.bm1.Job, exists)

if __name__ == "__main__":
    unittest.main()