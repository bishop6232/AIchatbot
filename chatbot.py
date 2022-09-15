import greetings

print("Welcome to AI chatbot!")
print(greetings.respond_greetings(input()))
print("how can i help you today?\n")
print("i'm programmed to assist you with your 'visa' application process")

while True:
    user_reason = input()
    bot_responses = "what kind of visa are you applying for?"
    if user_reason.lower() == "i want to apply for visa" or user_reason.lower() == "i want to apply visa" or user_reason.lower() == "how can i apply visa?" or user_reason.lower() == "i want to apply for a visa" or user_reason.lower() == "visa":
        print(bot_responses)
        break
    else:
        print("Not sure I understand, Please give me more info: ")

while True:
    visa_selection = input()
    if visa_selection.lower() == "student visa":
        print("Ok,i will be glad to assist you with that\n")
        print(f"For {visa_selection}! please submit the following information")
        break
    elif visa_selection.lower() == str("work visa" or "family visa" or "business visa"):
        print("sorry this type of visa is not available at the moment only 'STUDENT VISA' is available")
    elif visa_selection.lower() == str("family visa"):
        print("sorry this type of visa is not available at the moment only 'STUDENT VISA' is available")
    elif visa_selection.lower() == str("business visa"):
        print("sorry this type of visa is not available at the moment only 'STUDENT VISA' is available")
    else:
        print("invalid input")
while True:
    biometrics_submit = input("\nDo you have an active biometrics: \n")
    biometrics_yes = "\nok, you can proceed with the visa application"
    if biometrics_submit.lower() == "yes":
        print(biometrics_yes)
        break

    elif biometrics_submit.lower() == "no":
        print("\nSorry, you have to go to the nearest visa center close to you to do your biometrics before you can continue your visa process")
        print(">>>>>>    The chat ended    <<<<<<")
        quit()

while 1:
    user_data = input("\nwhat is your first name?\n")
    if user_data.isalpha():
        print(f"{user_data}")
        break
    else:
        print("invalid input")
while 2:
    user_data = input("\nwhat is your last  name?\n")
    if user_data.isalpha():
        print(f"{user_data}")
        break
    else:
        print("invalid input")
while 3:
    user_data = input("\nwhat is your birth date: please enter in this format eg. June_05_1999?\n")
    if user_data.isidentifier():
        print(f"{user_data}")
        break
    else:
        print("invalid input")
while 4:
    user_data = input("what is your email address?\n")
    if user_data.isprintable():
        print(f"{user_data}")
        break
    else:
        print("invalid input")
while 5:
    user_data = input("please provide me with your valid passport number\n")
    if user_data.isidentifier():
        print(f"{user_data}")
        print("\nthank you very much for the information\n")
        print("here is the list of documents you have to upload for your student visa\n")
        print("\nfully filled and signed Visa Application Forms\n")
        print("\nletter of admission from the university in Germany\n")
        print("\nschool Leaving Certificates of Primary and Secondary School / WAEC Certificate\n")
        print("\nofficial birth certificate\n")
        print("\npersonally signed letter of motivation\n")
        print("\npersonally signed Curriculum Vitae stating all visited schools,universities "
              "and listing of all employers until date of visa application\n")
        print("\nproof of financial means for the duration of your stay, maximum one year\n")
        print("\nproof of knowledge of the German language, if applicable\n")
        break
    else:
        print("invalid input")

while True:
    user_pay_response = input("\nPlease click on 'PAY NOW' to be directed to the secure channel where you can pay your visa fee: ")
    bot_responses = "ok, now redirecting you to a secure channel for your payment........"
    if user_pay_response.lower() == "pay" or user_pay_response.lower() == "pay now" or user_pay_response.lower() == "paynow":
        print(f"{bot_responses}")
        print("\npayment was successful,.....\n")
        break
    else:
        print("Wrong input")

while True:
    user_scan_response = input("\nPlease type 'SCAN' to scan your passport data page: ")
    bot_response = "\nThank you....scan was successful"
    if user_scan_response.lower() == "scan" or user_scan_response.lower() == "scannow" or user_scan_response.lower() == "scan now":
        print(f"{bot_response}")
        print("\nYou can now make a face capture")
        print(">> successful << thank you for the face capture...")
        break
    else:
        print("Wrong input: please type 'SCAN'")


while True:
    user_upload_response = input("\nclick the 'upload' button to upload the documents listed above: ")
    bot_response = "Uploading.......\nthank you very much for uploading the requested documents"
    if user_upload_response.lower() == "upload" or user_upload_response.lower() == "upload now":
        print(f"{bot_response}")
        print("\nyou will be connected to an agent now to ask you some questions regarding your visa application\n")
        print("\nconnecting......\n")
        print("\nthank you for answering the questions....."
              "you will get an email from us if the visa is approved and also a rejection email if rejected\n")
        print("\nif you receive an approved visa email please login to this platform again and your '2D barcode visa' "
              "will be available\n")
        print("\n you have completed your visa process: you can now end the chat: \n")
        print(greetings.respond_goodbye(input()))
        break
    else:
        print("Wrong input: please type 'UPLOAD'")

