{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c48d3491-f7fa-4e68-a126-1d6c3068f248",
   "metadata": {},
   "outputs": [],
   "source": [
    "import smtplib\n",
    "from email.message import EmailMessage\n",
    "\n",
    "def send_email_native(subject, body, sender, password, recipient):\n",
    "    msg = EmailMessage()\n",
    "    msg.set_content(body)\n",
    "    msg[\"Subject\"] = subject\n",
    "    msg[\"From\"] = sender\n",
    "    msg[\"To\"] = recipient\n",
    "\n",
    "    with smtplib.SMTP_SSL(\"smtp.gmail.com\", 465) as smtp:\n",
    "        smtp.login(sender, password)\n",
    "        smtp.send_message(msg)\n",
    "    print(\"Email Sent\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
