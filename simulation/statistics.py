from utils.log_loggers import MODEL_LOG


def debug_general_statistic(obj_list):
    MODEL_LOG.info("Number of objects %3d", len(obj_list))


def debug_roles(obj_list):
    results = {}
    for obj in obj_list:
        obj_role = obj.el_role
        if obj_role not in results:
            results[obj_role] = 0
        results[obj_role] += 1
    for (role, cnt) in results.items():
        MODEL_LOG.info("Role: '%s': %3d", role, cnt)
