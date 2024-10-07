import os
from webexteamssdk import WebexTeamsAPI


api = WebexTeamsAPI(access_token= "YTIxNjVkMDItM2FlZC00ZTQ4LWEwMjktYzVlZmRkNzUwYWFkYmU4MjMyYmItNWE1_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e")

def add_participants(room_id, participant_emails):
   
    for email in participant_emails:
        api.memberships.create(roomId=room_id, personEmail=email)


room_id = input("Enter the room ID: ")
participant_emails = input("Enter the participant emails (comma-separated): ").split(",")


participant_emails_list = []
participant_emails_list.extend(participant_emails)

add_participants(room_id, participant_emails_list)

print(f"Participants added to room {room_id}")