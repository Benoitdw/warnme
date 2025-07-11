from dotenv import load_dotenv
import os 
import asyncio
from warnme.message import Message
from pathlib import Path


class Messager():
    """
    Parent class, useless for now but can be used in the future (more subclass, delay message, avoid night, ...)
    """
    def __init__(self ) -> None:
        load_dotenv(dotenv_path=Path.home().joinpath('.config', '.warnme'))

    def get_envar(self, envar) -> None:
        try:
            return os.environ[envar]
        except KeyError:
            raise KeyError(f"Environment variable '{envar}' not found. Please set it in the .env file.")
        
    def send(self, message : Message | str ) -> None:
        formated_message = self.format_message(message)
        asyncio.run(self._send(formated_message))

    def format_message(self, message:Message  | str ) : 
        raise NotImplementedError("This method should be overridden by subclasses")

        
    def _send(self, message) -> None:
        raise NotImplementedError("This method should be overridden by subclasses")

