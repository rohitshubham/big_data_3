class ClientHistory:    

    def __init__(self, user_id, location, date_time):
        self.user_id = user_id
        self.location = location
        self.date_time = date_time

    def get_last_location(self):
        return self.location

    def get_last_time(self):
        return self.date_time

    def get_user_id(self):
        return self.user_id

    def update_details(self, location, date_time):
        self.location = location 
        self.date_time = date_time  


class Client():

    person_list = []

    @staticmethod
    def add_client(user_id, location, date_time):
        client = ClientHistory(user_id, location, date_time)
        Client.person_list.append(client)

    @staticmethod
    def update_client(user_id, location, date_time):
        for person in Client.person_list:
            if person.get_user_id() == user_id:
                person.update_details(location, date_time)
                break
    
    @staticmethod
    def get_all_clients():
        return Client.person_list
    
    @staticmethod
    def client_exists(user_id):
        for person in Client.person_list:
            if person.get_user_id() == user_id:
                return True
        return False

