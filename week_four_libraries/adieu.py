#In a file called adieu.py, implement a program that prompts the user for names, one per line,
# until the user inputs control-d. Assume that the user will input at least one name.
# Then bid adieu to those names, separating two names with one and, three names with two
# commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:
# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import inflect
p = inflect.engine()

def get_names():
    names_list = []
    while True:
        try:
            name = input("Name: ")
            names_list.append(name)
        except EOFError:
            break
    return names_list

def bid_adieu(list_of_names):
    print(f"Adieu, adieu, to {p.join(list_of_names)}")

def main():
    bid_adieu(get_names())

if __name__ == "__main__":
    main()