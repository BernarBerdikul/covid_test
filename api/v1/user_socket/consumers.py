from channels.generic.websocket import AsyncJsonWebsocketConsumer

from covidtest.sockets.middlewares import get_user


class UserConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """authenticate user in try...except"""
        try:
            email = (
                self.scope.get("url_route", {}).get("kwargs", {}).get("email", False)
            )
            if not email:
                await self.close()
            """ get params """
            self.scope["user"] = await get_user(email=email)
            user_id: int = self.scope["user"].id
            """ set room """
            self.room_group_name: str = f"room_{user_id}"
            """ join room group """
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            """ send order message """
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "send_message", "message": {"connect": True}},
            )
        except Exception:
            await self.close()

    async def disconnect(self, code):
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "send_message", "message": {"connect": False}},
        )
        """Leave room group"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def send_message(self, event):
        """send message in channel layer room"""
        await self.send_json({"message": event["message"]})
