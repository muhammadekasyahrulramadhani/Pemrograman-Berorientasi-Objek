class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Inisialisasi koneksi database di sini
            cls._instance.connection_string = "Database Connection Established"
        return cls._instance

    def get_connection(self):
        return self.connection_string

# Penggunaan Singleton
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"Connection String from db1: {db1.get_connection()}")
    print(f"Connection String from db2: {db2.get_connection()}")
    print(f"Are both instances the same? {'Yes' if db1 is db2 else 'No'}")