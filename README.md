# SMARTplugs
*a smart remote for 2.0 plugs*

### Intro
**SMARTplugs** è una *web-app* che consente di controllare prese radiocomandate grazie a chip ricetrasmittenti collegati ad un Raspberry Pi. Per maggiori dettagli sul funzionamento generale rimando al *tutorial* pubblicato sul mio blog (https://geekonerd.blogspot.it/2017/03/tutorial-come-rendere-smart-le-prese-di-casa-con-il-raspberry-pi-zero-wireless.html).

#### Contenuto
Sono compresi:
- la web-app HTML+JS+PHP per il controllo da remoto
- il codice python per catturare i segnali che controllano le prese (frequenza 433MHz)
- il codice python per l'invio dei segnali che controllano le prese (frequenza 433MHz)

###### Nota bene
Il codice presente in questo repository funziona su un Raspberry Pi configurato come descritto nel tutorial. Nella versione attuale, si tratta di una *demo* che può essere utilizzata senza problemi in locale, ma ne è sconsigliato l'uso *as is* se esposta su Internet.
