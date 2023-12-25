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


def confirm_login(username: str, password: str):
    session = table_session()
    user = session.query(USER).filter_by(username=username).first()
    if user is None or not verify_password(user.password_hash, password):
        return False
    return True


def update_password(uid: str, password_hash: str):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.password_hash = password_hash
    session.commit()
    session.close()


def update_last_login(uid: str):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.last_login = datetime.now()
    session.commit()
    session.close()


def update_is_active(uid: str, is_active: bool):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.is_active = is_active
    session.commit()
    session.close()


def remove_user(uid: str):
    session = table_session()
    user = session.query(USER).filter_by(uid=uid).first()
    user.is_active = False
    session.commit()
    session.close()


############################################################
################### CONVERSATION FUNCTIONS #################
############################################################


def add_conversation(
    uid: str,
    chat_id: str,
    model: str,
    user_query: str,
    model_response: str,
    created_at: datetime,
):
    session = table_session()
    conversation_details = CONVERSATION(
        uid=uid,
        chat_id=chat_id,
        model=model,
        user_query=user_query,
        model_response=model_response,
        created_at=datetime.now(),
    )
    session.add(conversation_details)
    session.commit()
    session.close()


# All chats by the user
def get_conversations(uid: str):
    session = table_session()
    conversations = session.query(CONVERSATION).filter_by(uid=uid).all()
    session.close()
    return conversations


# Whole conversation within a chat session
def get_user_chat_conversation(uid: str, chat_id: str):
    session = table_session()
    conversation = (
        session.query(CONVERSATION).filter_by(uid=uid, chat_id=chat_id).first()
    )
    session.close()
    return conversation


# Whole conversation with one model
def get_model_conversation(uid: str, model: str):
    session = table_session()
    conversation = session.query(CONVERSATION).filter_by(uid=uid, model=model).first()
    session.close()
    return conversation


# Whole conversation with a model within a chat session
def get_user_model_conversation(uid: str, chat_id: str, model: str):
    session = table_session()
    conversation = (
        session.query(CONVERSATION)
        .filter_by(uid=uid, chat_id=chat_id, model=model)
        .first()
    )
    session.close()
    return conversation
