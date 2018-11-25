from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from hokudai_furima.account.models import User
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from hokudai_furima.account.emails import send_account_activation_email
from django.contrib.auth.tokens import default_token_generator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()

        # 仮登録なので、is_activeがfalseになっている。trueにするリンクを持った本登録メール送信
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        validation_link_token = default_token_generator.make_token(user)
        context = {'uid': uidb64, 'token': validation_link_token}
        to_email_address = user.email
        send_account_activation_email(context, to_email_address)

        return user

    class Meta:
        model = User
        fields = ('token', 'email', 'username', 'password')