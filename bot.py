from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse
from stor import *
from commands import*
from reddit import*
from direction import directionHandler
from greeting import*
from newFood import*
from security import*

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():

    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('Now calling campus security.')
            from_number = request.form['From']
            resp.dial("+4032205333", caller_id=from_number)
            return str(resp)
        elif choice == '2':
            resp.say('Now calling mental health services.')
            from_number = request.form['From']
            resp.dial("+4032109355", caller_id=from_number)
            return str(resp)
        elif choice == '3':
            fact = getFact()
            resp.say(fact)
            resp.say("That was my awesome fact. Redirecting you to the home menu now.")
            resp.redirect('/voice')
            return str(resp)
        elif choice == '4':
            joke = getJoke()
            resp.say(joke[0], voice="Polly.Joey")
            resp.pause(length=1)
            resp.say(joke[1], voice='Polly.Matthew', pitch='25%')
            resp.say("That was my awesome joke. Redirecting you to the home menu now.")
            resp.redirect('/voice')
            return str(resp)
        else:
            resp.say("Sorry, I don't understand that choice.")

    # Start our <Gather> verb
    with resp.gather(numDigits=1) as gather:
        gather.say("Thank you for calling the University of Calgary student help center. For campus security, please press 1. For mental health services, please press 2. For an interesting fact, press 3. For a funny joke, press 4.")

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/voice')

    return str(resp)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'map' in incoming_msg:
        msg.body("Here is your map")
        msg.media("https://i.imgur.com/COpyc9D.png")
        return str(resp)
    elif directionHandler(incoming_msg):
        msg.body(directionHandler(incoming_msg))
        return str(resp)
    elif storHandler(incoming_msg):
        msg.body(storHandler(incoming_msg))
        return str(resp)
    elif commandHandler(incoming_msg):
        msg.body(commandHandler(incoming_msg))
        return str(resp)
    elif foodHandler(incoming_msg):
        msg.body(foodHandler(incoming_msg))
        return str(resp)
    elif foodHandler1(incoming_msg):
        msg.body(foodHandler1(incoming_msg))
        return str(resp)
    elif greetHandler(incoming_msg):
        msg.media("https://www.ucalgary.ca/brand/system/files/uc-vert-rgb-sml.jpg")
        msg.body(greetHandler(incoming_msg))
        return str(resp)
    elif ("quote" in incoming_msg) or ("deep" in incoming_msg):
        quote = getQuote()
        msg.body(quote[0])
        msg.media(quote[1])
    elif ("meme" in incoming_msg) or ("Meme" in incoming_msg):
        meme = getMeme()
        msg.body(meme[0])
        msg.media(meme[1])
    elif ("interesting" in incoming_msg) or ("learn" in incoming_msg) or ("fact" in incoming_msg):
        fact = getFact()
        msg.body(fact)
        return str(resp)
    elif ("security" in incoming_msg) or ("stress" in incoming_msg) or ("mental" in incoming_msg):
        msg.body(securityHandler(incoming_msg))
        return str(resp)
    elif ("comic" in incoming_msg) or ("poland" in incoming_msg) or ("ball" in incoming_msg):
        comic = getComic()
        msg.body(comic[0])
        msg.media(comic[1])
        return str(resp) 
    else:
        msg.body('Invalid command. Please type COMMAND for commands.')
    return str(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
