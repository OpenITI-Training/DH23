import zipfile

fp = r"D:\AKU\teaching\2023_DH_course\session_7\This is a test document.docx"
with zipfile.ZipFile(fp) as zf:
    zf.extractall(r"D:\AKU\teaching\2023_DH_course\session_7\unzipped")