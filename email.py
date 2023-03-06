usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
: '''


#An Email Simulation
#Email class

class Email:
    #Initialisation
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

#Inbox class


class Inbox:

    #initialising an empty list of emails
    def __init__(self):
        self.inbox_list = []
    #Creates a new email instance and adds the email

    def add_email(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        an_email = Email(from_address, subject_line, email_contents)
        self.inbox_list.append(an_email)
        return self.inbox_list

    messages_list = []
    #Stores index and subject lines from a specific sender in a list

    def list_messages_from_sender(self, sender_address):
        self.sender_address = sender_address
        count = 0
        messages = ""
        for email in self.inbox_list:
            if self.sender_address == email.from_address:
                messages += f"{count}  {email.subject_line}\n"
                self.messages_list.append(email.subject_line)
                count += 1
                pass
        return messages
    #fetches email by matching the index and subject line in the inbox

    def get_email(self, sender_address, index):
        self.messages_list = []
        self.sender_address = sender_address
        self.index = index
        self.list_messages_from_sender(sender_address)
        target_subject = self.messages_list[index]
        for email in self.inbox_list:
            if email.subject_line == target_subject:
                return email
    #Marks an email as spam using get_email method

    def mark_as_spam(self, sender_address, index):
        mail = self.get_email(sender_address, index)
        Email.mark_as_spam(mail)
    #Retrieves unread emails by using the mark_as_read method

    def get_unread_emails(self):
        unread_emails = ""
        for email in self.inbox_list:
            if email.has_been_read == False:
                unread_emails += f"{email.subject_line}\n"
        return unread_emails
    #Retrieves spam emails by using the mark_as_spam method

    def get_spam_emails(self):
        spam_emails = ""
        for email in self.inbox_list:
            if email.is_spam == True:
                spam_emails += f"{email.subject_line}\n"
        return spam_emails
    #Deletes email using the get_email method and removing it

    def delete(self, sender_address, index):
        email = self.get_email(sender_address, index)
        self.inbox_list.remove(email)


user_choice = ""
inbox = Inbox()

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox
        inbox.add_email(sender_address, subject_line, contents)
        for email in inbox.inbox_list:
            print(f"{email.from_address} {email.subject_line} {email.email_contents}")
        # Print a success message
        print("Email has been added to inbox.")
        pass

    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        # Now list all emails from this sender
        #inbox.list_messages_from_sender(sender_address)
        inbox.list_messages_from_sender(sender_address)
        print(inbox.list_messages_from_sender(sender_address))
        pass

    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        print(inbox.list_messages_from_sender(sender_address))
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))
        # Step 4: display the email
        mail = inbox.get_email(sender_address, email_index)
        Email.mark_as_read(mail)
        print(f"{mail.from_address} {mail.subject_line} {mail.email_contents}")
        pass

    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        print(inbox.list_messages_from_sender(sender_address))
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))

        # Step 4: mark the email as spam
        inbox.mark_as_spam(sender_address, email_index)
        # Step 5: print a success message
        print("Email has been marked as spam")
        pass

    elif user_choice == "gu":
        # List all unread emails
        print(inbox.get_unread_emails())
        pass

    elif user_choice == "gs":
        # List all spam emails
        print(inbox.get_spam_emails())
        pass

    elif user_choice == "e":
        print("Goodbye")
        break

    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        print(inbox.list_messages_from_sender(sender_address))
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        inbox.delete(sender_address, email_index)
        # prints messages still left in inbox from sender
        print(inbox.list_messages_from_sender(sender_address))
        # Step 5: print a success message
        print("Email has been deleted")
        pass

    else:
        print("Oops - incorrect input")
