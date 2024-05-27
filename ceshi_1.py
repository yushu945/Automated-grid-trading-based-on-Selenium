
import time
from quantization_rules import quantitfy


old_price = '3.331'
old_rise = '-0.004'
old_pcage = '-0.15%'
new_price = '3.500'
new_rise = '0.500'
new_pcage = ['-0.60%', '1.10%', '-1.60%', '-2.10%', '-2.60%', '-3.10%']
number = 0


while True:
    old_price,old_rise,old_pcage = quantitfy(old_price, old_rise, old_pcage, new_price, new_rise, new_pcage[number])
    number = number + 1
    time.sleep(3)
