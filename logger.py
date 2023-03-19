import logging as log

# Se muestran desde el nivel mas basico (debug) en adelante

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', # Esto agrega el tiempo
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('C:\\Users\\Usuario\\Desktop\\ClicOH\\Programacion\\FastAPI\\Prueba-CRUD\\CRUD'
                                    '-Test\\DataLayer.log'),
                    log.StreamHandler()]
                )

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
