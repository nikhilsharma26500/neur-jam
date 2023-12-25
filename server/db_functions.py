from db_schema import USER, CONVERSATION
from db_schema import table_session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid


def password_hash(password):
    return generate_password_hash(password)


def verify_password(password_hash, password):
    return check_password_hash(password_hash, password)


############################################################
####################### USER FUNCTIONS #####################
############################################################


def add_user(
    first_name: str,
    last_name: str,
    email: str,
    username: str,
    password: str,
    is_active: bool,
    is_verified: bool,
):
    session = table_session()
    user_details = USER(
        uid=uuid.uuid4().hex,
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
        password_hash=password_hash(password),
        is_active=is_active,
        is_verified=is_verified,
        last_login=datetime.now(),
        created_at=datetime.now(),
    )
    session.add(user_details)
    session.commit()
    session.close()


def confirm_login(username, password):
    session = table_session()
    user = session.query(USER).filter_by(username=username).first()
    if user is None or not verify_password(user.password_hash, password):
        return False
    return True


def update_password(uid, password_hash):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.password_hash = password_hash
    session.commit()
    session.close()


def update_last_login(uid):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.last_login = datetime.now()
    session.commit()
    session.close()


def update_is_active(uid, is_active):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.is_active = is_active
    session.commit()
    session.close()


def remove_user(uid):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.is_active = False
    session.commit()
    session.close()


