import os.path
from pathlib import Path

from modules.AzerothCoreDBWriter import AzerothCoreDBWriter

CUSTOM_WEAPONS = "custom_weapon_proficiencies.sql"

# Creates all custom components and database changes
if __name__ == '__main__':
    AzerothCoreDBWriter().generate_all_weapon_proficiencies_sql(filename=str(Path("../custom/db_world").resolve() / CUSTOM_WEAPONS))