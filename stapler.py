# Code Submission
# Alyssa Lee
# This header is a sample (this is the optional description)
# Files in submission: 
# - stapler.py
# ============================ #
########## stapler.py ##########

import glob

def main():
  files = glob.glob('folder/*.py') #Replace with your own glob
  submission = open('submission.txt', 'w') #The file to write to
  # (Creates a new file if it doesn't exist)

  #This part creates a header for your .txt file
  title = 'Code Submission Week 1' #your title here
  author = 'Alyssa Lee' #your name here
  description = '' #optional (possibly write collaborators here)
  submission.write(makeHeader(title, author, description, files))

  for filename in files:
    f = open(filename)
    submission.write('\n\n\n########## ' + filename + ' ##########\n\n')
    submission.write(f.read())
    f.close()

  submission.close()
  print('Submission created.')
    
def makeHeader(title, author, description, files):
  header = '# ' + title + '\n' + '# ' + author + '\n'
  if description != '':
    header += '# ' + description + '\n'
  header += '# Files in submission: \n# - ' + '\n# - '.join(files) + '\n'
  header += '# ============================ #\n'
  return header


if __name__ == '__main__':
  main()