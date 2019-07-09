#! pyhton3

import re,pyperclip

#TODO : create a regex for phone number

phoneRegex = re.compile(r'''
# 444-444-4444, 555-5555, (444) 555-5555, 555-5555 ext 12345, ext. 12345, x12345
(
((/d/d/d)|(/(/d/d/d/)))?        #area code (optional)
(/s|-)                          #separator
(/d/d/d)                        #first part
-                               #seperator
(/d/d/d/d)                      #second half
(ext(/.)?\s|x)                  #extension word part (optional)
(/d{2,5})                       #extension number part (optional)

)
    
''',re.VERBOSE)


#TODO: create a regex for email id

emailRegex = re.compile(r'''
#something.something@something.com

[a-zA-Z0-9_.+]+                #name part
@                              #symbol
[a-zA-Z0-9_.+]+                #domain name google-chrome-stable_current_amd64.deb

''',re.VERBOSE)

#TODO : get the text from the clipboard
text=pyperclip.paste()

#TODO : get the phone numbers and emailid from the text
extractedPhoneNumbers = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhoneNumbers)
print(extractedEmail)



allPhoneNumbers=[]
for phoneNumber in extractedPhoneNumbers
    allPhoneNumbers.append(phoneNumber(0))

#TODO: copy the extracted data to the clipboard

results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)

pyperclip.copy(results)

