from . import models


def add_user_db(data: dict[str]) -> None | str:
    try:
        models.db.session.add(models.Users(**data))
        models.db.session.commit()

    except:
        return 'При добавлении данных произошла ошибка'
