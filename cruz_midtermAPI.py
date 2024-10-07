
import os
from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token ="YTIxNjVkMDItM2FlZC00ZTQ4LWEwMjktYzVlZmRkNzUwYWFkYmU4MjMyYmItNWE1_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e")


room_name = input("Enter the room name: ")
message = input("Enter the welcome message: ")


room = api.rooms.create(room_name)


api.messages.create(roomId=room.id, text=message)

print(f"Room created: {room_name}")
print(f"Message sent: {message}")

