from users.schemas import CreateUser


def create_user(this_user: CreateUser):
    user = this_user.model_dump()
    return {"sucsses": True, "user": user}
