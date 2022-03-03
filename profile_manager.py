import bcrypt


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password.encode('utf-8'))


def update_password_on_form(form, password):
    """Replaces the unhashed password with hashed one
    in dictionary"""
    form = dict(form)
    form['password'] = password
    return form


def validate_registration(form):
    """If every input matches the requirements
    returns True"""
    pass


def validate_login(form):
    """If every input matches the requirements
    returns True"""
    pass


def submit_registration(form):
    """This submits !valid! data to database
    If process successful returns user id"""
    return user_id


def is_password_format_correct(password):
    """If password formatted like, 'format_template'
    returns True"""
    return bool


def is_registration_major_data_equal(str1, str2):
    """If data field one and data field two
    the same string, returns True"""
    return bool


def is_unique_data_exist(unique):
    """If unique already exist in database
    returns True"""
    return bool


def unpack_registration_form(form_data):
    """Unpacks registration from coming from html
    returns username, email, password, pp_id = (profile_picture_id)"""
    return [username, email, password, pp_id]


def unpack_login_form(form):
    """Unpacks login form coming from html
    returns login_token, password"""
    return [login_token, password]
