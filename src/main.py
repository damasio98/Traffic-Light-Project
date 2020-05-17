#Problemas: Uma coisa que não consegui corrigir foi que após entrar em estado intermitente, o circuito só volta a um semáforo normal após completar um ciclo de 9 segundos.Se premirmos o botão quando t(led verde)=4s, então teremos de esperar 5s para conseguirmos que ele volte ao normal.  
#Podemos carregar no botão que nada acontece. Acho que isto se deve a um ciclo que é apanhado no meio (provavelmente a ver com a luz verde devido ao tempo) mas não consegui identificar e corrigir o erro.


from utime import ticks_ms,sleep_ms
from machine import Pin
led_red = Pin(21, Pin.OUT)
led_red.value(False)
led_green = Pin(19, Pin.OUT)
led_green.value(True)     #o semáforo começa com a luz verde
led_yellow = Pin(22, Pin.OUT)
led_yellow.value(False)
button_left = Pin(23, Pin.IN, Pin.PULL_UP)
button_right = Pin(18, Pin.IN, Pin.PULL_UP)

t1=ticks_ms()

while True:
  t2=ticks_ms()
  z2=ticks_ms() 
  
  if button_left.value()==0:
    sleep_ms(25)              #reparei que ao acrescentar este comando, o controlador apanhava todas as vezes que eu carregava no botão. Antes de o acrescentar, era 50/50.
    while button_left.value()==1:
      t5=ticks_ms()
      led_green.value(False)
      if t5-z2>=1000:
        z2=t5
        led_yellow.value(not led_yellow.value())
  if button_right.value()==0:
    if t2-t1>=4000:
      led_green.value(False)
      led_yellow.value(True)
      sleep_ms(1000)          #normalmente não usaria o sleep devido a implicar atrasos noutros comandos, mas neste caso assumi que depois de tocar no botão de peão não haveria necessidade de outras funções.
      led_yellow.value(False)
      led_red.value(True)
      sleep_ms(5000)
      led_red.value(False)
      led_green.value(True)
      sleep_ms(9000)
    else:
      while t2-t1<=4000:
        t8=ticks_ms()
        t2=t8
      led_green.value(False)
      led_yellow.value(True)
      sleep_ms(1000)
      led_yellow.value(False)
      led_red.value(True)
      sleep_ms(5000)
      led_red.value(False)
      led_green.value(True)
      sleep_ms(9000)  

  if t2-t1>=9000:
    t1=t2+6000
    led_green.value(False)
    led_yellow.value(True)
    
    while led_yellow.value()==1:
      t3=ticks_ms()
      z3=ticks_ms()

      if button_left.value()==0:
        sleep_ms(25)
        while button_left.value()==0:
          t7=ticks_ms()
          if t7-z3>=1000:
            z3=t7
            led_yellow.value(not led_yellow.value())
      led_yellow.value(True)
      if t3-t2>=1000:
        t2=t3+5000
        led_yellow.value(False)
    led_red.value(True)
       
    while led_red.value()==1:
      t4=ticks_ms()
      z4=ticks_ms()
          
      if button_left.value()==0:
        sleep_ms(25)
        while button_left.value()==1:
            t6=ticks_ms()
            led_red.value(False)
            if t6-z4>=1000:
              z4=t6
              led_yellow.value(not led_yellow.value())
      led_red.value(True)
          
      if t4-t3>=5000:
        t4=t3
        led_red.value(False)
        led_green.value(True)
