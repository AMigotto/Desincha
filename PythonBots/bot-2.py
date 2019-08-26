import instaloader


account = instaloader.Instaloader()


account.login('paarthur_', 'nevermind123')        



profile = instaloader.Profile.from_username(account.context, "casadesincha")




#Create a counter for lupping
follow_list = []
count=0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("desincha_seguidores.txt","a+")
    file.write(follow_list[count] + "\n")
    file.close()
    print(follow_list[count])
    count = count + 1
