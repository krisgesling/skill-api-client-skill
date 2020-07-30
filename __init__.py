from mycroft import MycroftSkill, intent_file_handler


class SkillApiClient(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('client.api.skill.intent')
    def handle_client_api_skill(self, message):
        self.speak_dialog('client.api.skill')


def create_skill():
    return SkillApiClient()

