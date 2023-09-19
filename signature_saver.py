import json
# Class responsible for saving the signature to a JSON file
class SignatureSaver:
    def __init__(self, signature_lines, output_file):
        self.__signature_lines = signature_lines
        self.__output_file = output_file

    def save_signature_to_json(self):
        signature = list(self.__signature_lines)
        with open(self.__output_file, 'w') as json_file:
            json.dump(signature, json_file, indent=4)
        print("Signature lines written to", self.__output_file)

   