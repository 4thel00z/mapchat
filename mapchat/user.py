import uuid

class User: 
    def __init__(self, id_, username=''): 
        self.id=id_
        self.username=username

def generate_user():
        uid = str(uuid.uuid4())
        user = User(uid)
        return user   