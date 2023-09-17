from .models import db, Users, Orders, Offers
import sys


def add_obj_db(data: dict[str], model_name: str) -> None | str:
    try:
        db.session.add(getattr(sys.modules[__name__], model_name)(**data))
        db.session.commit()
    except ValueError:
        db.session.rollback()
        return 'При добавлении данных произошла ошибка'


def del_obj_db(data) -> None | str:
    try:
        db.session.delete(data)
        db.session.commit()
    except:
        db.session.rollback()
        return 'При удалении данных произошла ошибка'


def update_data_db(data):
    try:
        db.session.add(data)
        db.session.commit()
    except :
        return 'При обновлении данных произошла ошибка'
