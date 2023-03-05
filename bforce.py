import string
import whois

ALLOWED_CHARACTERS = string.ascii_lowercase + string.digits + "öäüØÅÆ" # + "-"
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)
MAX_LENGTH = 3
TLDS = ["de", "com"]

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) == 0:
            return list(string[0]) + next(string[1:])
    return string

def is_not_registered(site):
    """Check if a domain has an WHOIS record."""
    try: 
        details = whois.whois(site)
        return False
    except:
        return True
    

def check_domain(domain):
    if is_not_registered(domain):
        return True
    return False

def save_domain(domain):
    name, tld = domain.split(".")
    open(f"{tld}.txt", "a").write(f"{domain}\n")

def clear_domain_files():
    for tld in TLDS:
        open(f"{tld}.txt", "w").write("")

def main():
    # clear_domain_files()
    sequence = list()
    while not len(sequence) > MAX_LENGTH:
        sequence = next(sequence)
        for tld in TLDS:
            domain = ''.join(sequence) + "." + tld
            if check_domain(domain):
                save_domain(domain)

if __name__ == "__main__":
    main()
