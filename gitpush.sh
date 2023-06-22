

#! /bin/sh
#
# Prompt for user input
read -p "Please enter a message: " message

# Check the answer
if [ "$message" = "First Commit" ]; then
  echo "The message is correct!"
else
  echo "The message is incorrect."
fi

read message

git add * 
git commit -m "${message}"
if [-n "$(git status - porcelain)"];
then
	echo "IT's CLEAN"
else
	git status
	echo "Pushing data to remote server!!!"
	git push 
fi

