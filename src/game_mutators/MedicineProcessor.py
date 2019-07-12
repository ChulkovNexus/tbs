from src.models.person.buffs.DisabledByInjuryBuff import DisabledByInjuryBuff

max_blood_count = 200
default_blood_regeneration = 10
default_injury_regeneration = 3

blood_loss_threshold = 50
default_pain_threshold = 75

disabled_by_injuries_buff = DisabledByInjuryBuff()


def process_turn(user_game_models):
    for user_id, user_game_model in user_game_models.items():
        for char in user_game_model.persons:
            if char.health.blood_loss_level > 0:
                char.health.blood_count -= char.health.blood_loss_level
            elif char.health.blood_count < max_blood_count:
                char.health.blood_count += default_blood_regeneration * char.health.ill_resistance_effectivity / 100
            for injury in char.health.injuries:
                if injury.treatment_level > 0:
                    regen = default_injury_regeneration * injury.treatment_level
                    regen_value = regen * char.health.ill_resistance_effectivity / 100
                    injury.pain_level = 0 if injury.pain_level - regen_value < 0 else injury.pain_level - regen_value
                    injury.blood_loss_level = 0 if injury.blood_loss_level - regen_value < 0 else injury.pain_level - regen_value

            update_emergencies(user_game_model, char)
            char.health.refresh_injuries_affects()


def update_emergencies(user_game_model, char):
    if char.health.blood_count <= blood_loss_threshold:
        char.buffs.append(disabled_by_injuries_buff)
    elif char.health.pain_level >= default_pain_threshold:
        char.buffs.append(disabled_by_injuries_buff)
    elif char.health.pain_level < default_pain_threshold and char.health.blood_count > blood_loss_threshold and disabled_by_injuries_buff in char.buffs:
        char.buffs.remove(disabled_by_injuries_buff)

    if char.health.blood_count <= 0:
        user_game_model.persons.remove(char) #char_killed
    if char.health.pain_level > 100:
        user_game_model.persons.remove(char) #char_killed
