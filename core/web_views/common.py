class TestMail(Resource):

    def post(self):
        msg = Message(
            'Hello',
            sender='contatoahadi@gmail.com',
            recipients=['flavioribeiro342@gmail.com']
        )
        msg.html = "<b>testing</b>"
        mail.send(msg)
        return {}