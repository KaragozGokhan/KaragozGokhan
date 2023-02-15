import cv2
from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod
from collections.abc import MutableMapping
import xlwt

class Visualize:
    def __init__(self):
        self.root = Tk()
        self.root.title("Storeroom Software")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        self.capture_button = ttk.Button(self.frame, text="Capture", command=self.capture_video)
        self.capture_button.grid(column=0, row=0)

        self.image_button = ttk.Button(self.frame, text="Image", command=self.show_image)
        self.image_button.grid(column=1, row=0)

        self.root.mainloop()

    def capture_video(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, frame = self.cap.read()
            cv2.imshow("Storeroom", frame)
            if cv2.waitKey(1) == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()

    def show_image(self):
        pass  # TODO: Add code to show image of selected raw material/product photo


class RawMaterials(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key


class Products(RawMaterials):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __keytransform__(self, key):
        return key.lower()

    def save_to_excel(self, file_name):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("Products")
        row = 0
        for key, value in self.items():
            worksheet.write(row, 0, key)
            for col, item in enumerate(value):
                worksheet.write(row, col+1, item)
            row += 1
        workbook.save(file_name)

    def load_from_excel(self, file_name):
        pass  # TODO: Add code to load raw materials and products from Excel file

visualize = Visualize()

raw_materials = RawMaterials()
raw_materials["RM1"] = ("Name", "Date of Purchase", "Name of Supplier", "Storage Expiration Date", "Storage Code", "Description")
raw_materials["RM2"] = ("Name", "Date of Purchase", "Name of Supplier", "Storage Expiration Date", "Storage Code", "Description")
raw_materials["RM3"] = ("Name", "Date of Purchase", "Name of Supplier", "Storage Expiration Date", "Storage Code", "Description")
raw_materials["RM4"] = ("Name", "Date of Purchase", "Name of Supplier", "Storage Expiration Date", "Storage Code", "Description")
raw_materials["RM5"] = ("Name", "Date of Purchase", "Name of Supplier", "Storage Expiration Date", "Storage Code", "Description")

products = Products()
products["Product1"] = ("Name", "Date of Production", "Name of Customer", "Product Expiration Date", "Storage Code", "List of Raw Material Codes", "Description")
products["Product2"] = ("Name", "Date of Production", "Name of Customer", "Product Expiration Date", "Storage Code", "List of Raw Material Codes", "Description")
products["Product3"] = ("Name", "Date of Production", "Name of Customer", "Product Expiration Date", "Storage Code", "List of Raw Material Codes", "Description")
products["Product4"] = ("Name", "Date of Production", "Name of Customer", "Product Expiration Date", "Storage Code", "List of Raw Material Codes", "Description")
products["Product5"] = ("Name", "Date of Production", "Name of Customer", "Product Expiration Date", "Storage Code", "List of Raw Material Codes", "Description")

products.save_to_excel("products.xls")

