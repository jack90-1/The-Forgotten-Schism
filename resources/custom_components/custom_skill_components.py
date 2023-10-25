from __future__ import annotations

from app.data.database.components import ComponentType
from app.data.database.skill_components import SkillComponent, SkillTags
from app.engine import (action, banner, combat_calcs, engine, equations,
                        image_mods, item_funcs, item_system, skill_system,
                        target_system)
from app.utilities import (static_random)
from app.engine.game_state import game
from app.engine.objects.unit import UnitObject
from app.engine.combat import playback as pb
import logging

class EventAfterCombat(SkillComponent):
    nid = 'event_after_combat'
    desc = 'Calls event after any combat'
    tag = SkillTags.ADVANCED

    expose = ComponentType.Event
    value = ''

    def end_combat(self, playback, unit: UnitObject, item, target: UnitObject, mode):
        game.events.trigger_specific_event(self.value, unit, target, unit.position, {'item': item, 'mode': mode})
