import time
import sys
import RPi.GPIO as GPIO

'''Stringhe binarie ON e OFF per le prese 1,2,3,4 mappate come a,b,c,d'''
a_on = ''
a_off = ''
b_on = ''
b_off = ''
c_on = ''
c_off = ''
d_on = '0011100011000111011010001'
d_off = '0011100011000111011010011'

'''intervalli brevi/lunghi nel segnale e tra le ripetizioni (in secondi)'''
intervallo_breve = 0.00030
intervallo_lungo = 0.00096
intervallo_tra_tentativi = 0.0113
NUMERO_DI_TENTATIVI = 15

'''PIN da utilizzare per inviare i dati verso il chip trasmettitore'''
PIN_DATA_DI_INVIO = 16


def transmit_code(code):
    '''Utilizziamo lo standard BCM per specificare quale PIN utilizzare'''
    GPIO.setmode(GPIO.BCM)
    '''Impostiamo il PIN indicato nello standard BCM come PIN di invio dati'''
    GPIO.setup(PIN_DATA_DI_INVIO, GPIO.OUT)
    
    '''Ripetiamo la trasmissione per il numero di tentativi indicati'''
    for t in range(NUMERO_DI_TENTATIVI):
        for i in code:
            if i == '1':
                '''Bit = 1, accensione breve e poi spegnimento lungo del PIN'''
                GPIO.output(PIN_DATA_DI_INVIO, 1)
                time.sleep(intervallo_breve)
                GPIO.output(PIN_DATA_DI_INVIO, 0)
                time.sleep(intervallo_lungo)
            elif i == '0':
                '''Bit = 0, accensione lunga e poi spegnimento breve del PIN'''
                GPIO.output(PIN_DATA_DI_INVIO, 1)
                time.sleep(intervallo_lungo)
                GPIO.output(PIN_DATA_DI_INVIO, 0)
                time.sleep(intervallo_breve)
            else:
                continue
        '''Spegnimento del PIN e attesa fino al prossimo intervallo'''
        GPIO.output(PIN_DATA_DI_INVIO, 0)
        time.sleep(intervallo_tra_tentativi)

    '''Invio terminato e chiusura del GPIO'''
    GPIO.cleanup()


if __name__ == '__main__':
    '''Cattura del segnale da inviare: a_on, a_off, b_on - etc...'''
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
