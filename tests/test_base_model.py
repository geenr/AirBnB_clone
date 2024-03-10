#!/usr/bin/env python3
"""
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_initialize(self):
        """
        checks whether the created_at has been initialized
        """

        base_model = BaseModel()

        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
    def test_to_dict(self):
        """
        tests whether a dictionary was formed.
        acertains whether a key and a value was formed.
        """
        base_model = BaseModel()
        dict_model = base_model.to_dict()
        self.assertIsInstance(dict_model, dict)
        
        self.assertEqual(dict_model['__class__'], 'BaseModel')
        self.assertEqual(dict_model['id'], base_model.id)
        self.assertEqual(dict_model['updated_at'], base_model.updated_at.isoformat())
        self.assertEqual(dict_model['created_at'], base_model.created_at.isoformat())
    def test_uuid_instance(self):
        """
        tests whether each instance has been allocated a UID.
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
    def test_uuid_str(self):
        """
        tests whether the uuid is a string.
        """
        base_model = BaseModel()
        self.assertTrue(str(base_model).startswith('[BaseModel]'))
        self.assertIn(base_model.id, str(base_model))
        self.assertIn(str(base_model.__dict__), str(base_model))
    def test_save(self):
        """
        tests whether updated_at has the current time value.
        """
        base_model = BaseModel()
        first_updated_at = base_model.updated_at
        now_updated_at = base_model.save()
        self.assertNotEqual(first_updated_at, now_updated_at)

if __name__ == '__main__':
    unittest.main
