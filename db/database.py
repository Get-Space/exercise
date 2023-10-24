class MockDatabase:
    def __init__(self):
        self._users = {"test": {"username": "test"}}
        self._questions = {
            "1": {"question": "What is your favorite color?", "weight": 1000},
            "2": {"question": "What is your favorite animal?", "weight": 1000},
            "3": {"question": "What is your favorite food?", "weight": 100},
        }
        self._responses = {}

    def get_user(self, username):
        return self._users.get(username)

    def save_user(self, username, value):
        self._users[username] = value

    def delete_user(self, username):
        del self._users[username]

    def get_question(self, id):
        return self._questions.get(id)

    def get_all_questions(self):
        return self._questions

    def save_question(self, id, question):
        self._questions[id] = question

    def delete_question(self, id):
        del self._questions[id]

    def get_response(self, id):
        return self._responses.get(id)

    def get_responses_for_user(self, username):
        return [r for r in self._responses if r["user"] == username]

    def save_response(self, id, question):
        self._responses[id] = question

    def delete_response(self, id):
        del self._responses[id]
