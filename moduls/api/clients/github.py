import requests

class GitHub():

    # def get_user_defunkt(self):
    #     r = requests.get('https://api.github.com/users/defunkt')
    #     body = r.json()
    #     return body
    
    # def get_not_exist_user(self):
    #     r = requests.get('https://api.github.com/users/s_butenko')
    #     body = r.json()
    #     return body

# optimising

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        return body
    
    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories',
                      params= {'q': name})
        body = r.json()
        return body
    
    def search_topic(self, topic):
        r = requests.get('https://api.github.com/search/topics',
                      params= {'q': topic})
        body = r.json()
        return body