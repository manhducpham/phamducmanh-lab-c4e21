from gmail import GMail, Message
import datetime

mail = GMail("c4e21.pdm.test", "CodeTheChange123")
body = '''
<p>Dear&nbsp;Mr. Huy Quang Nguyen,</p>
<p>I won&rsquo;t be able to report to work today because I&rsquo;m under the weather and have a&nbsp;headache. I went to the emergency room last night and the doctor confirmed that I've got doctor&rsquo;s diagnosis.</p>
<p>The doctor prescribed&nbsp;1 day off from work&nbsp;as I&nbsp;need to rest, so I asked&nbsp;Mr. Nam&nbsp;to take over my meeting with&nbsp;Mr. Quan&nbsp;this afternoon. They'll also handle my pending tasks while I'm away. I'll be available via email for your urgent needs.</p>
<p>I&rsquo;ve also attached the doctor&rsquo;s note to this email. I'd appreciate it if you would forward this email with the attachment to HR so they can process my sick leave. Thank you for your help.</p>
<p>Regards,</p>
<p>&nbsp;</p>
<p>Manh Duc Pham</p>
'''
msg = Message("Manh Duc Pham - Sick day", to = 'manhadhvnh@gmail.com', html = body)

now = datetime.datetime.now()
while True:
    if now.hour == 7:
        mail.send(msg)
        print('sent')
        break