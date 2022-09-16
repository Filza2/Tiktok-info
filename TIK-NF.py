try:import re;from colorama import Fore;from requests import get
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
print("""
████████╗██╗██╗  ██╗     ███╗   ██╗███████╗
╚══██╔══╝██║██║ ██╔╝     ████╗  ██║██╔════╝
   ██║   ██║█████╔╝█████╗██╔██╗ ██║█████╗  
   ██║   ██║██╔═██╗╚════╝██║╚██╗██║██╔══╝  
   ██║   ██║██║  ██╗     ██║ ╚████║██║     
   ╚═╝   ╚═╝╚═╝  ╚═╝     ╚═╝  ╚═══╝╚═╝                                                              
          By @TweakPY - @vv1ck
""")
user=input(f'[{Fore.RED}?{Fore.WHITE}] Enter The user : ');print('\n')
rdu=get(f"https://tokcount.com/?user={user}",headers={'Host': 'tokcount.com','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Cache-Control': 'max-age=0','Te': 'trailers'})
if 'undefined' in re.findall('<title>(.*?)</title>',rdu.text)[0]:exit(f'[!] user Not Found ! , {user}')
elif 'false' in re.findall('"success":(.*?),',rdu.text)[0]:exit(f'[!] user Not Found ! , {user}')
elif 'true' in re.findall('"success":(.*?),',rdu.text)[0]:
    print(f'[{Fore.RED}+{Fore.WHITE}] user id : ',re.findall('"userId":"(.*?)",',rdu.text)[0])
    print(f'[{Fore.RED}+{Fore.WHITE}] verified : ',re.findall('"verified":(.*?),',rdu.text)[0])
    print(f'[{Fore.RED}+{Fore.WHITE}] username : ',re.findall('"username":"(.*?)",',rdu.text)[0])
    print(f'[{Fore.RED}+{Fore.WHITE}] Likes : ',re.findall('"likeCount":(.*?),',rdu.text)[0])    
    print(f'[{Fore.RED}+{Fore.WHITE}] Followers : ',re.findall('"followerCount":(.*?),',rdu.text)[0])
    print(f'[{Fore.RED}+{Fore.WHITE}] Following : ',re.findall('"followingCount":(.*?),',rdu.text)[0])
    print(f'[{Fore.RED}+{Fore.WHITE}] Video Count : ',re.findall('"videoCount":(.*?)},',rdu.text)[0])
else:exit('[!] Error !! ')
