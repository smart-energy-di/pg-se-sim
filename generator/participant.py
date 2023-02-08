from generator.genobject import GenObject
from utils.log_loggers import PLUGIN_LOG


class GenParticipant(GenObject):
    """
    The participant object for the code generator
    """

    def __init__(self):
        super().__init__()
        PLUGIN_LOG.debug(f"create code generator 'participant'")

    def gen_output_pre(self, level):
        PLUGIN_LOG.debug("GenParticipant.gen_output_pre")
        print(f"{' ' * (level * 4)}(participant:", end='')

    def gen_output_post(self, level):
        PLUGIN_LOG.debug("GenParticipant.gen_output_post")
        print(f")")

    def gen_output(self, level):
        PLUGIN_LOG.debug("GenParticipant.gen_output")
        print(f"'{self.en_title}'", end='')
