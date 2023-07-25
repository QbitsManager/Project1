import PySimpleGUI as sg
import math
def format_history(prev_expressions):
  if len(prev_expressions) == 0:
    return "No history"

  n = min(len(prev_expressions), 6)
  history_str = "Last " + str(n) + " expressions:\n\n"
  for i in range(-n, 0):
    history_str += prev_expressions[i] + "\n"
  return history_str


def calculator():
  sg.theme('Dark Blue 2')
  layout = [
    [
      sg.Input(key='input',
               size=(20, 2),
               do_not_clear=True,
               font=('Arial', 16)),
      sg.Button('X', size=(4, 2), button_color=('white', 'red'))
    ],
    [
      sg.Button('1', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('2', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('3', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('+', size=(4, 2), button_color=('white', 'green')),
      sg.Button('sqrt', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('4', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('5', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('6', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('-', size=(4, 2), button_color=('white', 'green')),
       sg.Button('pow', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('7', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('8', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('9', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('*', size=(4, 2), button_color=('white', 'green')),
       sg.Button('sin', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('.', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('0', size=(4, 2), button_color=('white', 'blue')),
      sg.Button('C', size=(4, 2), button_color=('white', 'red')),
      sg.Button('/', size=(4, 2), button_color=('white', 'green')),
       sg.Button('cos', size=(4, 2), button_color=('white', 'blue')),
     
    ],
    [
      sg.Button('=', size=(6, 2), button_color=('white', 'purple')),
      sg.Button('Cancel', size=(8, 2), button_color=('white', 'red')),
      sg.Button('History', size=(6, 2), button_color=('white', 'blue')),
       sg.Button('tan', size=(4, 2), button_color=('white', 'blue')),
    ],
  ]

  window = sg.Window('Calculator', layout)
  prev_results = []
  ans = None

  while True:
    event, values = window.read()
    if event == 'X':
      current_input = values['input']
      if len(current_input) > 0:
        new_input = current_input[:-1]
        window['input'].update(new_input)

    if event in (sg.WIN_CLOSED, 'Cancel'):
      break
    if event in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
      if ('Expression Error' in values['input']):
        window['input'].update('')
      window['input'].update(values['input'] + event)
    elif event in ('+', '-', '*', '/'):
      if (values['input'] in 'Expression Error'):
        window['input'].update('')
      window['input'].update(values['input'] + event)
    elif event == 'C':
      window['input'].update('')
    elif event == '=':
      history=''
      try:
        result = float(eval(values['input']))
        history = values['input']+' = '+str(result)
        prev_results.append(history)
        window['input'].update(f"{result:.2f}")
      except:
        window['input'].update('Expression Error')

    elif event == 'History':

      history_str = format_history(prev_results)
      sg.popup_scrolled(history_str, title='History', size=(50, 8))

    elif event == 'sin':
        try:
            angle = float(values['input'])
            result = math.sin(math.radians(angle))
            history = 'sin '+ values['input']+' = '+str(result)
            prev_results.append(history)
            window['input'].update(str(result))
        except:
            window['input'].update('Expression Error')
    elif event == 'cos':
        try:
            angle = float(values['input'])
            result = math.cos(math.radians(angle))
            history = 'cos '+ values['input']+' = '+str(result)
            prev_results.append(history)
            window['input'].update(str(result))
        except:
            window['input'].update('Expression Error')
    elif event == 'tan':
        try:
            angle = float(values['input'])
            result = math.tan(math.radians(angle))
            history = 'tan '+ values['input']+' = '+str(result)
            prev_results.append(history)
            window['input'].update(str(result))
        except:
            window['input'].update('Expression Error')
    elif event == 'pow':
        try:
            if '**' not in values['input']:
              num = values['input']
              if num:
                pow_str = '**'
                updated_input = num + pow_str
                window['input'].update(updated_input)
            # window['input'].update(str(math.pow(float(values['input']), 2)))
        except:
            window['input'].update('Expression Error')
    elif event == 'sqrt':
        try:
            history ='√' + values['input']+' = '+str(math.sqrt(float(values['input'])))
            prev_results.append(history)
            window['input'].update(str(math.sqrt(float(values['input']))))
        except:
            window['input'].update('Expression Error')
  window.close()

calculator()
