import random
import string


def set_contact_payload():
    """
    Setting a random contact payload to send to the contact API. We set 2 email addresses.
    n.b: here we assume the strings are large enough to get unicity.
    :return: hash random_contact: a random contact payload.
    """
    first_name = random.choice(string.ascii_letters.upper()) \
        + ''.join([random.choice(string.ascii_letters.lower()) for _ in range(9)])
    surname = random.choice(string.ascii_letters.upper()) \
        + ''.join([random.choice(string.ascii_letters.lower()) for _ in range(9)])
    username = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])
    email1 = ''.join([random.choice(string.ascii_letters) for _ in range(10)]) + \
        '@' + ''.join([random.choice(string.ascii_letters) for _ in range(7)]) + '.com'
    email2 = ''.join([random.choice(string.ascii_letters) for _ in range(10)]) + \
        '@' + ''.join([random.choice(string.ascii_letters) for _ in range(7)]) + '.com'

    random_contact = {'first_name': first_name,
                      'surname': surname,
                      'username': username,
                      'emails': [{'email': email1}, {'email': email2}]}
    return random_contact
