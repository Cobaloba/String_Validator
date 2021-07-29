# 4) String has no period characters other than the last character 
def multiperiods(testword, wordlength):
    periods = True
    # Check each character except last
    for chars in testword[:wordlength -1]:
        if chars == ".":
            periods = False
            break
    return periods