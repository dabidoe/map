#!/usr/bin/env python3
import re

# Read the file
with open('BattleOfTrenton.html', 'r') as f:
    content = f.read()

# Fix 1: Remove COMBAT tab manual add buttons - replace the whole section
old_buttons = r'<div style="margin-bottom: 1\.5rem;">[\s\S]*?<button onclick="rollAllCombatInitiative\(\)"'
new_buttons = '''<div style="margin-bottom: 1.5rem;">
                        <button onclick="rollAllCombatInitiative()"'''
content = re.sub(old_buttons, new_buttons, content, count=1)

# Fix 2: Make combat tracker open by default - change display: none to display: block
content = content.replace(
    'id="floating-combat-tracker" style="position: fixed; top: 100px; right: 20px; width: 500px; min-width: 350px; background: rgba(244, 228, 193, 0.98); border: 3px solid #8b6f47; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); z-index: 9999; display: none;',
    'id="floating-combat-tracker" style="position: fixed; top: 100px; right: 20px; width: 500px; min-width: 350px; background: rgba(244, 228, 193, 0.98); border: 3px solid #8b6f47; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); z-index: 9999; display: block;'
)

# Fix 3: Change selectAttackMode to NOT call hideTokenActionMenu - keep menu open until target selected
content = content.replace(
    "onclick=\"selectAttackMode('${token.id}', '${attack.replace(/'/g, \"\\\\'\")}')", hideTokenActionMenu();\"",
    "onclick=\"selectAttackMode('${token.id}', '${attack.replace(/'/g, \"\\\\'\")}');\""
)

# Write the fixed file
with open('BattleOfTrenton.html', 'w') as f:
    f.write(content)

print("Fixes applied!")
