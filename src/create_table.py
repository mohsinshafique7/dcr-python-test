from db import Country
import sqlite3

class CreateTables:
    
    def run(self):
        DB_FILE = "../data/countries.db"
        # Connect to the SQLite database
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        try:
            # Create the region table
            cursor.execute('''CREATE TABLE IF NOT EXISTS region (
                                id INTEGER PRIMARY KEY,
                                name TEXT
                            )''')

            # Create the country table with a foreign key constraint
            cursor.execute('''CREATE TABLE IF NOT EXISTS country (
                                id INTEGER PRIMARY KEY,
                                country_name TEXT,
                                alpha2Code TEXT,
                                alpha3Code TEXT,
                                population INTEGER,
                                topLevelDomain TEXT,
                                capital TEXT,
                                region_id INTEGER,
                                FOREIGN KEY (region_id) REFERENCES region(id)
                            )''')

            # Commit the changes
            conn.commit()
            print("Tables created successfully.")

        except sqlite3.Error as e:
            print("Error creating tables:", e)

        finally:
            # Close the connection
            conn.close()


if __name__ == "__main__":
    CreateTables().run()