import services
from autonomy.autonomy_modifier import AutonomyModifier
from game_effect_modifier.pie_menu_modifier import PieMenuModifier
from services import get_instance_manager
from sims4.resources import get_resource_key, Types
from tag import Tag
from typing import Dict, Tuple

def do_tag_injections():
    with Tag.make_mutable():
        Tag._add_new_enum_value("DIVINEASCENSION", 281894785)
        Tag._add_new_enum_value("CELESTIALBODY", 2953039053)


do_tag_injections()

def inject_to_objects(object_manager, *_, **__):
    try:
        affordance_manager = get_instance_manager(Types.INTERACTION)
        required_sa = affordance_manager.get(13328)
        interaction_to_add = affordance_manager.get(1549772142778404788)
        interaction_tuple = (interaction_to_add,)
        for obj in object_manager.types.values():
            if not hasattr(obj, "_super_affordances"):
                continue
            if required_sa in obj._super_affordances:
                obj._super_affordances = obj._super_affordances + interaction_tuple

    except Exception as e:
        try:
            raise e
        finally:
            e = None
            del e

    try:
        affordance_manager = get_instance_manager(Types.INTERACTION)
        required_sa = affordance_manager.get(13328)
        interaction_to_add = affordance_manager.get(9214555920345739465)
        interaction_tuple = (interaction_to_add,)
        for obj in object_manager.types.values():
            if not hasattr(obj, "_super_affordances"):
                continue
            if required_sa in obj._super_affordances:
                obj._super_affordances = obj._super_affordances + interaction_tuple

    except Exception as e:
        try:
            raise e
        finally:
            e = None
            del e


get_instance_manager(Types.OBJECT).add_on_load_complete(inject_to_objects)
buff_ids = (10094, 26171)
interaction_ids = (15847149625366149475, 15283619116768750678, 5894399786406898521)

def InjectProvidedAffordances(_):
    buff_manager = services.get_instance_manager(Types.BUFF)
    interaction_manager = services.get_instance_manager(Types.INTERACTION)
    loaded_interaction_set = set()
    for interaction in interaction_ids:
        loaded_interaction = interaction_manager.get(get_resource_key(interaction, Types.INTERACTION))
        if not loaded_interaction:
            continue
        else:
            loaded_interaction_set.add(loaded_interaction)

    for buff_id in buff_ids:
        loaded_buff = buff_manager.get(get_resource_key(buff_id, Types.BUFF))
        if not loaded_buff:
            continue
        else:
            game_effect_modifiers_slots = loaded_buff.game_effect_modifier._tuned_values
            game_effect_modifiers_values = game_effect_modifiers_slots._game_effect_modifiers
            for index, element in enumerate(game_effect_modifiers_values):
                if isinstance(element, PieMenuModifier):
                    pie_inclusion_slots = element.affordance_filter
                    pie_affordance_slots = pie_inclusion_slots.affordance_filter._tuned_values
                    pie_inclusion_slots = pie_affordance_slots.default_inclusion
                    pie_affordance_set = set(pie_inclusion_slots.include_affordances).union(loaded_interaction_set)
                    pie_inclusion_slots = pie_inclusion_slots.clone_with_overrides(include_affordances=(tuple(pie_affordance_set)))
                    pie_affordance_slots = pie_affordance_slots.clone_with_overrides(default_inclusion=pie_inclusion_slots)
                    game_effect_modifiers_values[index].affordance_filter.affordance_filter._tuned_values = pie_affordance_slots
                    game_effect_modifiers_slots = game_effect_modifiers_slots.clone_with_overrides(_game_effect_modifiers=game_effect_modifiers_values)
                    loaded_buff.game_effect_modifier._tuned_values = game_effect_modifiers_slots
                if isinstance(element, AutonomyModifier):
                    provided_affordance_slots = element._provided_affordance_compatibility._tuned_values
                    default_inclusion_slots = provided_affordance_slots.default_inclusion
                    include_affordances_set = set(default_inclusion_slots.include_affordances).union(loaded_interaction_set)
                    default_inclusion_slots = default_inclusion_slots.clone_with_overrides(include_affordances=(tuple(include_affordances_set)))
                    provided_affordance_slots = provided_affordance_slots.clone_with_overrides(default_inclusion=default_inclusion_slots)
                    game_effect_modifiers_values[index]._provided_affordance_compatibility._tuned_values = provided_affordance_slots
                    game_effect_modifiers_slots = game_effect_modifiers_slots.clone_with_overrides(_game_effect_modifiers=game_effect_modifiers_values)
                    loaded_buff.game_effect_modifier._tuned_values = game_effect_modifiers_slots


services.get_instance_manager(Types.INTERACTION).add_on_load_complete(InjectProvidedAffordances)
data = dict()
data[12800476684265835490] = (40870, 77372)

def _add_test_sets(affordance_manager, snippet_manager, data_mapping: Dict[(int, Tuple[int])]):
    for test_set_id, affordance_ids in data_mapping.items():
        test_set = snippet_manager.get(test_set_id)
        if not test_set:
            continue
        else:
            for affordance_id in affordance_ids:
                affordance = affordance_manager.get(affordance_id)
                if not affordance:
                    continue
                else:
                    affordance.add_additional_test(test_set)


def _inject_test_sets(snippet_manager):
    affordance_manager = services.get_instance_manager(Types.INTERACTION)
    try:
        _add_test_sets(affordance_manager, snippet_manager, data)
    except BaseException as ex:
        try:
            pass
        finally:
            ex = None
            del ex


snippet_manager = services.get_instance_manager(Types.SNIPPET)
snippet_manager.add_on_load_complete(_inject_test_sets)

# okay decompiling extracted/DivineAscensionMod.pyc
