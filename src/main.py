"""
Audio Files per minute - 1MB, 0.0010GB
Videos per minute      - 25MB, 0.025GB
Pictures 1920x1080     - 2.7MB, 0.0027GB
Applications           - 500MB, 0.5000GB
Video Games            - 10000MB, 10GB
"""
print("-=-=-=-=-=-=-=-=-=-=-=-")
print("   STORAGE CALCULATOR  ")
print("-=-=-=-=-=-=-=-=-=-=-=-")

audio = int(
    input("How many minutes of audio (MP3) will you store on your drive? "))
video = int(
    input("How many minutes of video (MP4) will you store on your drive? "))
pictures = int(
    input("How many pictures will you store on your drive? "))
applications = int(
    input("How many applications will you store on your drive? "))
games = int(
    input("How many video games will you store on your drive? "))

storage_size = audio * 0.001 + video * 0.025 + \
    pictures * 0.0027 + applications * 0.5 + games * 10

print("-=-=-=-=-=-=-=-=-=-=-=-")
print("What drive size you need: " + str(storage_size) + "GB")
