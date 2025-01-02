import smtplib  # Import the library to handle email sending

# Step 1: Establish a connection to the SMTP server
ob = smtplib.SMTP("smtp.gmail.com", 587)  # Connect to Gmail's SMTP server on port 587
ob.ehlo()  # Identify yourself to the server
ob.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection

# Step 2: Login into your email account
your_email = ""  # Replace with your email address
your_password = ""  # Replace with your email password
ob.login(your_email, your_password)  # Authenticate with the SMTP server using your credentials

# Step 3: Create the email content
subject = ""  # Subject line of the email
body = ""  # Body content of the email
message = f"Subject: {subject}\n\n{body}"  # Format the email message with subject and body

# Step 4: Define recipient email addresses
email_1 = ""  # Replace with the first recipient's email address
email_2 = ""  # Replace with the second recipient's email address
email_3 = ""  # Replace with the third recipient's email address
email_4 = ""  # Replace with the fourth recipient's email address
email_5 = ""  # Replace with the fifth recipient's email address

# Step 5: Add recipients to a list
email_list = [email_1, email_2, email_3, email_4, email_5]  # A list containing all recipient email addresses

# Step 6: Send the email to each recipient
for recipient in email_list:  # Loop through the recipient list
    ob.sendmail(your_email, recipient, message)  # Send the email to the current recipient

# Step 7: Close the connection to the SMTP server
ob.quit()  # Terminate the connection with the SMTP server
