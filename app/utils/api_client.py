import json
from zoomus import ZoomClient

# todo move this to a yaml resources config file
zoom_client = ZoomClient(
    "ZfQeVKDQZMTX1JDcKfw", "8vDRVnzxjpUlFf6ltojszP7rgbWgxzYG", "LXrDeI6gSGiI3IgFfXc9bw"
)


def get_meeting_attendees(meeting_id: str):
    """
    Get the attendees of a meeting.
    """

    user_list_response = zoom_client.user.list()
    user_list = json.loads(user_list_response.content)

    try:
        for user in user_list["users"]:
            user_id = user["id"]
            # print(json.loads(zoom_client.meeting.list_meeting_participants(id=meeting_id).content))
            participants_response = json.loads(
                zoom_client.report.get_meeting_participants_report(
                    id=meeting_id
                ).content
            )
            attendees = participants_response.get("participants", [])

            return [
                {
                    "user_id": attendee["user_id"],
                    "name": attendee["name"],
                    "email": attendee["user_email"],
                    "status": attendee["status"],
                }
                for attendee in attendees
            ]
    except json.JSONDecodeError:
        print("Error: Invalid JSON data")
        return []

    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
        return []
