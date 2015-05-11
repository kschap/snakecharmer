# Snake Charmer, version 0.6.
import tweepy
from geopy.geocoders import GoogleV3
consumer_key = ''

Initializes API.
consumer_secret = ''
token_key = ''
token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

# Retrieves current user's timeline.
def timeline():
	timeline = api.home_timeline()
	for result in timeline:
		print result.text
	mainMenu()

# Searches Twitter for either a term or a hashtag.
def search():
	print "\nWhat would you like to look up?"
	search = raw_input("Search: ")
	search = api.search(q=search)
	for result in search:
		print result.text
	mainMenu()

# Creates a prompt for the user to spoof their location.
def waldo():
	tweet = raw_input("\nWhat's on your mind? ")
	location = raw_input("\nWhere would you like to tweet from? ")
	#Now, to determine the latitude and longitude of the location, we use geopy.
	engine = GoogleV3()
	location = engine.geocode(location)
	lat = location.latitude
	longitude = location.longitude
	# Now, we take these three bits of information and mix them all up...
	api.update_status(status=tweet, lat=lat, long=longitude)
	mainMenu()

# Allows for a user to reply to somebody's tweet.
def reply():
	tweetId = input("What is the tweet number of the tweet you wish to respond to? ")
	user = raw_input("What is that user's username? ")
	tweet = raw_input("What do you want to say to them? ")
	api.update_status(status="@" + user + " " + tweet, in_reply_to_status_id=tweetId)
	mainMenu()

# Tweets from the current user's account.
def tweet():
	print "Choose an option:\n"
	print "1. Tweet normally"
	print "2. Tweet while spoofing a location"
	print "3. Respond to a user's tweet"
	print "4. Go back to the main menu"
	option = input("Choose an option: ")
	if option == 1:
		tweet = raw_input("\nWhat's on your mind? ")
		api.update_status(tweet)
		mainMenu()
	elif option == 2:
		waldo()
	elif option == 3:
		reply()
	elif option == 4:
		mainMenu()
	else:
		print "\nYou screwed up! Try again!"
		tweet()

# Searches for a screen name and prints latest tweets from them.
def stalk():
	user = raw_input("\nWho do you want to stalk? ")
	user = api.user_timeline(user)
	for result in user:
		print result.text
	mainMenu()

# Direct messaging. It should work, the app is authorized for it...
def direct():
	user = raw_input("\nWho do you want to DM? ")
	message = raw_input("What do you want to say? ")
	api.send_direct_message(user=user, text=message)
	mainMenu()

# Bio display to change name.
def bio_name():
	newname = raw_input("\nWhat do you want your new name to be? ")
	api.update_profile(name=newname)
	mainMenu()

# Bio display to change web address.
def bio_web():
	newweb = raw_input("\nWhat is your new web address? ")
	api.update_profile(url=newweb)
	mainMenu()

# Bio display to change location.
def bio_location():
	newlocation = raw_input("\nWhere do you want to be? ")
	api.update_profile(location=newlocation)
	mainMenu()

# Bio display to change, well, the actual bio.
def bio_bio():
	newbio = raw_input("\nWhat do you want your new bio to say? ")
	api.update_profile(bio=newbio)
	mainMenu()

# Main bio menu for authenticated user.
def bio_main():
	print "\nWhat do you want to change about your bio?"
	print "1. Name"
	print "2. Web address"
	print "3. Location"
	print "4. Bio"
	print "5. Go back to main menu"
	option = input("Select an option: ")
	if option == 1:
		bio_name()
	elif option == 2:
		bio_web()
	elif option == 3:
		bio_location()
	elif option == 4:
		bio_bio()
	elif option == 5:
		mainMenu()
	else:
		print "\nYou screwed up! Try again!"
		bio_main()

# Checks for direct messages.
def checkdm():
	dm = api.direct_messages()
	for result in dm:
		print result.text
	mainMenu()

# Searches for people
def peopleFind():
	query = raw_input("What is the name of the person you want to find? ")
	search = api.search_users(query)
	for result in search:
		print result.text
	mainMenu()

# Main menu (duh...)
def mainMenu():
	print "\nSnake Charmer, version 0.6"
	user = api.me()
	print "Tweeting as: @" + user.screen_name + " | " + user.name
	print "Make a selection"
	print "1. Get timeline"
	print "2. Search Twitter"
	print "3. Tweet something"
	print "4. Stalk somebody"
	print "5. Direct message somebody"
	print "6. Change bio"
	print "7. Check direct messages"
	print "8. Find somebody"
	option = input("Your choice: ")
	if option == 1:
		timeline()
	if option == 2:
		search()
	elif option == 3:
		tweet()
	elif option == 4:
		stalk()
	elif option == 5:
		direct()
	elif option == 6:
		bio_main()
	elif option == 7:
		checkdm()
	elif option == 8:
		peopleFind()
	else:
		print "\nYou screwed up! Try again!"
		mainMenu()

mainMenu()
