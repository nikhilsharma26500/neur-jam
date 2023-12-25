from db_functions import (
    add_user,
    confirm_login,
    update_password,
    update_last_login,
    update_is_active,
    remove_user,
)
from db_functions import (
    add_conversation,
    get_conversations,
    get_user_chat_conversation,
    get_model_conversation,
    get_user_model_conversation,
)
from db_schema import table_session


# USER FUNCTIONS


def test_add_user():
    session = table_session()

    first_name = "Test"
    last_name = "User"
    email = "test@123.com"
    username = "testuser"
    password = "testpassword"
    is_active = True
    is_verified = False

    test = add_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=username,
        password=password,
        is_active=is_active,
        is_verified=is_verified,
    )

    session.close()


# test_add_user()


def test_confirm_login():
    session = table_session()
    username = "testuser"
    password = "testpassword"

    test = confirm_login(username, password)

    session.close()


# test_confirm_login()


def test_update_password():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"
    password = "testpasswordtest"

    test = update_password(uid, password)

    session.close()


# test_update_password()


def test_update_last_login():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"

    test = update_last_login(uid)

    session.close()


# test_update_last_login()


# CONVERSATION FUNCTIONS


def test_add_conversation():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"
    chat_id = "1"
    model = "llm1"
    user_query = "hi is this working?"
    model_response = "ooga booga beep bop"

    test = add_conversation(
        uid=uid,
        chat_id=chat_id,
        model=model,
        user_query=user_query,
        model_response=model_response,
    )

    session.close()


# test_add_conversation()


def test_get_conversations():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"

    test = get_conversations(uid)

    session.close()


# test_get_conversations()


def test_get_user_chat_conversation():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"
    chat_id = "1"

    test = get_user_chat_conversation(uid, chat_id)

    session.close()


# test_get_user_chat_conversation()


def test_get_model_conversation():
    session = table_session()

    model = "llm1"
    uid = "a6d3af6b4faa4766b23a4d70662f6abc"

    test = get_model_conversation(uid, model)

    session.close()


# test_get_model_conversation()

def test_get_user_model_conversation():
    session = table_session()

    uid = "a6d3af6b4faa4766b23a4d70662f6abc"
    chat_id = "1"
    model = "llm1"

    test = get_user_model_conversation(uid, chat_id, model)

    session.close()
    
# test_get_user_model_conversation()
