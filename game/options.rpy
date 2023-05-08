## Questo file contiene opzioni che possono venire cambiate per personalizzare
## il gioco.
##
## Le linee che cominciano con due '#' sono commenti e non dovresti modificarle.
## Le linee con un solo '#' sono linee di codice opzionali, e potresti volerle
## modificare se appropriato.


## Fondamentali ################################################################

## Il nome del gioco in forma leggibile. E' usato per il titolo nella finestra e
## viene impiegato per i resoconti di errore e nell'interfaccia.
##
## La notazione _() che racchiude la stringa la segna come testo traducibile.

define config.name = _("Snake")


## Determina se il titolo fornito più sopra è mostrato nel main menu. Imposta su
## 'False' per nascondere il titolo.

define gui.show_name = True


## La versione del gioco.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## Un nome abbreviato impiegato dagli eseguibili e dalle cartelle nelle
## distribuzioni compilate. Deve contenere solo caratteri ASCII e non può
## contenere spazi, due punti, o punti e virgole.

define build.name = "Snake"


## Suoni e musica ##############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Per consentire al giocatore di eseguire un test sonoro sui canali Suono o
## Voce, togli # dalla linea e usala per impostare un suono di esempio.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Togli # dalla linea seguente per impostare un file audio che sarà riprodotto
## durante il main menu. Continuerà a suonare fino a che non verrà interrotto o
## un altro file audio verrà suonato.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transizioni #################################################################
##
## Queste variabili impostano le transizioni che sono usate quando avvengono
## certi eventi. Ogni variabile deve essere impostata su una transizione, o su
## None per indicare che nessuna transizione deve venire usata.

## Entrare o uscire dal game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## Transizione usata dopo che una partita viene caricata.

define config.after_load_transition = None


## Usata quando si torna al main menu dopo che è finita una partita.

define config.end_game_transition = None


## Non esiste una variabile per impostare la transizione da usare quando inizia
## il gioco. Usa un comando 'with' subito dopo aver mostrato la prima 'scene'.


## Gestione finestra ###########################################################
##
## Controlla come viene mostrata la finestra dei dialoghi. Con "show", viene
## mostrata sempre. Con "hide", è mostrata solo quando ci sono linee di dialogo.
## Con "auto", la finestra è nascosta prima di un comando 'scene' e mostrata di
## nuovo al successivo dialogo.
##
## Dopo che il gioco ha avuto inizio, questo può essere cambiato coi comandi
## "window show", "window hide", and "window auto".

define config.window = "auto"


## Transizioni usate per mostrare e nascondere la finestra dei dialoghi

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Opzioni predefinite #########################################################

## Controlla la velocità del testo predefinita. Lo standard, 0, è infinito,
## mentre qualunque altro numero indica il numero di caratteri al secondo da
## mostrare.

default preferences.text_cps = 0


## Il ritardo predefinito dell'avanzamento automatico. Numeri alti portano ad
## attese più lunghe, con un intervallo valido da 0 a 30.

default preferences.afm_time = 15


## Percorso Salvataggi #########################################################
##
## Controlla dove ren'Py pone i file di salvataggio, secondo la piattaforma. I
## file possono essere posti in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Di solito questo non dovrebbe venire cambiato, ma se lo fosse deve sempre
## essere una stringa diretta e non un'espressione.

define config.save_directory = "Snake-1683539094"


## Icona #######################################################################
##
## L'icona mostrata sulla dock o sulla barra applicazioni.

define config.window_icon = "gui/window_icon.png"


## Configura Compilazione ######################################################
##
## Questa sezione controlla come Ren'Py trasforma il tuo progetto in file di
## distribuzione.

init python:

    ## Le funzioni seguenti richiedono schemi di nome. Questi schemi non
    ## differenziano maiuscole e minuscole, e corrispondono al percorso relativo
    ## alla cartella base, con e senza un segno / preposto. Se più schemi
    ## corrispondono, viene usato il primo.
    ##
    ## In uno schema:
    ##
    ## / è il separatore fra cartelle.
    ##
    ## * equivale a qualunque carattere tranne il separatore fra cartelle.
    ##
    ## ** equivale a qualunque carattere inclusi i separatori fra cartelle.
    ##
    ## Per esempio, "*.txt" indica file .txt nella cartella base, "game/**.ogg"
    ## indica file .ogg nella cartella base o qualunque sua sottocartella, e
    ## "**.psd" indica file .psd ovunque nel progetto.

    ## Classifica file come 'None' per escluderli dalla compilazione.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Per archiviare i file, classificali come 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## I file che corrispondono a schemi di documentazione sono duplicati nella
    ## compilazione di app Macintosh, quindi appariranno sia nella app che nel
    ## file zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Una licenza Google Play è richiesta per scaricare file di espansione ed
## eseguire acquisti in-app. La Chiave Licenza può essere trovata alla pagina
## "Services & APIs" della console sviluppatori di Google Play.

# define build.google_play_key = "..."


## L'username e project name associati a un progetto itch.io, separati da una
## slash.

# define build.itch_project = "renpytom/test-project"
