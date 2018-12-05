class Blog:
    def read(self):
        print('Reading the blog')

    def write(self):
        print('Writing the blog')



class BlogProxy:
    _is_user_authenticated = False
    def __init__(self, subject):
        self.subject = subject

    def __getattr__(self, attr):
        if self._is_user_authenticated:
            return getattr(self.subject, attr)
        else:
            raise Exception('User is not authorised')

if __name__ == "__main__":
    b = Blog()
    b.write()
    b.read()
    bp = BlogProxy(b)
    bp._is_user_authenticated = True
    bp.write()