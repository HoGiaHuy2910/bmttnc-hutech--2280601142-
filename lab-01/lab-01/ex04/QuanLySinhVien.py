from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId =1
        if(self.soLuongSinhVien()> 0):
            maxId =self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId <sv._id):
                    maxId = sv._id
                maxId =maxId +1
            return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien._len_()
    def nhapSinhVien(self):
        return self.listSinhVien._len_()
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("nhap name:")
        sex = input("Nhap gioi tinh:")
        major=input("Nhap chuyen nganh sv:")
        diemTB = float(input("Nhap diem cua sv:"))
        sv = SinhVien(svId, name , sex , major , diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self,ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhap ten sv: ")
            sex = input("Nhap gioi tinh:")
            major=input("Nhap chuyen nganh sv:")
            diemTB = float(input("Nhap diem cua sv:"))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinhvienco ID = {} ko ton tai".format(ID))
    def sortById(self):
        self.listSinhVien.sort(key=lambda x: x._id,reverse=False)
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name,reverse=False) 
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB,reverse=False)   
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() >0):
            for sv in self.listSinhVien:
                if (sv._id ==ID):
                    searchResult =sv
        return searchResult
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >=8):
            sv._hocluc = "Gioi"
        elif(sv._diemTB >=6.5):
            sv._hocluc="Kha"  
        elif (sv._diemTB >=6.5):
            sv._hocluc = "Trung binh"
        else:
        sv._hocluc = "Yeu"
                                                     