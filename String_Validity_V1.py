# For the purposes of this problem, a “valid” sentence is defined as:
#1 String starts with a capital letter
#2 String has an even number of quotation marks
#3 String ends with a period character “."
#4 String has no period characters other than the last character 
#5 Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)

from enums.Test import Test
import json
from tests.initialcapitalcheck import initialcapitalcheck
from tests.evenquotescheck import evenquotescheck
from tests.ultimateperiodcheck import ultimateperiodcheck
from tests.multiperiods import multiperiods
from tests.spelloutnumbers import spelloutnumbers

wordlength = 0
strusertest = ''

def checkvalidity(testphrase,testnumbers):
    # Accepts a test phrase, and an array of tests to perform, returns in JSON
    results = {}
    results['Test Sentence'] = testphrase
    overallpass = True
    for testnum in testnumbers:
        if testnum == Test.INITIALCAPITALCHECK.value:
            results['Initial Capital Check'] = initialcapitalcheck(testphrase)
        elif testnum == Test.EVENQUOTESCHECK.value:
            results['Even Quotes Check'] = evenquotescheck(testphrase)
        elif testnum == Test.ULTIMATEPERIODCHECK.value:
            results['Ends with a Period Check'] = ultimateperiodcheck(testphrase, wordlength)
        elif testnum == Test.MULTIPERIODSCHECK.value:
            results['Contains Multiple Periods Check'] = multiperiods(testphrase,wordlength)
        elif testnum == Test.SPELLOUTNUMBERSCHECK.value:
            results['Numbers Spelled Out Check'] = spelloutnumbers(testphrase)
    
    # Add an overall result
    for key in results:
        if results[key] == False:
            overallpass = False
            break
    results['Valid Sentence'] = overallpass
  
    resultoutput = json.dumps(results, indent=4, sort_keys=True)
    return resultoutput


def obtainparams():
    # Gather parameters from user and sanitise
    # Function will either return false or a list of valid parameters
    try:
        strparamsinput =  input('Enter tests to perform, numbers above seperated by commas (blank for all tests): ')

        if not strparamsinput.strip():
            arruserparams = [1,2,3,4,5]
        else:
            # Return a list of integers, removing duplicates
            arruserparams = list(
                                dict.fromkeys(
                                    map(int, strparamsinput.split(','))
                                )           
                            )
        for param in arruserparams:
            if param < 1 or param > 5:
                print('Please enter valid test numbers (1 - 5)')
                return False

        return arruserparams
    
    except ValueError:
        print('Please enter a full list')

def printrules():
    # Print out list of rules upon opening
    print(  '***Valid Sentence Coding Test*** \n'\
        'Type exit to quit \n'\
        'Tests: \n'\
        '1) String starts with a capital letter \n'\
        '2) String has an even number of quotation marks \n'\
        '3) String ends with a period character “."  \n'\
        '4) String has no period characters other than the last character  \n'\
        '5) Numbers below 13 are spelled out')

def main():
    printrules()
    run = True
    while run:
        try:
            strusertest = input('Enter a test phrase: ')
            userparams = False

            
            # Exit the program
            if (strusertest.upper() == 'EXIT'):
                print('Exiting...')
                run = False
                break
            
            # Run tests
            else:
                while not userparams:
                    userparams = obtainparams()

                wordlength = len(strusertest)
                print(checkvalidity(strusertest, userparams))
                strusertest = ''

        # Clean close if user escapes
        except EOFError:
                print('Exiting...')
                run = False


if __name__ == '__main__':
    main()

