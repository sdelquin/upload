dev:
    flask --app main.py --debug run

delete_db:
    rm -f upload.db

create_db:
    cat create_db.sql | sqlite3 upload.db
