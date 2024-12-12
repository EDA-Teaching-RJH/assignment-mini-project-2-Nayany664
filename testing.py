
from contacts import correct_format #get the class correct_format from the main file
import unittest #for correct format isolation
from contacts import correct_format #from other file

class Testing(unittest.TestCase):

    def isolation(info):
        info.format = correct_format(file_path="test_contacts.json")  #use a test file for isolation

    def testing_add_contact_details(info): #adding contact
        info.format.add_contact("John Doe", "01234567890", "john@example.com", "123 Street")
        info.assertEqual(len(info.format.contacts), 1) #1 contact is added

    def testing_invalid_email(info): #testing email
        with info.assertRaises(ValueError):
            info.format.add_contact("John Doe", "01234567890", "invalid-email", "123 Street")

    def testing_remove_contact(info): #testing removing contact
        info.format.add_contact("John Doe", "01234567890", "john@example.com", "123 Street")
        info.format.remove_contact("John Doe")
        info.assertEqual(len(info.format.contacts), 0) #1 less

if __name__ == "__main__":
    unittest.main()
