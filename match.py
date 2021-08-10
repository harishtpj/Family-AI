from fuzzywuzzy import fuzz

def dobmatch(statement): # Match for Finding DOB
    statement = statement.lower()
    rate = fuzz.token_set_ratio("when born",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("born on",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("birth date of",statement)
    return rate

def pobmatch(statement): # Match for Finding POB
    statement = statement.lower()
    rate = fuzz.token_set_ratio("where born",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("born in",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("which area born",statement)
    return rate

def nativematch(statement): # Match for Finding Native
    statement = statement.lower()
    rate = fuzz.token_set_ratio("native of",statement)
    if rate !=100:
        rate = fuzz.token_set_ratio("native",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("which area native",statement)
    return rate

def parentmatch(statement): # Match for Finding Parents
    statement = statement.lower()
    rate = fuzz.token_set_ratio("parents of",statement)
    if rate !=100:
        rate = fuzz.token_set_ratio("parents",statement)
    return rate

def fathermatch(statement): # Match for Finding Father
    statement = statement.lower()
    rate = fuzz.token_set_ratio("father of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who is dad",statement)
    if rate !=100:
        rate = fuzz.token_set_ratio("father",statement)
    return rate

def mothermatch(statement): # Match for Finding Mother
    statement = statement.lower()
    rate = fuzz.token_set_ratio("mother of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who is mom",statement)
    if rate !=100:
        rate = fuzz.token_set_ratio("mother",statement)
    return rate

def jobmatch(statement): # Match for Finding Job
    statement = statement.lower()
    rate = fuzz.token_set_ratio("what was doing",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("work of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("job of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("job",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("what is doing",statement)
    return rate

def biomatch(statement): # Match for finding Bio-data
    statement = statement.lower()
    rate = fuzz.token_set_ratio("who is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("bio data",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("bio-data",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("biodata",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("about",statement)
    if rate != 100:
         rate = fuzz.token_set_ratio("details",statement)
    return rate

def whopbirth(statement): # Match for finding who born place
    statement = statement.lower()
    rate = fuzz.token_set_ratio("who born in ",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose birth place is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whom birth place is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who birth place is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who born on",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who born at",statement)
    return rate

def whojob(statement): # Match for finding who job
    statement = statement.lower()
    rate = fuzz.token_set_ratio("who is a",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose job is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose is at",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose work to",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who work is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who is on",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who work of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who is working at",statement)
    return rate

def whonative(statement): # Match for finding who native
    statement = statement.lower()
    rate = fuzz.token_set_ratio("who native in ",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose native is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose native at",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whose native on",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("whom native is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who native is",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who native on",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who native of",statement)
    if rate != 100:
        rate = fuzz.token_set_ratio("who native at",statement)
    return rate
