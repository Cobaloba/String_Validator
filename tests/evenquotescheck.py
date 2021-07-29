#2 Check even number of quotes
def evenquotescheck(testword):
    # Sanitise input
    testword = testword.replace('“','"')
    testword = testword.replace('”','"')

    quotecount = testword.count('"')
    return not bool(quotecount % 2)