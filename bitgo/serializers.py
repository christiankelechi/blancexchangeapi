import base64
from io import BytesIO
import qrcode
# Deposit.update_deposits(user.profile)
from bitgo.models import Address

from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    qr_code = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = ['id', 'address', 'profile', 'wallet', 'bitgo_wallet', '_is_active', 'qr_code']

    def get_qr_code(self, obj):
        # generate qr code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )
        qr.add_data(obj.address)
        qr.make(fit=True)

        # save qr code as png image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        qr_img.save(buffer, format='PNG')
        qr_img.save('buffer.png', format='PNG')
        
        qr_bytes = buffer.getvalue()

        # create a base64 encoded string from the image bytes
        qr_base64 = base64.b64encode(qr_bytes).decode('utf-8')
        return qr_base64
