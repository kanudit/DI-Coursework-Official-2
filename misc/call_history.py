# xp ninja oop day 1
class Phone():
    def __init__(self,phone_number):
        self.call_history = []
        self.phone_number = phone_number
        self.outgoing_messages = []
        self.incoming_messages = []
    
    def call(self, other_phone):
        who_called = f'{other_phone.phone_number} called'
        self.call_history.append(who_called)
    
    def show_call_history(self):
        print(call_history)

    def send_message(self,other_phone):
        message_content = str(input('type msg here: '))
        message_info = {'to': other_phone.phone_number, 'from': self.phone_number, 'content': message_content}
        other_phone.incoming_messages.append(message_info)
        self.outgoing_messages.append(message_info)

    def show_outgoing_messages(self):
        print(f'Message \n {self.outgoing_messages}')
        pass

    def show_incoming_messages(self):
        print(f'Message \n {self.incoming_messages}')

        pass


    def show_messages_from (self,phone_number):
        for item in self.incoming_messages:
            if item['from'] == phone_number:
                print(f'message from {phone_number}: \n {item["content"]}')
                
        pass

me = Phone('053-596-5003')
taco = Phone('555-555-5555')
me.send_message(taco)
me.send_message(taco)
me.send_message(taco)

taco.show_incoming_messages()
taco.show_messages_from('053-596-5003')