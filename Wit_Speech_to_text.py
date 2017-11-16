from wit import Wit
from Wit_Credentials import *


class Speech_to_text:
    def convert(this):
        client=Wit(Wit_token);

        resp = None
        with open('output.wav', 'rb') as f:
            resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
        #print('Yay, got Wit.ai response: ' + str(resp))
        return resp;
