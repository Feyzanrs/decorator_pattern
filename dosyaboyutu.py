import os

def file_size_decorator(func):
    def wrapper(file_path):
        size = func(file_path)
        print(f"Dosya boyutu: {size} bytes")
        return size
    return wrapper

@file_size_decorator
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"{file_path} bulunamadi.")
        return None

# Kullanım örneği
file_path = "C:\\Users\\feyza\\OneDrive\\Masaüstü\\UBNJR" # Dosya yolunu güncelleyin
 # Dosya yolunu güncelleyin
get_file_size(file_path)
