import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_dom_1a':
		return

	actor.addSkill('expertise_domestic_tailor_hypothesis_3')

	actor.addSkillMod('expertise_experimentation_increase_tailor', 3)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_dom_1a':
		return

	actor.removeSkill('expertise_domestic_tailor_hypothesis_3')

	actor.removeSkillMod('expertise_experimentation_increase_tailor', 3)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
