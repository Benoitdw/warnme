from dotenv import load_dotenv
import os 


class Messager():
    """
    Parent class, useless for now but can be used in the future (more subclass, delay message, avoid night, ...)
    """
    def __init__(self ) -> None:
        load_dotenv()

    def get_envar(self, envar) -> None:
        try:
            return os.environ[envar]
        except KeyError:
            raise KeyError(f"Environment variable '{envar}' not found. Please set it in the .env file.")
        
    def send(self, message:str) -> None:
        raise NotImplementedError("This method should be overridden by subclasses")
