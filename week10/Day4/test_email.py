import unittest
from unittest.mock import patch, MagicMock
import send_email  # your actual module name

class TestSendEmail(unittest.TestCase):

    @patch('send_email.smtplib.SMTP')
    @patch('send_email.load_dotenv')        
    @patch('send_email.os.getenv')           
    def test_send_email_success(self, mock_getenv, mock_load_dotenv, mock_smtp):
        mock_getenv.side_effect = lambda key: {
            "email_passcode": "fake_passcode",
            "sender_email": "sender@example.com",
            "receiver_email": "receiver@example.com"
        }[key]

        mock_server_instance = MagicMock()
        mock_smtp.return_value = mock_server_instance

        send_email.send_email()

        mock_load_dotenv.assert_called_once()
        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
        mock_server_instance.starttls.assert_called_once()
        mock_server_instance.login.assert_called_once_with("sender@example.com", "fake_passcode")
        mock_server_instance.sendmail.assert_called_once_with(
            "sender@example.com",
            "receiver@example.com",
            "Subject: Disk usage Alert\n\nHello this is a testing mail"
        )
        mock_server_instance.quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
