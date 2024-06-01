from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
class Encryption:
    """
        Initializes an instance of the Encryption class.

        Args:
            password (str): The password to be hashed.
            hashed_password (str, optional): The hashed password. Defaults to an empty string.
    """
    
    def __init__(self, password:str, hashed_password = ""):
        self.password = password
        self.hashed_password  = hashed_password

    def password_hashing(self):
        """
        Generates a hashed password using the bcrypt algorithm.

        Parameters:
            password (str): The password to be hashed.

        Returns:
            str: The hashed password.
        """
        hashed_password = bcrypt.generate_password_hash(self.password).decode("utf-8")
        return hashed_password

    def decode_password(self, hashed_password, password):
        """
        Check if the provided password matches the hashed password.

        Parameters:
            hashed_password (str): The hashed password to compare against.
            password (str): The password to check.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        ispassword = bcrypt.check_password_hash(password, hashed_password)
        if ispassword:
            return True
        return False

if __name__ == "__main__":
    password = "nkang"
    obj1 = Encryption(password)
    hashed_password = (obj1.password_hashing())
    print(hashed_password)
    decrpyt = obj1.decode_password( password, hashed_password)
    print(decrpyt)

