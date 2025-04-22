import sys
import os

#help(os.environ)

class Learn:
    def study(chapter):
        print("Today i learnt chapter",chapter)

    def Revision(chapter):
        print("Today i revised chapter",chapter)

    def play(sport):
         print("Today i played ",sport)



if __name__== "__main__":

    chapter=input("what chapter did you study today")
    rev=input("what chapter you revised today")
    sport=input("what sport did you play today")


    Learn.study(chapter=chapter)
    Learn.Revision(chapter=rev)
    Learn.play(sport=sport)
