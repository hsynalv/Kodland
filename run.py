from app import app, db

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():  # Uygulama bağlamı oluşturuluyor
    db.create_all()  # Veritabanını oluştur
