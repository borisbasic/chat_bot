from bardapi import Bard
token = 'cwj2-R1FjXBKg592ZGnNTrIscExO5qBzGIEd8aixRdArNUR1CHBc-vFZ-tUk6_SYcctYoQ.'
bard = Bard(token_from_browser=True)
print(bard.get_answer("daj mi kazi nesto o ruzama")['content'])