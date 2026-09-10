# program praktikum minggu 2. 9/10/26. 
# program ini mengunakan fungsi type() untuk menampilkan tipe data dari variabel yang dibuat.

def main():
    # create a variable with numeric type value
    a_2021 = 100
    print("The type of variable having value", a_2021, " is ", type(a_2021))

    # create a variable with float value.
    b_2021 = 10.2345
    print("The type of variable having value", b_2021, " is ", type(b_2021))

    # create a variable with complex value.
    c_2021 = 100 + 3j
    print("The type of variable having value", c_2021, " is ", type(c_2021))


if __name__ == "__main__":
    main()

