from app import db

with app.app_context():
    db.create_all()  # creates Chat table
    print("✅ Tables created successfully!")
