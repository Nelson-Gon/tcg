from openai import Completion, Image
import os
import webbrowser


class TCG(object):
    def __init__(self) -> None:
        """
        Initiates a TCG object by assigning an api key if it exists and redirecting to signup page otherwise. 
        """
        try:
            self.api_key = os.environ["openai_key"]
        except KeyError:
            print(
                "No api key with the name, openai_key found in environment, taking you to signup page")
            webbrowser.open("https://beta.openai.com", new=1)

    # TODO: make this less duplicative
    def correct_english(self, text_):
        """
        Uses a GPT model (Text Davinci 003) to correct the grammar of a sentence 

        Args:
            text_ (str): A sentence or sentences, period separated, whose grammar should be corrected. 

        Returns:
            str: Grammatically correct sentence. 
        """
        return Completion.create(
            api_key=self.api_key,
            model="text-davinci-003",
            # TODO: text limit assertions
            prompt=f"Correct this to standard English: {text_}",
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )["choices"][0]["text"].replace("\n", "")

    def translate(self, text_, target_language="Czech"):
        """
        Translates given text to the target language. Currently only supports English to other translation. 

        Args:
            text_ (str): Text to translate. 
            target_language (str, optional): Language to translate to. Defaults to "Czech".

        Returns:
            str: Translation, as requested. 
        """
        return Completion.create(
            api_key=self.api_key,
            model="text-davinci-003",
            # TODO: text limit assertions
            prompt=f"Translate this to {target_language}: {text_}",
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )["choices"][0]["text"].replace("\n", "")
