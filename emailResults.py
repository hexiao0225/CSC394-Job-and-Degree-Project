# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

# Create a text/plain message


def sendEmailResults(emailAddr, bestFit, description):


	msg = MIMEText("""Hello from Kalia!

	You said you wanted to save your results so here they are!

	Your best fit was: {}!

	Short description: {}


	Thank you for using Kalia, we hope you enjoyed your experience!

	Sincerely, 
	The awesome folks at Team One""".format(bestFit, description))


	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = "Your Kalia Results"
	msg['From'] = "kalia.teamone.depaul@gmail.com"
	msg['To'] = emailAddr

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login("kalia.teamone.depaul@gmail.com", "teamoneisthebest")
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()