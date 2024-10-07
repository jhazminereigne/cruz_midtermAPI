import os
from webexteamssdk import WebexTeamsAPI


api = WebexTeamsAPI(access_token="YTIxNjVkMDItM2FlZC00ZTQ4LWEwMjktYzVlZmRkNzUwYWFkYmU4MjMyYmItNWE1_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e")


room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZTZiMDk5OTAtODQ3OC0xMWVmLTgxMWMtOTM1YzNhMjRkZTM0"


messages = api.messages.list(roomId=room_id)

print("Messages in the room:")
for message in messages:
    print(f"ID: {message.id}, Text: {message.text}")


message_id = input("Enter the message ID to delete: ")


try:
    api.messages.delete(messageId=message_id)
    print(f"Message {message_id} deleted successfully")
except Exception as e:
    print(f"Error deleting message {message_id}: {str(e)}")