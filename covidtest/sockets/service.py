from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


def update_socket_new_object(application) -> None:
    data: dict = {
        "id": int(application.id),
        "full_name": f"{application.full_name}",
        "status": f"{application.get_status_in_str}",
        "result": f"{application.get_result_in_str}",
        "qr_code": f"{application.get_qr_code}",
        "period": f"{application.schedule.get_period}",
        "address": f"{application.address}",
        "age": int(application.age),
        "gender": f"{application.get_gender_in_str}",
        "phone": f"{application.phone}",
    }
    async_to_sync(channel_layer.group_send)(
        "room_STAFF", {"type": "send_message", "message": {**data}}
    )


def update_socket_status(application) -> None:
    application_id: int = int(application.id)
    status: str = f"{application.get_status_in_str}"
    result: str = f"{application.get_result_in_str}"
    async_to_sync(channel_layer.group_send)(
        f"room_{application.user_id}",
        {
            "type": "send_message",
            "message": {"id": application_id, "status": status, "result": result},
        },
    )
    async_to_sync(channel_layer.group_send)(
        "room_STAFF",
        {
            "type": "send_message",
            "message": {"id": application_id, "status": status, "result": result},
        },
    )
