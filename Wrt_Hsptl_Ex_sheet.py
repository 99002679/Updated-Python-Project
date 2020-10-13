def Wrt_Patients_Db(Pat_DataBase):
    myfile = open("PatientData.csv", "w")
    for i in Pat_DataBase:
        myfile.write(
            str(i) + ";" + Pat_DataBase[i][0] + ";" + Pat_DataBase[i][1] + ";" + Pat_DataBase[i][
                2] + ";" + Pat_DataBase[i][3] + ";" + Pat_DataBase[i][4] + ";" + Pat_DataBase[i][
                5] + ";" + Pat_DataBase[i][6] + "\n")
    myfile.close()


def Wrt_Doc_Db(Doc_DataBase):
    myfile = open("DocData.csv", "w")
    for i in Doc_DataBase:
        myfile.write(str(i) + ";")
        for j in Doc_DataBase[i]:
            myfile.write(str(j[0]) + ";" + j[1] + ";" + j[2] + ";")
        myfile.write("\n")

    myfile.close()