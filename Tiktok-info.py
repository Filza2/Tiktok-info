from rich.console import Console
from requests import get
import re,os

console=Console()

def header():
    os.system('cls' if os.name=='nt' else 'clear');console.print("""
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗     ██╗███╗   ██╗███████╗ ██████╗ 
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝     ██║████╗  ██║██╔════╝██╔═══██╗
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ██║██║ ╚████║██║     ╚██████╔╝
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                                                             
                            By @TweakPY - @vv1ck
""")

def tiktok_info2(user):
    try:
        r=get(f"https://tiktok.livecounts.io/user/search/{user}",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Origin': 'https://livecounts.io'})
        if '"success":true' in r.text:
            console.print(f"""- Name : [bold red]{re.findall('"username":"(.*?)",',r.text)[0]}[/bold red]
- Bio : [bold red]{re.findall('"signature":"(.*?)",',r.text)[0]}[/bold red]
- userID : [bold red]{re.findall('"userId":"(.*?)",',r.text)[0]}[/bold red]
- Verified : [bold red]{re.findall('"verified":(.*?),',r.text)[0]}[/bold red]
- Followers : [bold red]{re.findall('"followers":(.*?),',r.text)[0]}[/bold red]
- Following : [bold red]{re.findall('"following":(.*?),',r.text)[0]}[/bold red]
- Likes : [bold red]{re.findall('"likes":(.*?),',r.text)[0]}[/bold red]
- Video : [bold red]{re.findall('"videos":(.*?)}}',r.text)[0]}[/bold red]
- Profile Pic URL : [bold red]{re.findall('"avatar":"(.*?)",',r.text)[0]}[/bold red]""")
        else:console.print(f"- [bold red]Error[/bold red], [bold red]Can't Get {user} info[/bold red] ! ");exit()
    except Exception as e:console.print(f"- [bold red]Error[/bold red], [bold red]Can't Get {user} info[/bold red] ! ");exit()
    
def tiktok_info():
    try:
        header()
        user=input(f'- Enter The user : ').strip();header()
        r=get(f"https://tokcount.com/?user={user}",headers={'Host': 'tokcount.com','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Te': 'trailers'})
        if 'undefined' in re.findall('<title>(.*?)</title>',r.text)[0]:tiktok_info2(user)
        elif 'false' in re.findall('"success":(.*?),',r.text)[0]:tiktok_info2(user)
        elif 'true' in re.findall('"success":(.*?),',r.text)[0]:
            console.print(f"""- userID : [bold red]{re.findall('"userId":"(.*?)",',r.text)[0]}[/bold red]
- Verified : [bold red]{re.findall('"verified":(.*?),',r.text)[0]}[/bold red]
- Name : [bold red]{re.findall('"username":"(.*?)",',r.text)[0]}[/bold red]
- Likes : [bold red]{re.findall('"likes":(.*?),',r.text)[0]}[/bold red]    
- Followers : [bold red]{re.findall('"followers":(.*?),',r.text)[0]}[/bold red]
- Following : [bold red]{re.findall('"following":(.*?),',r.text)[0]}[/bold red]
- Video Count : [bold red]{re.findall('"videos":(.*?)}},',r.text)[0]}[/bold red]""")
        else:tiktok_info2(user)
    except Exception as e:tiktok_info2(user)
    
    
    
tiktok_info()
