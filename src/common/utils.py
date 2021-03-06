from passlib.hash import pbkdf2_sha512
import re

__author__ = 'Qingyun Wu'


class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(hashed_password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(hashed_password)

    @staticmethod
    def check_hashed_password(hashed_password, double_hashed_password):
        """
        Checks that the password the user sent matches that of the database.
        The database password is encrypted more than the user's password at this stage.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if passwords match, False otherwise
        """
        return pbkdf2_sha512.verify(hashed_password, double_hashed_password)