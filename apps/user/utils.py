from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    role = get_role(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_id':str(user.id),
        'user_type': str(role),
        'username':str(user),
        'user_email':str(user.email),
        'is_staff':str(user.is_staff),
        'is_uber':str(user.is_uber),
        'is_passenger':str(user.is_passenger)
    }


def get_role(user):
    if user.is_staff:
        return "admin"
    elif user.is_uber:
        return "uber staff"
    elif user.is_passenger:
        return "passenger"

