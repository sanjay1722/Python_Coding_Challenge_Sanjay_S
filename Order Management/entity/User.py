class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    # Getters and setters for User class
    def get_user_id(self):
        return self.userId

    def set_user_id(self, userId):
        self.userId = userId

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def __str__(self):
        return f"User [ID={self.userId}, Username={self.username}, Role={self.role}]"
