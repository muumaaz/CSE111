#3
def remail(mail, newDomain, oldDomain):
    user, domain = mail.split('@')
    new_domain = '@' + newDomain
    new_mail = user + new_domain
    print(new_mail)

remail('alice@kaaj.com', 'sheba.xyz', 'kaaj.com')
