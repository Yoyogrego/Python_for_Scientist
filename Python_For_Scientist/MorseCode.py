#%%
#Finished by Gregory Krulin
def Build_Character_Encoder():
    '''
    return Character_Encoder, a dictionary
    Specification:
        Character_Encoder is a mapping from Character to Morse Code
        Every character in list('abcdefghijklmnopqrstuvwxyz0123456789') can be encoded in Morse code:
            Character_Encoder['a'] is '.-', which means 'a' is encoded to '.-' (Morse code)
            Character_Encoder['0'] is '-----'
        see https://en.wikipedia.org/wiki/Morse_code
        Let's 'enhance' Morse code to handle other characters
        Every character in list("""`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?""") is encoded to '.-.-.-'
            Character_Encoder['@'] is '.-.-.-'
            Character_Encoder['#'] is '.-.-.-'
        Now, every character on computer keyboard can be represented by Morse code
    '''
    # CodeList1 contains Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # CodeList2 contains Morse codes of the 10 integers from 0 to 9
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    # define three lists of characters
    #hint: try the following lines in console, see what they do
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')
    CharList3 = list("""`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?""")
    # define an empty dictionary
    Character_Encoder={}
    # add your code from here
    for i in range(len(CharList1)):
        Character_Encoder[ (CharList1[i] ) ] = CodeList1[i]
        
    for i in range(len(CharList2) ):
        Character_Encoder[ (CharList2[i] ) ] = CodeList2[i]
        
    for i in range(len (CharList3)):
        Character_Encoder[ CharList3[i] ] = '.-.-.-'
    
    return Character_Encoder
#%%
def Build_Character_Decoder():
    '''
    return Character_Decoder, a dictionary
    Specification:
            Character_Decoder is a mapping from Morse Code to Character
            Character_Decoder['.-'] is 'a', which means '.-' is decoded to 'a'
        All decoded letters are in lower case
            '.-' is 'a', not 'A'
        The special Morse code '.-.-.-' is decoded to '#':
             Character_Decoder['.-.-.-']  is '#'
    '''
    # add your code from here
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')
    
    Character_Decoder = {}
    
    for i in range(len(CodeList1) ):
        Character_Decoder[ CodeList1[i] ] = CharList1[i]
        
    for i in range(len(CodeList2) ):
        Character_Decoder[ CodeList2[i] ] = CharList2[i]
        
    Character_Decoder['.-.-.-'] = '#'
        
    

    return Character_Decoder
# %%
def Word_Encoder(Word, Character_Encoder=None):
    '''
    Word is an english word (str), e.g. 'Python'
    Character_Encoder is from BuildEncoder (Build_Character_Encoder() )
    return Word_in_Morse_Code
    a blank space is added between the two Morse codes of two adjacent letters in Word
    Examples: (enable the option Source->Show Blank Spaces in Sypder)
        Word "Gin" is converted to lowercase 'gin'
        then, "gin" is encoded to Word_in_Morse_Code "--. .. -." (NOT "--...-.")
    '''
    if Character_Encoder == None:
        Character_Encoder = Build_Character_Encoder()
    # add your code from here
    Word = Word.lower()
    word_decomposed = list(Word)
    word_encoded = []
    
        
    for i in range(len(word_decomposed)):
        word_encoded.append(Character_Encoder[ word_decomposed[i] ] )
        
    Word_in_Morse_Code = word_encoded[0]
    
    if len(Word)==1:
        return Word_in_Morse_Code
    
    if len(Word)==2:
         Word_in_Morse_Code += ' ' + word_encoded[1]
         return Word_in_Morse_Code
    
    for c in word_encoded[1:len(word_encoded) - 1]:
        Word_in_Morse_Code += ' ' + c + ' '
        
    Word_in_Morse_Code += word_encoded[len(word_encoded) - 1]

    return Word_in_Morse_Code
# %%
def Word_Decoder(Word_in_Morse_Code, Character_Decoder=None):
    '''
    Word_in_Morse_Code is from Word_Encoder
    Character_Decoder is from Build_Character_Decoder
    return the Word in Engilish
    Examples:
        Word_in_Morse_Code "--. .. -." is decoded to Word "gin" in English
        Word_in_Morse_Code "--. .. -. .-.-.-" is decoded to Word "gin#" in English
    '''
    if Character_Decoder == None:
        Character_Decoder = Build_Character_Decoder()
    # add your code from here
    code = (Word_in_Morse_Code).split()
    
    while( ' ' in code ):
        code.remove(' ')
        
    Word = ''
    
    for i in range( len(code) ):
        Word += Character_Decoder[code[i]]

    return Word
# %%
def Message_Encoder(Message, Character_Encoder=None):
    '''
    Message is an english sentence (str)
    Character_Encoder is from Build_Character_Encoder
    return Message_in_Morse_Code (str)
    steps:
    (1) split Message to words
    (2) use Word_Decoder to transform each word to Morse codes
    (3) add a comma between Morse codes of two adjacent words in Message
        before concatenating all Morse codes into a string
    Message_in_Morse_Code is the concatenation of all Morse codes, blank spaces and commas
    Examples:
        Message 'Hello Python 3.6'-> ['Hello', 'Python', '3.6']
        'Hello' is transformed to '.... . .-.. .-.. ---'
        'Python' is transformed to '.--. -.-- - .... --- -.'
        '3.6' is transformed to '...-- .-.-.- -....'
        Message 'Hello Python 3.6' is transformed to Message_in_Morse_Code:
            '.... . .-.. .-.. ---,.--. -.-- - .... --- -.,...-- .-.-.- -....'
    '''
    if Character_Encoder == None:
        Character_Encoder = Build_Character_Encoder()
    # add your code from here
    words = Message.split()
    coded_words = []
    
    for i in range(len(words)):
        coded_words.append(Word_Encoder(words[i], Character_Encoder) )
    
    Message_in_Morse_Code = coded_words[0]
    
    for s in coded_words[1:]:
        Message_in_Morse_Code += ','+s
    

    return Message_in_Morse_Code
# %%
def Message_Decoder(Message_in_Morse_Code, Character_Decoder=None):
    '''
    Message_in_Morse_Code is from Message_Encoder
    Character_Decoder is from Build_Character_Decoder
    return the Message in English
    Examples:
        Message_in_Morse_Code is
        '.... . .-.. .-.. ---,.--. -.-- - .... --- -.,...-- .-.-.- -....'
        It is transformed/decoded to Message 'hello python 3#6' in English
    '''
    if Character_Decoder == None:
        Character_Decoder = Build_Character_Decoder()
    # add your code from here
    coded = (Message_in_Morse_Code).split(',')
    uncoded = []
    
    for i in range(len(coded)):
        uncoded.append(Word_Decoder(coded[i], Character_Decoder))
    
    Message = uncoded[0]
    
    for s in uncoded[1:]:
        Message += ' ' + s
    

    return Message
# %% you do not need to modify this function
def Make_Sound(Message_in_Morse_Code):
    '''
    a bonus function to hear the sound of Morse Code
    It only works on Windows
    there is not linuxsound or macsound ...
    '''
    import winsound
    import time
    frequence = 600
    duration = 200
    for code in Message_in_Morse_Code:
        if code == '.':
            # A dot is 1 time unit.
            winsound.Beep(frequence, duration)
            #pause 1 time unit
            #time.sleep(duration/1000)
        elif code == '-':
            # A dash is 3 time units.
            winsound.Beep(frequence, 3*duration)
            #pause 1 time unit
            #time.sleep(duration/1000)
        elif code == ' ':
            #The space between letters is 3 time units.
            time.sleep(0.5*3*duration/1000)
        elif code == ',':
            # The space between words is 7 time units.
            time.sleep(0.5*7*duration/1000)
        else: # unknown character '#'
            winsound.Beep(2*frequence, 3*duration)
# %% you do not need to modify this function
def Send_Message(play_sound = False):
    '''
    a bonus function to send an 'encrypted' message (Morse Code)
    to your friends/parents via gmail
    Message could be Meet me in the restaurant at 6 PM tomorrow
    set play_sound to True if you want to hear it
    Note:
        you may receive a 'Security alert' email from google
        go to https://myaccount.google.com/lesssecureapps
        turn 'Allow less secure apps: ON'
        Then you can send an email using this function
        turn 'Allow less secure apps: OFF' after you test this function
    '''
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # input some information
    email_address_source = input('your gmail address:')
    password = input('passward of your gmail account:')
    email_address_destination = input('send the email to:')
    Subject =input('subject of the email:')
    Message = input('the message:')
    #encrypt the Message using MorseCode
    Message_in_Morse_Code = Message_Encoder(Message)
    # set up the SMTP server
    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp.starttls()
    smtp.login(email_address_source, password)
    # compose the email:
    email = MIMEMultipart()
    email['From'] = email_address_source
    email['To'] = email_address_destination
    email['Subject']= Subject
    email.attach(MIMEText(Message_in_Morse_Code, 'plain'))
    # send the email
    smtp.send_message(email)
    # Terminate the SMTP session and close the connection
    smtp.quit()
    #
    if play_sound == True:
        Make_Sound(Message_in_Morse_Code)
    print('the message is encrypted and sent:')
    print(Message_in_Morse_Code)
    print('the original message is:')
    print(Message)
