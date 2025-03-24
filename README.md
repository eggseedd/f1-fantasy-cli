# F1 Fantasy CLI App 🏎️ 
  
A simple Python-based application to make custom F1 teams, including team principals, drivers, and engines using Microsoft SQL.

## 📌 Features
✅ Add new teams with team principal, drivers, and engine <br>
✅ Edit team details <br>
✅ Remove teams <br>
✅ List all teams, team principals, drivers, and engine manufacturers <br>
✅ Uses a relational database for data storage <br>

## 🚀 Getting Started
### 1️⃣ Prerequisites
Make sure you have:
- Python installed
- A database (Microsoft SQL Server)
### 2️⃣ Installation
1. Clone this repository:
```
git clone https://github.com/eggseedd/f1-fantasy-cli.git
cd f1-fantasy-cli
```
2. Set up the database:
   - Ensure your database is running
   - Update `database/db.py` with your connection settings
   - Run the provided SQL schema and seed to create tables and insert the list of team principals, drivers, engines provided
### 3️⃣ Usage
Run the script:
```
python main.py
```
## ⚙️ Database Schema
### Conceptual Data Model (CDM)
![F1_Fantasy-2025-03-24_15-23](https://github.com/user-attachments/assets/c942345c-a1c6-4fa1-aaa3-8c47d06f27e6)
### Physical Data Model (PDM)
![F1_Fantasy_Physical_Export-2025-03-24_15-26](https://github.com/user-attachments/assets/21913cc0-0e3a-4eed-b5f0-9294527ae2a7)

- `teams`: Stores custom team names
- `drivers`: Stores driver details
- `engines`: Stores engine manufacturers
- `team_principals`: Stores team principals


## For ITS Software Engineering Lab Admin 

### 1️⃣ Alasan dan Justifikasi Pemilihan Database
#### -Dibutuhkan ACID compliance karena ada beberapa tabel atau entitas yang harus memiliki ketetapan data.
dibutuhkan ACID compliance, yang memastikan ketepatan dan integritas data antar tabel. Tabel seperti `drivers`, `engines`, dan `team_principals` berisi data tetap yang tidak dapat diubah oleh pengguna. Saat pengguna melakukan operasi CRUD, rollback akan dilakukan jika terjadi error, sehingga hubungan antar tabel tetap terjaga dan tidak ada data yang rusak atau inkonsisten.
#### -Query yang dijalankan cukup sederhana dan masih memiliki runtime yang cepat
Query yang digunakan hanya menggunakan operasi dasar seperti SELECT, WHERE, JOIN, dan lain-lain, sehingga tetap efisien. Dengan struktur database yang sederhana dan jumlah data yang relatif, SQL masih mampu menangani eksekusi query dengan runtime yang cepat.
#### -Data yang digunakan tidak bersifat dinamis.
Data dalam sistem ini tidak bersifat dinamis, karena atribut yang digunakan memiliki struktur yang tetap. Oleh karena itu, SQL database lebih sesuai dibanding NoSQL, yang lebih cocok untuk data yang bersifat fleksibel dan tidak memiliki skema tetap.


Oleh karena itu, saya memutuskan untuk menggunakan **SQL (relational) database, Microsoft SQL**.
### 2️⃣ Fitur dari Database yang Digunakan
#### -JOIN
models/teams.py (line 146-156)<br>
![image](https://github.com/user-attachments/assets/6f9730cd-400a-4881-8bcd-3b9c53076a44)
#### -Rollback
models/teams.py (line 48-50, 72-74, 132-134)<br>
![image](https://github.com/user-attachments/assets/ceaeb4ba-971b-458e-b3f1-c24821e4d3ac)

![image](https://github.com/user-attachments/assets/e96472f3-2a7b-4e89-9728-fe6a44d259a5)

![image](https://github.com/user-attachments/assets/b0a0f8f7-0d27-435f-9658-e76866824f5f)




