class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


my_mails = []
command = input()
while not command == "Stop":
    s, r, c = command.split()
    email = Email(s, r, c)
    my_mails.append(email)
    command = input()

mail_inx = list(map(int, input().split(", ")))

for index in mail_inx:
    email = my_mails[index]
    email.sent()

for email in my_mails:
    print(email.get_info())
