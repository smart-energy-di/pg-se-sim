from se_sim.generator.genobject import GenObject
from se_sim.utils.log_loggers import PLUGIN_LOG


class GenParticipant(GenObject):
    """
    The participant object for the code generator
    """

    def __init__(self) -> None:
        super().__init__()
        PLUGIN_LOG.debug("create code generator 'participant'")

    def gen_output_pre(self, level: int) -> None:
        PLUGIN_LOG.debug("GenParticipant.gen_output_pre")
        print(' ' * (level * 4) + "(participant:", end='')

    def gen_output_post(self, level: int) -> None:
        PLUGIN_LOG.debug("GenParticipant.gen_output_post")
        print(")")

    def gen_output(self, level: int) -> None:
        PLUGIN_LOG.debug("GenParticipant.gen_output")
        out_title = getattr(self, 'en_title', None)
        print(f"'{out_title}'", end='')
