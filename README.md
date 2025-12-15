# SSH-To-MINITEL

Passerelle **Minitel ⇄ SSH** écrite en **Python**, utilisant **WebSocket** pour interconnecter un **Minitel réel (Magis Club, Minitel 1B, etc.)** avec un **serveur SSH moderne**, tout en respectant les contraintes historiques du **VIDEOTEX**.

Ce projet permet d'utiliser un Minitel comme **terminal interactif** pour accéder à un shell Unix distant (`bash`, `vi`, `mc`, etc.).

---

## Fonctionnalités

* Compatibilité **Minitel réel** (M1 / M1B / Magis Club)
* Connexion à un **serveur SSH réseau**
* Passerelle **WebSocket** (client web ou frontal série)
* Utilisation correcte de **terminfo Minitel (`mntl.ti`)**
* Gestion des touches Minitel (ENVOI, RETOUR, etc.)
* Mode texte **40 colonnes Videotex**
* Sans Unicode (ISO-8859-1 / `LANG=C`)
* Testé sur Débian 13 et MagisClus à 9600 Bauds

---

## Architecture

```text
[Minitel réel]
   │  (VIDEOTEX / Série / TCP)
   ▼
[Client WebSocket]
   ▼
[Serveur Python SSHMINITEL]
   ├─ WebSocket
   ├─ Paramiko (SSH)
   ├─ Mapping clavier Minitel
   ▼
[Serveur SSH distant]
```

---

##  Prérequis

### Serveur passerelle (Python)

* Python ≥ 3.10
* `paramiko`
* `websockets`
## Récupération du projet (git clone)

Depuis une machine disposant de Git :

```sh
git clone https://github.com/labbej27/sshminitel.git
cd sshminitel
```
Création d’un environnement virtuel Python (recommandé) :

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Serveur SSH distant

* Linux / Unix
* `ncurses`
* Installation du terminfo Minitel (`mntl.ti`)

---

## Installation du terminfo Minitel (OBLIGATOIRE)

Sur le **serveur SSH** :

```sh
sudo adduser minitel #Création d'un utilisateur dédié au minitel
nano /home/minitel/.profile
#ajouter à la fin :
export TERM=m1b
export LANG=C
stty -ixon icrnl onlcr -echo
#puis sauvegarder ctrl-o puis ctrl-x
```
Pourquoi ?
* TERM=m1b → compatibilité Minitel (vous pouvez choisir d'autres minitels comme )
* LANG=C → pas d'UTF-8
* icrnl → ENVOI = Entrée
* -echo → évite les caractères en double
  
## Se loguer en user minitel :

```sh
wget http://canal.chez.com/mntl.ti
tic -x mntl.ti 
infocmp m1b
```
doit afficher :
```sh
#	Reconstructed via infocmp from file: /home/minitel/.terminfo/m/m1b
m1b|minitel 1-bistandard (in 40cols mode),
	am, bw, eslok, hs, hz, mir,
	colors#8, cols#40, lines#24, pairs#8,
	acsc=0\177j+k+l+m+n+o~q`s_t+u+v+w+x|, bel=^G,
	blink=\EH, civis=^T, clear=^L, cnorm=^Q, cr=\r,
	cub=\E[%p1%dD, cub1=^H, cud=\E[%p1%dB, cud1=\n,
	cuf=\E[%p1%dC, cuf1=^I, cup=\037%p1%'A'%+%c%p2%'A'%+%c,
	cuu=\E[%p1%dA, cuu1=^K, dch=\E[%p1%dP, dch1=\E[P,
	dl=\E[%p1%dM, dl1=\E[M, dsl=\037@A\030\n, ed=\E[J, el=^X,
	el1=\E[1K, flash=\037@A\EW \177\022\177\022P\r\030\n,
	fsl=\n, home=^^, il=\E[%p1%dL, il1=\E[L, ind=\n,
	iprog=stty -ixon, is1=\E:dS\E;iYA\E;jYC,
	is2=\E;`ZQ\E:iC\E:iE\021, kbs@, kcan@, kclr=\E[2J,
	kcub1=\E[D, kcud1=\E[B, kcuf1=\E[C, kcuu1=\E[A, kdch1=\E[P,
	kdl1=\E[M, kend=^SI, kent@, kf1=^SD, kf10=^Y0, kf11=^Y1,
	kf12=^Y/, kf13=^Y{1, kf14=^Y{2, kf15=^Y{3, kf16=^Y{4,
	kf17=^Y{5, kf18=^Y{6, kf19=^Y{7, kf2=^SC, kf20=^Y{8,
	kf21=^Y{9, kf22=^Y{0, kf23=^Y{*, kf24=^Y{#, kf3=^SF, kf4=^SA,
	kf5=^SG, kf6=^SE, kf7=^Y8, kf8=^Y\,, kf9=^Y., khlp@,
	khome=\E[H, kich1=\E[4h, kil1=\E[L, knp=^SH, kpp=^SB, krfr@,
	lf1=Guide, lf10=Ctrl+0, lf2=Repetition, lf3=Sommaire,
	lf4=Envoi, lf5=Correction, lf6=Annulation, lf7=Ctrl+7,
	lf8=Ctrl+8, lf9=Ctrl+9, mc0@, mc4=\E;`[R, mc5=\E;a[R,
	nel=\r\n, op=\EG, rep=%p1%c\022%p2%'?'%+%c, rev=\E], ri=^K,
	rmir=\E[4l, rmso=\E\\, rs1=\E[4l,
	rs2=\024\037XA\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\n\030\014\021,
	setab=\0, setaf=\E%p1%'@'%+%c, setb=\0,
	setf=\E%?%p1%{1}%=%tD%e%p1%{3}%=%tF%e%p1%{4}%=%tA%e%p1%{6}%=%tC%e%p1%'@'%+%c%;,
	sgr=%?%p1%t\E]%;%?%p3%t\E]%;%?%p4%t\EH%;,
	sgr0=\EI\E\\\EG, smir=\E[4h, smso=\E],
	tsl=\037@%p1%'A'%+%c, u6=\037%c%'A'%-%c%'A'%-, u7=\Ea,
	u8=\001%[ABCPtuvwxyz0123456789:;<=>?]\004, u9=\E9{,
```

#### Tester :
```sh
echo $TERM 
```
##### Doit afficher : m1b
---

## Configuration du compte SSH

Dans `~/.profile` de l'utilisateur SSH :

```sh
export TERM=m1b
export LANG=C
stty -ixon icrnl onlcr -echo
```

### Pourquoi ?

* `TERM=m1b` → compatibilité Minitel
* `LANG=C` → pas d'UTF-8
* `icrnl` → ENVOI = Entrée
* `-echo` → évite les caractères en double
#### Vous pouvez choisir un autre terminal minitel visitez http://canal.chez.com/terminfo.htm
---

## Lancement du serveur

```sh
python3 sshwebsocket.py
```

Sortie attendue :

```text
Passerelle SSH–Minitel prête
```
---

## Connexion du Minitel au Websocket
Via usb/serial vers péri-info
utiliser par exemple :
https://github.com/labbej27/websocket-minitel

---

## Problèmes connus & solutions

### Touches en double

Cause : double écho
Solution : `stty -echo` (déjà inclus plus haut)

---

### Le caractère `@` devient `à`

Mauvais mode de terminal sur le Minitel ( fnct T puis A ou ctrl-esc puis T puis A sur magisclub)
## Licence

Ce projet est libre d'utilisation, de modification et de redistribution à des fins non commerciales.

Toute utilisation commerciale est interdite sans autorisation explicite de l'auteur.

Ce projet a été développé à des fins personnelles et éducatives, en s’inspirant de projets existants de la communauté Minitel.

---

## Crédits
http://canal.chez.com/terminfo.htm

---

> *"Faire dialoguer le Minitel avec l'Internet moderne."*
