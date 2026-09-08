import bcrypt

from src.database.config import supabase

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def check_teacher_exists(username):
    response = supabase.table('teachers').select('username').eq('username', username).execute()
    return len(response.data) > 0

def create_teacher(username, password, name):
    data = {
        "username": username,
        "password": hash_password(password),
        "name": name
    }
    response = supabase.table('teachers').insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table('teachers').select('*').eq('username', username).execute()
    if response.data:
        teacher = response.data[0]
        if check_password(password, teacher["password"]):
            return teacher
    return None