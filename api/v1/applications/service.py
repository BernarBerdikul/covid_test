from io import BytesIO

import qrcode
from django.conf import settings
from django.core.files import File


def create_qr(application, schedule) -> None:
    """method for QR-code generating"""
    data: str = f"{settings.SITE_URL}/{application.id}"
    buffer = BytesIO()
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=0,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(buffer, "PNG")
    f_name: str = f"qr_code_{application.id}.png"
    application.qr_code.save(f_name, File(buffer), save=False)
    application.schedule_id = schedule.id
    application.save()
