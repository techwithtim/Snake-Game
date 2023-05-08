################################################################################
## Inizializzazione
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Dichiarare gui.init resetta gli stili ai valori predefiniti, e imposta
## l'altezza e larghezza del gioco.
init python:
    gui.init(1920, 1080)



################################################################################
## Variabili di Configurazione GUI
################################################################################


## Colori ######################################################################
##
## I colori del testo nell'interfaccia.

## Un colore di risalto usato nell'interfaccia per le etichette e il testo in
## evidenza.
define gui.accent_color = '#336600'

## Il colore usato per il testo di un pulsante quando non è nè selezionato nè
## sotto il puntatore.
define gui.idle_color = '#aaaaaa'

## Il colore small è usato per testo piccolo, che richiede di essere più chiaro
## o più scuro per ottenere lo stesso effetto.
define gui.idle_small_color = '#888888'

## Il colore usato per pulsanti e barre che si trovano sotto il puntatore.
define gui.hover_color = '#336600'

## Il colore usato per il testo di un pulsante che è selezionato ma non
## evidenziato. Un pulsante è selezionato se indica l'attuale schermata o valore
## di preferenza.
define gui.selected_color = '#555555'

## Il colore del testo per un pulsante che non può venire selezionato.
define gui.insensitive_color = '#aaaaaa7f'

## Colori usati per le frazioni di barre che non sono riempite. Non vengono
## usati direttamente, ma lo sono quando si ri-generano i file immagine della
## barra.
define gui.muted_color = '#84a366'
define gui.hover_muted_color = '#adc199'

## I colori usati per il dialogo e le scelte.
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'


## Font e Dimensioni ###########################################################

## Il font usato per il testo interno al gioco.
define gui.text_font = "DejaVuSans.ttf"

## Il font usato per i nomi dei personaggi.
define gui.name_text_font = "DejaVuSans.ttf"

## Il font usato per il testo esterno al gioco.
define gui.interface_text_font = "DejaVuSans.ttf"

## La dimensione del normale testo di dialogo.
define gui.text_size = 33

## La dimensione dei nomi dei personaggi.
define gui.name_text_size = 45

## Le dimensioni del testo nell'interfaccia di gioco.
define gui.interface_text_size = 33

## Le dimensioni delle etichette nell'interfaccia di gioco.
define gui.label_text_size = 36

## La dimensione del testo delle notifiche (notify screen).
define gui.notify_text_size = 24

## Le dimensioni del titolo del gioco.
define gui.title_text_size = 75


## Menu - Main e Game ##########################################################

## Le immagini usate per i menu Main e Game.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogo #####################################################################
##
## Queste variabili controllano come viene mostrato il dialogo a schermo una
## linea alla volta.

## L'altezza del textbox contenente il dialogo.
define gui.textbox_height = 278

## La posizione verticale del textbox sullo schermo. 0.0 è in alto, 0.5 è al
## centro, e 1.0 è in basso.
define gui.textbox_yalign = 1.0


## La posizione del nome del personaggio, relativa al textbox. Può essere un
## numero esatto di pixel da sinistra o da sopra, oppure 0.5 per centrare.
define gui.name_xpos = 360
define gui.name_ypos = 0

## L'allineamento orizzontale del nome del personaggio. Può essere 0.0 per
## allinearlo a sinistra, 0.5 al centro e 1.0 a destra.
define gui.name_xalign = 0.0

## Larghezza, altezza e bordi del riquadro che contiene il nome del personaggio,
## oppure None per dimensionarlo automaticamente.
define gui.namebox_width = None
define gui.namebox_height = None

## I bordi del riquadro che contiene il nome del personaggio, in questo ordine:
## sinistro, superiore, destro, inferiore.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Se 'True', lo sfondo di namebox sarà tassellato (ripetuto come una
## piastrella). Se 'False' sarà invece scalato.
define gui.namebox_tile = False


## La posizione dei dialoghi, relativa al textbox. Può essere un numero esatto
## di pixel relativo ai bordi sinistro o superiore del textbox, oppure 0.5 per
## centrare.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## La larghezza massima del testo di dialogo, in pixel.
define gui.dialogue_width = 1116

## L'allineamento orizzontale del testo di dialogo. Può essere 0.0 per
## allinearlo a sinistra, 0.5 al centro e 1.0 a destra.
define gui.dialogue_text_xalign = 0.0


## Pulsanti ####################################################################
##
## Queste variabili, assieme alle immagini contenute in gui/button, definiscono
## l'aspetto dei pulsanti.

## Larghezza e altezza di un pulsante, in pixel. Se 'None', Ren'Py calcolerà una
## dimensione.
define gui.button_width = None
define gui.button_height = None

## I bordi su ogni lato del pulsante, nell'ordine: sinistro, superiore, destro,
## inferiore.
define gui.button_borders = Borders(6, 6, 6, 6)

## Se 'True', l'immagine di sfondo sarà tassellata. Se 'False', l'immagine di
## sfondo verrà scalata.
define gui.button_tile = False

## Il font usato dal pulsante.
define gui.button_text_font = gui.interface_text_font

## La dimensione del testo usato dal pulsante.
define gui.button_text_size = gui.interface_text_size

## Colore testo nel pulsante, secondo i vari stati.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## L'allineamento orizzontale del testo nel pulsante. (0.1 a sinistra, 0.5 al
## centro, 1.0 a destra).
define gui.button_text_xalign = 0.0


## Queste variabili sovrascrivono le impostazioni per differenti tipi di
## pulsante. Leggere nella documentazione i tipi di pulsante disponibili, e per
## cosa viene usato ciascuno.
##
## Queste personalizzazioni sono usate dall'interfaccia predefinita:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Puoi aggiungere le tue personalizzazioni, aggiungendo variabili con la giusta
## nomenclatura. Per esempio, puoi togliere il segno # dalla linea seguente per
## impostare una larghezza fissa dei pulsanti di navigazione.

# define gui.navigation_button_width = 250


## Pulsanti Scelta #############################################################
##
## I pulsanti di scelta sono usati per i menu interni al gioco.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Pulsanti Slot ###############################################################
##
## Un pulsante Slot è un tipo di pulsante speciale. Contiene un'immagine
## miniatura, e testo che riporta i contenuti dello slot. Uno Slot Save usa
## immagini presenti in gui/button, come tutti gli altri tipi di pulsante.

## Il pulsante slot.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Larghezza e altezza delle miniature usate dallo slot.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Numero di colonne e righe della griglia degli slot.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posizioni e Spaziature ######################################################
##
## Queste variabili controllano posizione e spaziatura di vari elementi
## dell'interfaccia.

## Posizione del lato sinistro dei pulsanti di navigazione, relativa al lato
## sinistro dello schermo.
define gui.navigation_xpos = 60

## Posizione verticale dell'indicatore 'SALTO'.
define gui.skip_ypos = 15

## Posizione verticale delle notifiche.
define gui.notify_ypos = 68

## Spaziatura fra le scelte.
define gui.choice_spacing = 33

## Pulsanti nella sezione di navigazione dei menu Main e Game.
define gui.navigation_spacing = 6

## Controlla l'ammontare di spazio fra le opzioni (preferences).
define gui.pref_spacing = 15

## Controlla l'ammontare di spazio fra i pulsanti delle opzioni (preferences).
define gui.pref_button_spacing = 0

## La spaziatura fra i pulsanti delle pagine file.
define gui.page_spacing = 0

## Spaziatura fra gli slot.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frame #######################################################################
##
## Queste variabili controllano l'aspetto dei frame che possono contenere
## elementi d'interfaccia quando un livello sostrato (overlay) o una finestra
## sono assenti.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Frame usato come parte del confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Frame usato come parte dello skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Frame usato come parte delle notifiche.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Gli sfondi del frame devono essere tassellati?
define gui.frame_tile = False


## Barre, Barre Scorrimento e Selettori ########################################
##
## Controllano aspetto e dimensioni di barre e selettori
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## Altezza delle barre orizzontali. Larghezza delle barre verticali.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 'True' se le immagini devono venire tassellate. 'False' se devono venire
## scalate.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordi orizzontali.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Bordi verticali.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Cosa fare con barre di scorrimento che non possono scorrere. "hide" le
## nasconde, mentre None le mostra comunque.
define gui.unscrollable = "hide"


## History #####################################################################
##
## Lo screen 'History' mostra una cronologia dei dialoghi già letti dal
## giocatore.

## Il numero di blocchi di dialogo conservati da Ren'Py nella cronologia.
define config.history_length = 250

## L'altezza di un elemento nella schermata di cronologia, oppure None per avere
## altezze variabili al costo delle prestazioni.
define gui.history_height = 210

## Posizione, larghezza e allineamento dell'etichetta che equivale al nome del
## personaggio in causa.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Posizione, larghezza e allineamento del testo di dialogo.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Modalità NVL ################################################################
##
## Lo screen NVL mostra il dialogo dei personaggi NVL.

## I bordi della finestra in Modalità NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## L'altezza di un elemento NVL. Impostalo a 'None' e gli elementi stabiliranno
## un'altezza automatica.
define gui.nvl_height = 173

## La spaziatura fra gli elementi in Modalità NVL, quando gui.nvl_height è None,
## e fra questi e un menu NVL.
define gui.nvl_spacing = 15

## Posizione, larghezza e allineamento dell'etichetta che equivale al nome del
## personaggio in causa.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Posizione, larghezza e allineamento del testo di dialogo.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## La posizione, larghezza e allineamento del testo nvl_thought (il testo del
## personaggio nvl_narrator.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## La posizione dei menu_buttons in modalità NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## Localizzazione ##############################################################

## Questo controlla dove avviene un'interruzione di riga. Il valore predefinito
## è valido per la maggior parte dei linguaggi. Una lista di valori disponibili
## si può trovare su:https://www.renpy.org/doc/html/style_properties.html#style-
## property-language

define gui.language = "unicode"


################################################################################
## Dispositivi mobili
################################################################################

init python:

    ## Questo aumenta la dimensione dei Pulsanti Rapidi per renderli più facili
    ## da toccare su tablet e telefoni.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Questo cambia la dimensione e spaziatura di vari elementi della GUI per
    ## assicurarsi che siano facilmente visibili su telefono.
    @gui.variant
    def small():

        ## Dimensioni font.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Cambia la posizione del textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Schema pulsanti file.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modalità NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
