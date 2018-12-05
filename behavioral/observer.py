class User:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.notifications = []

    def follow(self, user):
        user.followers.append(self)

    def share_update(self, update):
        msg = '{} has shared the following update: {}'.format(self.name, update)
        for user in self.followers:
            user.notify(msg)

    def notify(self, notification):
        self.notifications.append(notification)

    def get_notifications(self):
        for notification in self.notifications:
            print(notification)
    
    def __repr__(self):
        return self.name

