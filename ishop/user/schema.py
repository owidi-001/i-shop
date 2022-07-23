from rest_framework.schemas import AutoSchema
import coreapi
import coreschema


class RegistrationSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == "post":
            extra_fields = [
                coreapi.Field("username", required=True, location="form"),
                coreapi.Field(
                    "email", required=True, location="form", schema=coreschema.String()
                ),
                coreapi.Field(
                    "phone_number",
                    required=True,
                    location="form",
                    schema=coreschema.String(
                        pattern=r"\+254\w{9}",
                        description="must start with +254... eg +2547 xxxx xxxx",
                    ),
                ),
                coreapi.Field("password", required=True, location="form"),
                coreapi.Field("is_vendor", required=False, location="form", schema=coreschema.Boolean(default=False)),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class UserLoginSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        fields = [
            coreapi.Field("email", required=True, location="form"),
            coreapi.Field("password", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return fields + manual_fields


class UserSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["put", "post"]:
            extra_fields = [
                coreapi.Field("email", required=False, location="form"),
                coreapi.Field("phone_number", required=False, location="form"),
                coreapi.Field("username", required=False,
                              location="form", schema=None),
                coreapi.Field("avatar", required=False, location="form"),

            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class DriverSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["put", "post"]:
            extra_fields = [
                coreapi.Field("dl_number", required=False, location="form"),
                coreapi.Field("gender", required=False, location="form"),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


"""
For changing current user password
"""


class UpdatePasswordSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field("new_password", required=True, location="form"),
            coreapi.Field("old_password", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


"""
For resetting password/Forgot password
"""


class ResetPasswordSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field("email", required=True, location="form"),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields