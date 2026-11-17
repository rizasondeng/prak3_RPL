from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"
        self.last_error = ""

    def get_all_buku(self):
        if self.conn is None:
            self.conn = self.db.get_connection()
        if self.conn:
            try:
                cursor = self.conn.cursor(dictionary=True)
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Exception as e:
                print(f"Error get_all_buku: {e}")
                return []
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        self.last_error = ""
        if self.conn is None:
            self.conn = self.db.get_connection()
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
                val = (judul, penulis, tahun_terbit)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                self.last_error = str(e)
                print(f"Error create_buku: {e}")
                return False
        self.last_error = "Koneksi database tidak tersedia"
        return False
