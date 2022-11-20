from voluptuous import Schema

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    }
)

get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    }
)
update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    }
)

register_successful_schema = Schema(
    {
        "id": int,
        "token": str
    }
)


login_successful_schema = Schema(
    {
        "token": str
    }
)
