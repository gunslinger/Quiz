import random
from quiz_choice import *
from os import system
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def check_initial_choice(initial_answer):
    if initial_answer in ["Y", "y", "yes","YES"]:
        return True
    else:
        return False
def check_answer():
    answer = raw_input("Your answer is : ")
    while answer not in ['a', 'b', 'c', 'd']:
        answer = raw_input("Your answer is (please only input a, b, c, or d): ").lower()
    return answer

def score_emo(input_score):
    if input_score <= 30:
        emo = ":("
    elif input_score >= 31 and input_score <= 60:
        emo = ":|"
    else:
        emo = ":)"
    return emo

def send_mail(recipient, subject, message):
    username = "tsq-ttp@outlook.com"
    password = "TSQ1234@"

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('Please wait...')

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        #mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()
    except smtplib.socket.gaierror as e:
        print(str(e))
    except smtplib.SMTPServerDisconnected as e:
        print "[!!!] Please tell admin: You need to login to your mail provider and fill captcha for anti spam checking..."

#print initial_choice

def main():
    score = 0
    cnt_score = 10
    max_question = 10
    passed_topic = []
    q_cnt = 1
    max_question_count = len(ls)
    debug = False
    welcome_message = "Welcome to the Space Quiz"
    email_result = "tsq-ttp@outlook.com"  # "yudha.gunslinger@gmail.com"
    copyright = ""
    brief = """In this Quiz, it will test you for your abilities of recalling knowledge about Space.
You will be given a maximum of 10 questions to answer, using your keyboard. The total
mark is out of 100 and make sure, you are prepared to go infinity and beyond!"""
    system("cls")
    print welcome_message
    print brief
    name = raw_input("Enter your name : ")
    initial_choice = raw_input("Hello %s, Do you want to start quiz now? (Y/n)" % (name))

    if debug: print len(list(ls))
    if check_initial_choice(initial_choice):
        while q_cnt <= max_question:
            system("cls")
            not_choosed = False
            num_choosed = random.choice(ls)
            num_choosed_key = num_choosed.keys()
            while num_choosed_key not in passed_topic:
                if debug: print "num_choosed %s" % (num_choosed.keys())
                questions = num_choosed
                passed_topic.append(num_choosed_key)
            #if questions.keys() not in passed_topic:
                for topic, choice in questions.iteritems():
                    #print topic
                    print "%s\n%s\n%s\n%s\n%s\n" % (topic, choice['a'], choice['b'], choice['c'], choice['d'])
                    #print passed_topic
                    input_answer = check_answer()
                    if choice["theanswer"] == input_answer:
                        score+=10
                    if debug: print score
                    #print choice["d"]
                q_cnt += 1
        send_mail(email_result, 'Space Quiz by %s' % name,
                  'Hello,\n\nName : %s\nScore : %d\n\nSent by Space Quiz program' % (name, score))
        print "Hello %s, your final score is %d %s" % (name, score, score_emo(score))
        print copyright
    else:
        raw_input("Program will quit... \nPress any key to exit")

if __name__ == '__main__':
    main()
    rechoice = True
    while rechoice:
        a_rechoice = raw_input("Would you like to retry test? (Y/n)")
        if check_initial_choice(a_rechoice):
            main()
        else:
            raw_input("Program will quit... \nPress any key to exit")
            break

