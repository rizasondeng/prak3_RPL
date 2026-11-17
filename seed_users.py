from config.database import Database
from models.user_model import UserModel


def seed():
    db = Database()
    conn = db.get_connection()
    if not conn:
        print("Koneksi ke database gagal! Pastikan MySQL sudah aktif.")
        return

    cur = conn.cursor(dictionary=True)

    users_to_add = [
        ("admin", "admin123", "admin"),
        ("user", "user123", "anggota"),
    ]

    for username, pwd, role in users_to_add:
        pwd_hash = UserModel.hash_password(pwd)
        query = """
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE password = VALUES(password), role = VALUES(role)
        """
        cur.execute(query, (username, pwd_hash, role))

    conn.commit()
    print("Akun admin dan user berhasil ditambahkan ke database!")


if __name__ == "__main__":
    seed()
