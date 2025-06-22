import csv
import smtplib
import ssl
import time
from email.message import EmailMessage
import schedule

# Configuration
email_sender = ''
email_password = ''  # Use your Gmail App Password here
resume_path = 'CV.pdf'  # Path to your resume file

# creating a function to send personalized email -----
def send_personalized_email(receiver_email, company, job_title, name):
    subject = f"Application for {job_title} at {company}"
    body = f"""
Hi {name},

My name is Ananta Verma, I graduated as a Data Scientist from University of the Pacific in May, 2025. I understand your time is valuable, so I’ll keep this brief with the following bullet points:

- Proficient in Python, SQL, R, PyTorch, and AWS. 

- Experienced in ML workflows including NLP, computer vision, and RAG systems.

- Built and deployed an multimodal AI Travel Agent for itinerary generation and Shopify data insights dashboard for Pashion Footwear analyzing product performance, profits, and returns for business decision-making.

- Eager to learn and contribute to {company} by building data-driven, intelligent solutions that deliver real business impact.

I have applied for the {job_title} role at {company} and would welcome the opportunity to further discuss how my skills align with your team’s goals.

You can view my portfolio here - https://anantas-portfolio-d0858a.webflow.io/

I have also attached my resume for your reference. Thank you for your time and consideration.

Best regards,
Ananta Verma
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    # Attaching your resume
    with open(resume_path, 'rb') as file:
        em.add_attachment(file.read(), maintype='application', subtype='pdf', filename=resume_path)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
        print(f"Email sent to {receiver_email} for {job_title} at {company}")

# Creating a function to process CSV and send emails
def process_and_send():
    with open('email_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            send_personalized_email(row['email'], row['company'], row['job_title'], row['name'])
            time.sleep(10)  # Delay to avoid being flagged as spam

# (Optional) Schedule daily job at 10:00 AM
# # Uncomment this if you want to run it daily
# schedule.every().day.at("10:00").do(process_and_send)
# while True:
#     schedule.run_pending()
#     time.sleep(60)

# Run once
process_and_send()
