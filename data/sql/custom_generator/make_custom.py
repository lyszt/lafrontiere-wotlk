import os.path
from pathlib import Path

from modules.MakeCustomNPCS import MakeCustomNPCS
from modules.CustomSkillSetter import CustomSkillSetter

CUSTOM_WEAPONS = "custom_weapon_proficiencies.sql"

# Creates all custom components and database changes
if __name__ == '__main__':
    # Custom Skills
    CustomSkillSetter().generate_all_weapon_proficiencies_sql(filename=str(Path("../custom/db_world").resolve() / CUSTOM_WEAPONS))

    # Custom NPCs
    MakeCustomNPCS(folder_db=str(Path("../custom/db_characters").resolve())).run()