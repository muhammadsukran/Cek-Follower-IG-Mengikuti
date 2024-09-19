import json

# Fungsi untuk membaca file JSON >"Pastikan File program ini disimpan didalam folder yang sama"
def baca_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Fungsi untuk mengekstrak daftar username dari JSON
def extract_usernames(data):
    usernames = []
    for item in data:
        if "string_list_data" in item and len(item["string_list_data"]) > 0:
            username = item["string_list_data"][0]["value"]
            usernames.append(username)
    return usernames

# Membaca data dari file followers dan following >"Ganti nama file following dan follower"
following_data = baca_json('following.json')["relationships_following"]
followers_data = baca_json('followers_1.json')

# Ekstraksi username dari followers dan following
following_usernames = extract_usernames(following_data)
followers_usernames = extract_usernames(followers_data)

# Mencari username yang ada di following tapi tidak ada di followers
not_followed_back = set(following_usernames) - set(followers_usernames)

# Menampilkan hasil
print("Akun yang Anda ikuti tapi tidak mengikuti balik:")
for username in not_followed_back:
    print(username)
