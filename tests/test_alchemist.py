import os
import sys
import unittest

# Add the src directory to the Python path so we can import alchemist.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from alchemist import load_database, recommend_tablets, get_tablet_details

class TestAlchemist(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = load_database()
    
    def test_recommend_tablets_valid(self):
        # For a known condition, the list should not be empty.
        tablets = recommend_tablets("headache", self.database)
        self.assertIsInstance(tablets, list)
        self.assertGreater(len(tablets), 0)
    
    def test_recommend_tablets_invalid(self):
        # For an unknown condition, the function should return an empty list.
        tablets = recommend_tablets("unknown", self.database)
        self.assertEqual(tablets, [])
    
    def test_get_tablet_details_found(self):
        tablets = recommend_tablets("headache", self.database)
        tablet = get_tablet_details("Ibuprofen", tablets)
        self.assertIsNotNone(tablet)
        self.assertEqual(tablet["name"], "Ibuprofen")
    
    def test_get_tablet_details_not_found(self):
        tablets = recommend_tablets("headache", self.database)
        tablet = get_tablet_details("NonExistent", tablets)
        self.assertIsNone(tablet)

if __name__ == '__main__':
    unittest.main()
