
from contacts import correct_format #get the class correct_format from the main file

class Testing() :

    def testing_add_contact(info): #adding contact
        info.format.add_contact("John Doe", "1234567890", "john@example.com", "123 Street")
        info.assertEqual(len(info.format.contacts), 1) #1 contact is added

    def testing_invalid_email(info): #testing email
        with info.assertRaises(ValueError):
            info.format.add_contact("John Doe", "1234567890", "invalid-email", "123 Street")

    def testing_remove_contact(info): #testing removing contact
        info.format.add_contact("John Doe", "1234567890", "john@example.com", "123 Street")
        info.format.remove_contact("John Doe")
        info.assertEqual(len(info.format.contacts), 0) #1 less
