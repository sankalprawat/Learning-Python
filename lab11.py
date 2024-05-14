import sys
import os


def main(): #main method
 try:
  f1 = open(sys.argv[1], 'r')         #takes the first input file in command line

  user_input1 = (sys.argv[3])    #takes the word which is to be excluded.
  user_input2 = (sys.argv[4])    #takes the word which is to be included.
  if sys.argv[1] == sys.argv[2]:

       sys.exit('\nERROR!!\nThe two file names cannot be the same.')

  if sys.argv[3] != sys.argv[4]:

    for line in f1:
         if user_input2 or user_input1 in line:

           f2 = open(sys.argv[2], 'a')

           if user_input1 in line:
              if user_input2 in line:
                   pass

           elif user_input2 in line:
              f2.write(line)

         else:
          sys.exit('\nOne of the words or both of them does not exist.')


  if sys.argv[3] == sys.argv[4]:

         sys.exit('\nERROR!!\nThe word to be excluded and the word to be included     cannot be the same.')



 except IOError:
       print('\nIO error or wrong file name.')
 except IndexError:
       print('\nYou must enter 5 parameters.')
 except SystemExit as e:
       sys.exit(e)


if __name__ == '__main__':
  main()