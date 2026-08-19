import yt_dlp

url = input("กรุณาใส่ URL ของ YouTube: ")

options = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("ดาวน์โหลดเสร็จเรียบร้อยแล้ว")
