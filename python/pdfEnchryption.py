import pikepdf
name=""
new_name=""
old_pdf=pikepdf.Pdf.open(name)
no_extract=pikepdf.Permissions(extract=False)
old_pdf.save(new_name, encryption=pikepdf.Encryption(user="password",owner="ghost",allow=no_extract))