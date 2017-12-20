import sys

SUCCESS_MSG = 'success'
EXIT_MSG = 'cya'

def convert(tup):
  (c, p, ga, gp, fmt) = tup
  return ((c, p, ga, gp, not fmt), SUCCESS_MSG)

def get_units(metric):
  return ('kilometeres', 'kilometeres', 'gallons', 'km per gallon', 'km/g') if metric else ('miles', 'miles', 'gallons', 'miles per gallon', 'm/g')

def get_data(tup):
  (_, _, _, _, fmt) = tup
  (c_u, p_u, ga_u, gp_u, _) = get_units(fmt)
  def ask_for(name, unit):
    sys.stdout.write('Please enter the new {} [{}]: '.format(name, unit))
    sys.stdout.flush()
    return input()
  try:
    c = int(ask_for('current odometer', c_u))
    p = int(ask_for('previous odometer', p_u))
    ga = int(ask_for('gas added', ga_u))
    gp = int(ask_for('gas price', gp_u))
  except ValueError as e:
    return (tup, 'fail: {}'.format(getattr(e, 'message', repr(e))))
  if c < 0 or p < 0 or ga < 0 or gp < 0:
    return (tup, 'fail: invalid params')
  return ((c, p, ga, gp, fmt), SUCCESS_MSG)

def print_data(tup):
  (c, p, ga, gp, fmt) = tup
  print('(unit: {}); current odometer: {}, previous odometer: {}, fuel efficency: {}, gas price: {}.'.format(('metric' if fmt else 'us').upper(), c, p, ga, gp)) 
  return (tup, SUCCESS_MSG)

def calculate(tup):
  (c, p, ga, gp, fmt) = tup
  (_, _, _, _, x) = get_units(fmt)
  if c < 0 or p < 0 or ga < 0 or gp < 0:
    return (tup, 'fail: invalid params')
  miles = p - c
  gpu = miles / ga
  print('{}{}'.format(gpu, x))
  return (tup, SUCCESS_MSG)
  
def repl():
  cur_od = -1
  pre_od = -1
  fuel_efficency = -1
  gas_price = -1
  g_format = True # use metric
  
  tup = (cur_od, pre_od, fuel_efficency, gas_price, g_format)
  
  response = ''

  options = [
      ("data", get_data, True),
      ("convert", convert, True),
      ("print", print_data, False),
      ("calculate", calculate, False)
  ]
  
  def find_and_execute(tup, response, options):
    for option in options:
      (name, func, rets) = option
      if name.lower() == response.lower():
        if rets:
          return func(tup)
        else:
          (x, err) = func(tup)
          return (tup, err)
    return    
    
  while response.lower() != EXIT_MSG:
    sys.stdout.write('Your options are: ')
    for (i, option) in enumerate(options):
      (name, _, _) = option
      sys.stdout.write('{}{}'.format(name, ', ' if i != (len(options) - 1) else '.'))
      if i == len(options) - 1:
        sys.stdout.write(' [say "{}" to dip]'.format(EXIT_MSG))
        print()
    sys.stdout.flush()  
    response = input()
    if response != EXIT_MSG:
      res = find_and_execute(tup, response, options)
      if res == None:
        print('command: {} not found.'.format(response))
      else:
        (f, err) = res
        if err != None and err.lower() != SUCCESS_MSG:
          print('data not changed: {}'.format(err))
        else:
          tup = f

  print('lol thx bye')
  
def main():
  print('welcome to my gas shit lol')
  repl()

main()
