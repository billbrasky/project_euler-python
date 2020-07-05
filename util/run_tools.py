import sys, re
import os, importlib
import time, glob

from typing import Tuple, Union, List, Dict


class ProjectEuler():

    def __init__( self, test_path: [str, None] = None, test: [str, None] = None ) -> None:

        self.test_path = test_path
        self.test = test
        # self.test = re.search( r'[\\/](\d{3})\.py', test_path ).groups(1)[0]
        self.my_answer = None
        self.answer = None
        self.passed = None
        self.duration = None


    # Checks if provided test is numeric 1 to 3 digits
    #
    def validateTest( self ) -> bool:

        if re.match( r'\d{1,3}', self.test ) is None:
            print( f'The problem number {self.test} is not a suitable option.' )
            print( 'Try a natural number.' )
            return False

        return True

    # Pads the test on the left to be 3 digits
    #   
    def padTestPath( self ) -> None:

        while len( self.test ) != 3:
            self.test = '0' + self.test

    # Processes a test to compare its solution to the answers.
    # 
    def processTest( self ):
        if self.my_answer == self.answer:
            self.passed = True
 
        else:
            self.passed = False

    def getAnswer( self, answers: Dict ):

        self.answer = answers[self.test]

    # Executes the script at a specific path
    #
    def getMyAnswer( self ) -> None:

        if '/' in self.test_path:
            importpath = self.test_path.replace( '/', '.' )[:-3]
        else:
            importpath = self.test_path.replace( '\\', '.' )[:-3]

        if os.path.exists( self.test_path ):
            module = importlib.import_module( importpath )

            start = time.time()
            try:
                self.my_answer = str( module.run())
                self.duration = time.time() - start
            
            except:
                self.my_answer = 'FAILURE'
                self.duration = None

        else:

            print( f'The path {self.test_path} could not be found.' )




def log( test: str, completed: bool, passed: bool, time: float, start_time: float ) -> None:

    log_path = './log/'

    if not os.path.exists( log_path ):
        os.mkdir( log_path )

    log_path += f'{start_time}.txt'

    if not os.path.exists( log_path ):
        with open( log_path, 'w' ) as f:

            f.write( 'Problem\t\tCompleted\t\tPass\t\ttime\n' )

    with open( log_path, 'a' ) as f:
        f.write( f'{test}\t\t\t{completed}\t\t{passed}\t\t{time}\n' )

# Gets all of the answers from a provided file
#
def getAnswers():
    answers = {}

    with open( 'data/answers.txt', newline = '' ) as f:
        for line in f:
            m = re.search( r'Problem (\d{3}): (.*)', line )

            problem = m.group(1)
            answer = m.group(2)

            answers[problem] = answer.strip()
    return answers        