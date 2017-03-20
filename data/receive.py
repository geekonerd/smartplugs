from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO

'''Segnali catturati dal chip e durata massima di cattura'''
SEGNALI_CATTURATI = [[], []]  #[[tempo di lettura], [segnale catturato]]
DURATA_MAX_CATTURA = 5

'''Pin da utilizzare per leggere i dati catturati dal chip ricevitore'''
PIN_DATA_DI_CATTURA = 23


if __name__ == '__main__':
    '''Utilizziamo lo standard BCM per specificare quale PIN utilizzare'''
    GPIO.setmode(GPIO.BCM)
    '''Impostiamo il PIN indicato nello standard BCM come PIN di lettura dati'''
    GPIO.setup(PIN_DATA_DI_CATTURA, GPIO.IN)
    
    '''Avvio della cattura'''
    tempo_trascorso = 0
    tempo_di_inizio = datetime.now()
    print '**Premere un tasto del telecomando (per circa un secondo)**'
    
    '''Fin quando dura il tempo di cattura'''
    while tempo_trascorso < DURATA_MAX_CATTURA:
        '''Salviamo il tempo e il valore catturato dal chip ricevitore'''
        delta_tempo = datetime.now() - tempo_di_inizio
        SEGNALI_CATTURATI[0].append(delta_tempo)
        SEGNALI_CATTURATI[1].append(GPIO.input(PIN_DATA_DI_CATTURA))
        tempo_trascorso = delta_tempo.seconds

    '''Cattura terminata, sample catturati e chiusura del GPIO'''
    print '**Cattura completata**'
    print len(SEGNALI_CATTURATI[0]), 'sample registrati'
    GPIO.cleanup()

    '''Processamento dei dati mantenendo solo secondi e microsendi dei tempi'''
    print '**Processamento...**'
    for i in range(len(SEGNALI_CATTURATI[0])):
        SEGNALI_CATTURATI[0][i] = SEGNALI_CATTURATI[0][i].seconds + SEGNALI_CATTURATI[0][i].microseconds/1000000.0

    '''Avvio di matplotlib per mostrare a video i segnali catturati'''
    print '**Visualizzazione risultato**'
    pyplot.plot(SEGNALI_CATTURATI[0], SEGNALI_CATTURATI[1])
    pyplot.axis([0, DURATA_MAX_CATTURA, -1, 2])
    pyplot.show()
