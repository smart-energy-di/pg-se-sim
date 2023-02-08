from generator.genobject import GenObject
from simulation.create_objects import createSimObjects
from utils.log_loggers import MODEL_LOG, PLUGIN_LOG


class Simulation(list, GenObject):
    def __init__(self):
        pass

    def create_objects(self):
        createSimObjects(self)

    def debug_general_statistic(self):
        MODEL_LOG.info("Number of objects %3d", len(self))

    def debug_roles(self):
        results = {}
        for obj in self:
            obj_role = obj.el_role
            if obj_role not in results:
                results[obj_role] = 0
            results[obj_role] += 1
        for (role, cnt) in results.items():
            MODEL_LOG.info("Role: '%s': %3d", role, cnt)

    def get_obj_by_en_title(self, search_title):
        for obj in self:
            if obj.en_title == search_title:
                return obj
        return None


    def gen_output_pre(self, level):
        PLUGIN_LOG.debug("Simulation.gen_output_pre")
        print(f"{' ' * (level * 4)}(Simulation:")

    def gen_output_post(self, level):
        PLUGIN_LOG.debug("Simulation.gen_output_post")
        print(f")")

    def go_deeper(self, level):
        PLUGIN_LOG.debug("Simulation.go_deeper")
        for obj in self:
            obj.generate(level + 1)
