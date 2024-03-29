import json
from typing import Any

from se_sim.generator.genobject import GenObject
from se_sim.model.participant import Participant
from se_sim.simulation.create_objects import createSimObjects
from se_sim.utils import cli_utils
from se_sim.utils.log_loggers import MODEL_LOG, PLUGIN_LOG


class Simulation(list[Participant], GenObject):
    def __init__(self) -> None:
        pass

    def create_objects(self) -> None:
        createSimObjects(self)

    def create_from_json(self, filename: str) -> None:
        f = open(filename)
        data = json.load(f)
        f.close()
        for obj in data:
            sim_class = cli_utils.locate(obj['sim_class'])
            self.append(sim_class(**obj['params']))

    def debug_general_statistic(self) -> None:
        MODEL_LOG.info("Number of objects %3d", len(self))  # pragma: no cover

    def debug_roles(self) -> None:  # pragma: no cover
        results = {}
        for obj in self:
            obj_role = obj.el_role
            if obj_role not in results:
                results[obj_role] = 0
            results[obj_role] += 1
        for (role, cnt) in results.items():
            MODEL_LOG.info("Role: '%s': %3d", role, cnt)

    def get_obj_by_en_title(self, search_title: str) -> object:
        for obj in self:
            if obj.en_title == search_title:
                return obj
        return None

    def gen_output_pre(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("Simulation.gen_output_pre")
        print(f"{' ' * (level * 4)}(Simulation:")

    def gen_output_post(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("Simulation.gen_output_post")
        print(")")

    def go_deeper(self, env: dict[str, Any], level: int) -> None:
        PLUGIN_LOG.debug("Simulation.go_deeper")
        for obj in self:
            obj.generate(env, level + 1)
