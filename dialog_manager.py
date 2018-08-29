

class DialogManager:

    speeches = []
    first_speech = None

    @classmethod
    def set_speeches(cls, speeches, first_speech):
        cls.speeches = speeches
        cls.first_speech = first_speech

    @classmethod
    def get_speech(cls, speech_id):
        speech = next(i for i in cls.speeches if str(i['id']) == str(speech_id))
        return speech

    @classmethod
    def get_first_speech(cls):
        return cls.get_speech(cls.first_speech)
