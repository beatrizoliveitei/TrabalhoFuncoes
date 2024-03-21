def compose(f, g, x):
  return f(g(x))

def main():
  f_str = input("Digite a função f(x): ")
  g_str = input("Digite a função g(x): ")
  x = int(input("Digite o valor de x: "))

  f_str = f_str.replace("^", "**")  
  g_str = g_str.replace("^", "**")

  f = eval("lambda x: " + f_str)
  g = eval("lambda x: " + g_str)

  g_of_f = compose(g, f, x)
  print("(g ° f)({}) =".format(x), g_of_f)

  g_of_g = compose(g, g, x)
  print("(g ° g)({}) =".format(x), g_of_g)

  f_of_f = compose(f, f, x)
  print("(f ° f)({}) =".format(x), f_of_f)

  f_of_g = compose(f, g, x)
  print("(f ° g)({}) =".format(x), f_of_g)

if __name__ == "__main__":
  main()
