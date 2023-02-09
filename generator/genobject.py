from utils.log_loggers import MODEL_LOG, PLUGIN_LOG


class GenObject:
    """
    The base object for the code generator
    """

    def __init__(self) -> None:
        MODEL_LOG.debug("create code generator 'base'")

    def gen_output_pre(self, level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output_pre")  # pragma: no cover

    def gen_output_post(self, level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output_post")  # pragma: no cover

    def gen_output(self, level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output")

    def go_deeper(self, level: int) -> None:
        PLUGIN_LOG.debug("GenObject.go_deeper")

    def generate(self, level: int = 0) -> None:
        PLUGIN_LOG.debug("GenObject.generate")
        self.gen_output_pre(level)
        self.gen_output(level)
        self.go_deeper(level + 1)
        self.gen_output_post(level)
