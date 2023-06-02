from typing import Any
from se_sim.utils.log_loggers import MODEL_LOG, PLUGIN_LOG


class GenObject:
    """
    The base object for the code generator
    """

    def __init__(self) -> None:
        MODEL_LOG.debug("create code generator 'base'")

    def gen_output_pre(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output_pre")  # pragma: no cover

    def gen_output_post(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output_post")  # pragma: no cover

    def gen_output(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("GenObject.gen_output")

    def go_deeper(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("GenObject.go_deeper")

    def generate(self, env: dict[str, Any], level: int = 0) -> None:
        PLUGIN_LOG.debug("GenObject.generate")
        self.gen_output_pre(env, level)
        self.gen_output(env, level)
        self.go_deeper(env, level + 1)
        self.gen_output_post(env, level)
