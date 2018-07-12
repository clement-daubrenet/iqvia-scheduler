from tasks.services import set_contact_payload


def test_contact_payload():
    """
    Testing the function to set the payload for contact creation.
    :return:
    """
    contact_payload = set_contact_payload()

    assert 'username' in contact_payload.keys()
    assert 'emails' in contact_payload.keys()
    assert 'first_name' in contact_payload.keys()
    assert 'surname'in contact_payload.keys()
    assert len(contact_payload['emails']) == 2
