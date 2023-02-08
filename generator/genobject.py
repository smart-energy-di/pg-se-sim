from utils.log_loggers import MODEL_LOG, PLUGIN_LOG


class GenObject:
    """
    The base object for the code generator
    """

    def __init__(self):
        MODEL_LOG.debug(f"create code generator 'base'")

    def gen_output_pre(self, level):
        PLUGIN_LOG.debug("GenObject.gen_output_pre")

    def gen_output_post(self, level):
        PLUGIN_LOG.debug("GenObject.gen_output_post")

    def gen_output(self, level):
        PLUGIN_LOG.debug("GenObject.gen_output")

    def go_deeper(self, level):
        PLUGIN_LOG.debug("GenObject.go_deeper")

    def generate(self, level=0):
        PLUGIN_LOG.debug("GenObject.generate")
        self.gen_output_pre(level)
        self.gen_output(level)
        self.go_deeper(level + 1)
        self.gen_output_post(level)
