# Whatsapp-Bulk-Messenger

Whatsapp Bulk Messenger automates sending of messages via Whatsapp Web. The tool can you used to send whatsapp message in bulk. Program uses runs through a list of numbers provided in numsbers.txt and then tries to send a prediefined (but templated) message to each number in the list. It can also read other columns from the number csv to populate template specific words and then send out a personalized message to the number

Note: The current program is limited to sending only TEXT message


# Requirements

*  Python >= 3.6
*  Chrome headless is installed by the program automatically

# Setup

1. Install python - >=v3.6
2. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `numbers.txt` file.Enter the code country with +
3. Run `python automator.py`.
4. Once the program starts, you'll see the message in message.txt and count of numbers in the numbers.txt file.
5. After a while, Chrome should pop-up and open web.whatsapp.com.
6. Scan the QR code to login into whatsapp.
7. Press `Enter` to start sending out messages.
8. Sit back and relax!

https://www.linkedin.com/in/majid-ahangari-7b861953/   
https://github.com/MajidAhangari    
My email address majidahangari2015@gmail.com       


