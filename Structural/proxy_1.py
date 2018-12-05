class SubjectInterface:
    def request(self):
        pass

class Subject(SubjectInterface):
    def request(self):
        print('Subject is handling the request')

class Proxy(SubjectInterface):
    def __init__(self, subject):
        self.subject = subject

    def request(self):
        print('Proxy is doing something with the request first')
        self.subject.request()


if __name__ == "__main__":
    import pdb; pdb.set_trace()