from src.models.items.buildings.Building import Sawmill
from src.models.tasks.CreateBuildingMaterials import CreateBuildingMaterials
from src.models.tasks.CreateBuildingTask import CreateBuilding

task_not_needed_buildings = [CreateBuilding(Sawmill())]


class BuildingsDependedTasksManager:

    def __init__(self):
        self._task_list = list()

    def get_tasks(self, buildings):
        if not self._task_list:
            self._task_list = task_not_needed_buildings
            for building in buildings:
                tasks = building.get_allowed_tasks()
                self._task_list.extend([x for x in tasks if x not in self._task_list])
                for material, count in building.allow_to_create_materials.items():
                    self._task_list.append(CreateBuildingMaterials({material: count}, [building]))
        return self._task_list

    def clear_cache(self):
        self._task_list.clear()
