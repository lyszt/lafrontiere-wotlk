from pathlib import Path
class AllRaceAllSkills:
    """
    A class to generate SQL scripts for an AzerothCore 3.3.5a database.
    """
    def __init__(self):
        self.races = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
        self.classes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.all_races_mask = 2549
        ]

    def generate_all_weapon_proficiencies_sql(self, filename):
        """Generates the SQL file with REPLACE INTO statements."""
        print(f"Generating SQL script: '{filename}'...")

        with open(filename, "w") as sql_file:
            sql_file.write("-- This script grants all weapon proficiencies to all playable races and classes.\n")
            sql_file.write("-- It uses REPLACE INTO to safely add spells without affecting existing ones.\n\n")
            sql_file.write("REPLACE INTO `playercreateinfo_spell_custom` (`racemask`, `classmask`, `Spell`, `Note`) VALUES\n")

            all_lines = []

            for spell_id in self.proficiencies:
                note = f" -- Spell ID {spell_id} added by Python script"
                line = f"({self.all_races_mask}, {self.all_classes_mask}, {spell_id}, '{note}')"
                all_lines.append(line)

            for i, line in enumerate(all_lines):
                if i < len(all_lines) - 1:
                    sql_file.write(f"  {line},\n")
                else:
                    sql_file.write(f"  {line};\n")

        print(f"SQL script '{filename}' generated successfully!")
        print(f"File saved to: {Path(filename).resolve()}")
