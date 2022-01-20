


class CustomUser:
    def __init__(self, firstname, lastname, email, password, age, gender, phone, secret_key):
        if isinstance(firstname, str):
            self.first = firstname
        else:
            raise Exception('First name is string')
        if isinstance(lastname, str):
            self.last = lastname
        else:
            raise Exception('Last name is string')
        if isinstance(email, str):
            self.email = email
            raise Exception('Email is string')
        if isinstance(password, str):
            self.pswrd = password
            raise Exception('Password is string')
        if isinstance(age, str):
            self.age = age
            raise ValueError('Age is string')
        if isinstance(gender, str):
            self.gen = gender
            raise ValueError('Gender is string')
        if isinstance(phone, str):
            self.phone = phone
            raise ValueError('Phone is string')
        if isinstance(secret_key, str):
            self.key = secret_key
            raise ValueError('Key is string')


    def __str__(self):
        return f'First name: {self.first}\n' \
               f'Last name: {self.last}\n' \
               f'Email: {self.email}\n' \
               f'Password: {self.pswrd}\n' \
               f'Age: {self.age}\n' \
               f'Gender: {self.age}\n' \
               f'Phone: {self.phone}\n' \
               f'Key: {self.key}\n' \

user_1 = CustomUser(firstname='kirill', lastname='oplachkin', email='zoj',password='121', age=17, gender='male', phone='0508111667', secret_key='228')
print(user_1)


class Admin:
    def __init__(self, firstname, lastname, email, password, age, gender, phone, secret_key, vip_client):
        super().__init__(firstname, lastname, email, password, age, gender, phone, secret_key)

    def __str__(self):
        return super(, self)





