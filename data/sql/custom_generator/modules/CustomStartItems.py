from pathlib import Path



class CustomStartItems:
    """
    A class to generate SQL scripts for an AzerothCore 3.3.5a database.
    """
    def __init__(self):
        self.races = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
        self.classes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
        self.all_races_mask = 1791
        self.all_classes_mask = 1535


    def add_items(self, filename, item_id: int, note: str):
        print(f"Generating SQL script: '{filename}'...")

        with open(filename, "w") as sql_file:
            # Every character starts with a gun
            sql_file.write(
                f"INSERT INTO `playercreateinfo_item` (`race`, `class`, `itemid`, `Note`) VALUES\n"
                f"(0, 0, {item_id}, '{note}');"
            )


        print(f"SQL script '{filename}' generated successfully!")
        print(f"File saved to: {Path(filename).resolve()}")


    def add_items_for_all(self, filename, item_id: int, note: str):
        print(f"Generating SQL script: '{filename}'...")
        with open(filename, "w") as sql_file:
            # Every character starts with a gun
            for race in self.races:
                for cls in self.classes:
                    sql_file.write(f"INSERT INTO `playercreateinfo_item` (`race`, `class`, `itemid`, `Note`) VALUES\n")
                    sql_file.write(f"({race}, {cls}, {item_id}, '{note}');\n")
