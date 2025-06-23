# Automated Cold Email Sender 

This project helps automate personalized cold emailing using Python. It reads a CSV list of recipients with job titles and company names, then sends tailored emails with your resume attached. Optionally, you can use services like SendGrid or Mailgun to track email opens.

## 💡 Features

- 🔁 Sends emails to multiple recipients with job and company-specific personalization
- 📎 Attaches your resume automatically to each email
- 🕙 Supports daily automation using Windows Task Scheduler
- 📊 Optional open-tracking support via SendGrid or Mailgun
- ⏱️ Adds delay between emails to avoid spam flags

---

## Project Structure

```
├── send_emails.py           # Main script to send personalized emails
├── email_list.csv           # CSV file with columns: company, job\_title, email
├── Your_Resume.pdf  # Resume to be attached with every email
└── README.md                # Project documentation
```
---

## Requirements

- Python 3.7+
- Modules: `smtplib`, `ssl`, `email`, `csv`, `time`, `schedule`, `requests` (for SendGrid/Mailgun)

Install any missing modules:
```bash
pip install schedule requests
````

---

## 📝 Setup Instructions

### 1. Prepare the CSV File

`email_list.csv` should look like this:

```csv
company,job_title,email
Tesla,Data Analyst,careers@tesla.com
OpenAI,ML Engineer,hiring@openai.com
```

### 2. Update the Script

In `send_emails.py`:

* Replace your Gmail email and **App Password** check out this [link](https://youtu.be/g_j6ILT-X0k?si=3_uy3K4Cev_ua-rK) to get app password for your email address.
* Make sure the resume file path is correct

### 3. Test It

Run manually:

```bash
python send_emails.py
```

---

## 🕘 Automate with Task Scheduler (Windows)

Use **Windows Task Scheduler** to run this script daily:

* Program: `python.exe`
* Arguments: `"path\to\send_emails.py"`
* Set schedule to your preferred time

---

## 📈 Optional: Enable Open Tracking

You can switch from Gmail to a provider like **SendGrid** or **Mailgun** to track opens and manage deliverability better.

---

## 📬 Disclaimer

This script is intended for ethical cold emailing. Please comply with email etiquette and anti-spam regulations.

---

## 👩‍💻 Author

**Ananta Verma**
[LinkedIn](https://linkedin.com/in/anantaverma) | [Portfolio](https://anantas-portfolio-d0858a.webflow.io/) | [Email](mailto:anantaverma20@gmail.com)

---

Feel free to ⭐️ this repo if it helps you, and contributions are welcome!
