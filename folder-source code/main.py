import numpy as np

def show_SPL(matriks, row, column, variable):
    
    for i in range(row): 
        status = False
        for j in range(column):
            if j < column-1:
               
                if matriks[i][j] != 0:
                    if status == True:
                        
                        if matriks[i][j] > 0:
                            print(" +", end="")
                        else:
                            print(" ", end="")
                    print(" {}{}".format(matriks[i][j], variable[j]), end="")
                    status = True
            else:
                if status == True:
                    print(" =", matriks[i][j])


def show_matriks(matriks, row, column):

    for i in range(row):
        print(" [", end="")
        for j in range(column):
         
            if matriks[i][j] != 0:
                matriks[i][j] = round(matriks[i][j], 2)
           
            if j == column-1:
                print(" |", end="")
        
            print(" {}".format(matriks[i][j]), end="")
        print(" ]")

def gauss(matriks, row, column, i=0, z=0):
    
    if i < row:
        if z < column-1:
           
            if matriks[i][z] == 0:
                for j in range(i+1, row):
                    
                    if matriks[j][z] != 0:
                        for k in range(column):
                            matriks[i][k], matriks[j][k] = matriks[j][k], matriks[i][k]
                        print("="*50)
                        print("R{} =><= R{}".format(i+1, j+1))
                        show_matriks(matriks, row, column)
                        break
        
            if matriks[i][z] != 0:
              
                if matriks[i][z] != 1:
           
                    temp = matriks[i][z]
                    for j in range(z, column):
                        matriks[i][j] /= temp
                   
                    print("="*50)
                    print("R{} / {}".format(i+1, temp))
                    show_matriks(matriks, row, column)
                
                for j in range(i+1, row):
                    if matriks[j][z] != 0:
                        
                        temp = matriks[j][z] / matriks[i][z]
                        for k in range(z, column):
                            matriks[j][k] = matriks[j][k] - (temp * matriks[i][k])
                        
                        print("="*50)
                        print("R{}".format(j+1), end="")
                        if temp > 0:
                            print(" - ", end="")
                        else:
                            print(" + ", end="")
                            temp *= -1
                        print("{}R{}".format(temp, i+1))
                        show_matriks(matriks, row, column)
              
                i += 1
                gauss(matriks, row, column, i, z)
            else:
                z += 1
                gauss(matriks, row, column, i, z)


def gauss_jordan(matriks, row, column, variable):
    status_solusi_unik = False
    
    for i in range(row):
        fill_status = True
        result_status = False
        for j in range(column):
            if j < column-1:
                if matriks[i][j] == 0 and fill_status == True:
                    fill_status = True
                else:
                    fill_status = False
            else:
                if matriks[i][j] == 0:
                    result_status = True
                else:
                    result_status = False

        if fill_status == True and result_status == False:
            print("="*50)
            print("*="+"Tidak Ada Solusi".center(48)+"=*")
            print("="*50)
            return
     
        elif fill_status == True and result_status == True:
            solusi = "Banyak Solusi"
            break

        else:
            solusi = "Solusi Unik"
            status_solusi_unik = True

    if status_solusi_unik == True or (fill_status == True and result_status == True):
        
        for i in range(row-1, -1, -1):
            for j in range(column-1):

                if matriks[i][j] != 0:
                    for k in range(i-1, -1, -1):
                       
                        if matriks[k][j] != 0:
                            temp = matriks[k][j] / matriks[i][j]
                            for l in range(j, column):
                                matriks[k][l] -= (temp * matriks[i][l])

                            print("="*50)
                            print("R{}".format(k+1), end="")
                            if temp > 0:
                                print(" - ", end="")
                            else:
                                print(" + ", end="")
                                temp *= -1
                            print("{}R{}".format(temp, i+1))
                            show_matriks(matriks, row, column)
                    break
        print("="*50)
        print("*="+solusi.center(48)+"=*")
        print("="*50)
      
        for i in range(row):
            cek = False
            for j in range(column):
                if matriks[i][j] != 0 and j < column-1:
                    if cek == True:
                        print(" +", end="")
                    print(" {}".format(variable[j]), end="")
                    cek = True
            if cek == True:
                print(" = {}".format(matriks[i][j]))
    print("="*50)


print("="*52)
print("*="+"Tubes Martriks dan Ruang Vektor".center(48)+"=*")
print("*="+(48*"*").center(48)+"=*")
print("*="+"Nama : Ahmad Fadillah ".center(48)+"=*")
print("*="+"NIM  : 121140173".center(48)+"=*")
print("="*52)

user_option = "0"

while user_option != "2":
    print("*="+"Pilihan menu untuk penyelesaian (1-2)".center(48)+"=*")
    print("="*52)
    print("*="+"1.Mencari Solusi Sistem Persamaan Linear Matriks".ljust(48)+"=*")
    print("*="+"2.Keluar".ljust(48)+"*")
    print("="*52)
    user_option = input("Input Pilihan (1-2) : ")
    print("="*52)
    status_matriks = False
    
    if user_option == "1":
        print("="*52)
        print("*="+"Masukkan Jumlah Baris Dan Kolom".ljust(48)+"=*")
        print("="*52)
        row = int(input("Baris : "))
        column = int(input("Kolom : "))
        print("="*52)
        variable = ["x{}".format(i+1) for i in range(column-1)]
        matriks = np.zeros((row, column))
        for i in range(row):
            for j in range(column):
                if j < column-1:
                    print(" {} : ".format(variable[j]), end="")
                else:
                    print(" Hasil {} : ".format(i+1), end="")
                   
                    matriks[i][j] = float(input())
                 
                    if j == column-1:
                        print("="*52)
        status_matriks = True
        if status_matriks == True:
            print("*="+"Sistem Persamaan Linear".center(48)+"*=")
            print("*"*52)
            show_SPL(matriks, row, column, variable)
            print("="*52)
            print("*="+"Matriks Augmented".center(48)+"*=")
            print("="*52)
         
            show_matriks(matriks, row, column)
            print("="*52)
            print("*="+"Proses Eliminasi Gauss".center(48)+"*=")
            print("="*52)
            
            gauss(matriks, row, column)
            print("="*52)
            print("*="+"Proses Eliminasi Gauss Jordan".center(48)+"=*")
            print("="*52)
        
            gauss_jordan(matriks, row, column, variable)

    elif user_option != "2":
        print("*="+"Inputan Salah!".center(48)+"=*")