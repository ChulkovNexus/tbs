from src.models.items.buildings.BuildingPerfabs import no_requerements_buildings
from src.models.tasks.CreateBuildingMaterials import CreateBuildingMaterials
from src.models.tasks.CreateBuildingTask import CreateBuilding


class NotAllowedBuildingsStack(list):

    def __init__(self, buildings_task_manager):
        super().__init__()
        self.buildings_task_manager = buildings_task_manager

    def append(self, other, n=1):
        list.append(self, other)
        self.buildings_task_manager.update_allowed_buildings_tasks_cashe()

    def __delitem__(self, **kwargs):
        list.__getitem__(self, **kwargs)
        self.buildings_task_manager.update_allowed_buildings_tasks_cashe()


class NotAllowedTasksStack(list):

    def __init__(self, buildings_task_manager):
        super().__init__()
        self.buildings_task_manager = buildings_task_manager

    def append(self, other, n=1):
        list.append(self, other)
        self.buildings_task_manager.update_allowed_tasks_cashe()

    def __delitem__(self, **kwargs):
        list.__getitem__(self, **kwargs)
        self.buildings_task_manager.update_allowed_tasks_cashe()


def check_necessary_buildings_condition(new_building, already_created_buildings):
    return all(x in already_created_buildings for x in new_building.necessary_buildings)


class BuildingsDependedTasksManager:

    def __init__(self):
        self._task_list = list()
        self.not_allowed_buildings = NotAllowedBuildingsStack(self)
        self.not_allowed_tasks = NotAllowedTasksStack(self)
        self.task_not_needed_buildings = []
        for building in no_requerements_buildings:
            for resource in building.building_resources_needed:
                self.task_not_needed_buildings.append(CreateBuilding(building, resource, self.not_allowed_buildings))

    def get_tasks(self, already_created_buildings, person):
        if not self._task_list:

            self._task_list.extend([x for x in self.task_not_needed_buildings if x.result_building not in self.not_allowed_buildings])
            for building in already_created_buildings:

                # allow execute special tasks
                tasks = building.get_allowed_tasks(self.not_allowed_tasks)
                self._task_list.extend([x for x in tasks if x not in self._task_list])

                # allow create building
                new_buildings = [x for x in building.allow_to_create_buildings if x not in self.not_allowed_buildings]
                new_buildings_tasks = []
                for new_building in new_buildings:
                    if new_building not in already_created_buildings and check_necessary_buildings_condition(new_building, already_created_buildings):
                        for resource in new_building.building_resources_needed:
                            new_buildings_tasks.append(CreateBuilding(new_building, resource, self.not_allowed_buildings))
                self._task_list.extend(new_buildings_tasks)

                #allow create materials
                for material, count in building.allow_to_create_materials.items():
                    self._task_list.append(CreateBuildingMaterials({material: count}, [building]))

        return self._task_list

    def update_allowed_buildings_tasks_cashe(self):
        self._task_list = [x for x in self._task_list if not isinstance(x, CreateBuilding) or (isinstance(x, CreateBuilding) and x not in self.not_allowed_buildings)]

    def update_allowed_tasks_cashe(self):
        self._task_list = [x for x in self._task_list if x not in self.not_allowed_tasks]

    def clear_cache(self):
        self._task_list.clear()
