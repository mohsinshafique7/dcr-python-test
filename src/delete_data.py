from db import Country
import sqlite3

class DeleteData:
    
    def run(self):
        DB_FILE = "../data/countries.db"
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        try:
            # Get the list of tables in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            # Iterate over each table and delete all rows
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DELETE FROM {table_name};")
                print(f"Data removed from table '{table_name}'")

            # Commit the changes
            conn.commit()
            print("Data removed from all tables successfully.")

        except sqlite3.Error as e:
            print("Error removing data:", e)

        finally:
            # Close the connection
            conn.close()


if __name__ == "__main__":
    DeleteData().run()