TOKEN = '5433210546:AAERAXlUecVL81d0DA8l8apapYXsrYqhhXI'
host = '127.0.0.1'
user = 'postgres'
password = 'qwerty'
database = 'b201'
port_for_db = '5432'
charset = 'utf8mb4'
chat_id = '-1001445976600'
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'webm',
        'preferredquality': '192',
    }],
    'forceurl': True,
}
port_for_redis = '6379'
decode_response = True
