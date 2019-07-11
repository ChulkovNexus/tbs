from src.models.person.buffs.Buff import Buff


class DisabledByInjuryBuff(Buff):

    def __init__(self):
        super().__init__()
        self.duration = 99999