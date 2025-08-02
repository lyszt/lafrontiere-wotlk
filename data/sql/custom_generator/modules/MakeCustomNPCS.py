from pathlib import Path

class MakeCustomNPCS:
    def __init__(self, folder_db):
        self.filename = Path(folder_db) # Ensure it's a Path object here

    def run(self):
        self.create_lieutenant_battlemaster()

    def create_lieutenant_battlemaster(self):
        print("Creating Lieutenant Battlemaster. Location: Northshire Valley")

        with open(self.filename / "battlemaster.sql", "w") as sql_file:
            sql_file.write("UPDATE acore_world.creature "
                           "SET position_x = -8913.835, position_y = -135.12477, position_z = 80.4693 WHERE guid = 79942;\n")
            sql_file.write("UPDATE acore_world.creature_template "
                           "SET name = 'Lieutenant Battlemaster' WHERE entry = 823;\n")

            # 4143 = Arathi Vindicator
            sql_file.write("UPDATE acore_world.creature_template_model "
                           "SET CreatureDisplayID = 4143 WHERE CreatureID = 823;\n")