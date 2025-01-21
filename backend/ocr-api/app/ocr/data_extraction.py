import re


def extract_data_by_type(text: str, document_type: str) -> dict:
    """
    Extract relevant data based on the document type.

    Args:
        text (str): Extracted text from the document.
        document_type (str): Type of the document ("Aadhaar", "PAN", "Passport", or "Unknown").

    Returns:
        dict: Extracted data.
    """
    def findword(text_lines, pattern):
        for line in text_lines:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                return match.group(0)
        return None

    def find_after_keyword(textlist, keyword):
        for wordline in textlist:
            if keyword.lower() in wordline.lower():
                index = textlist.index(wordline) + 1
                return textlist[index] if index < len(textlist) else None
        return None

    # Clean text into lines
    text_lines = [line.strip() for line in text.split("\n") if line.strip()]
    print(text_lines)

    if document_type == "Aadhaar":
        yob = findword(text_lines, r"\d{4}")
        gender = findword(text_lines, r"\b(Male|Female)\b")
        aadhaar_number = findword(text_lines, r"\d{4} \d{4} \d{4}")
        return {
            "Year of Birth": yob,
            "Gender": gender,
            "Aadhaar Number": aadhaar_number,
        }

    elif document_type == "PAN":

        name = None
        fname = None
        dob = None
        pan = None
        text1 = []
        # lines = text.split('\n')
        for lin in text_lines:
            s = lin.strip()
            s = lin.replace('\n', '')
            s = s.rstrip()
            s = s.lstrip()
            text1.append(s)
        text1 = list(filter(None, text1))
        name = find_after_keyword(text1, 'Name')
        if name:
            name = name.strip()
        else:
            name = "Not found"
        print(f"Extracted Name: {name}")

        # Extract Father's Name
        fname = find_after_keyword(text1, "Father's Name")
        if fname:
            fname = fname.strip()
        else:
            fname = "Not found"
        print(f"Extracted Father's Name: {fname}")

        # Extract Date of Birth
        dob = find_after_keyword(text1, 'Date of Birth')
        if dob:
            dob = dob.strip()
            # Ensuring only valid date characters
            dob = re.sub('[^0-9/]', '', dob)
            print(f"Extracted Date of Birth: {dob}")
        pan_number = findword(text_lines, r"[A-Z]{5}\d{4}[A-Z]")
        return {"Name": name, "Father Name": fname, "Date of Birth": dob, "PAN Number": pan_number}

    elif document_type == "Passport":
        passport_number = findword(text_lines, r"[A-Z]\d{7}")
        return {"Passport Number": passport_number}

    return {}


# import re


# def extract_data_by_type(text: str, document_type: str) -> dict:
#     """
#     Extract relevant data based on the document type.

#     Args:
#         text (str): Extracted text from the document.
#         document_type (str): Type of the document ("Aadhaar", "PAN", "Passport", or "Unknown").

#     Returns:
#         dict: Extracted data.
#     """
#     def findword(text_lines, pattern):
#         for line in text_lines:
#             match = re.search(pattern, line, re.IGNORECASE)
#             if match:
#                 return match.group(0)
#         return None

#     def find_after_keyword(textlist, keyword):
#         for wordline in textlist:
#             if keyword.lower() in wordline.lower():
#                 index = textlist.index(wordline) + 1
#                 return textlist[index] if index < len(textlist) else None
#         return None

#     # Clean text into lines
#     text_lines = [line.strip() for line in text.split("\n") if line.strip()]

#     if document_type == "Aadhaar":
#         yob = findword(text_lines, r"\d{4}")
#         gender = findword(text_lines, r"\b(Male|Female)\b")
#         aadhaar_number = findword(text_lines, r"\d{4} \d{4} \d{4}")
#         return {
#             "Gender": gender,
#             "Year of Birth": yob,
#             "Aadhaar Number": aadhaar_number,
#         }

#     elif document_type == "PAN":
#         name = None
#         fname = None
#         dob = None
#         pan = None
#         text1 = []
#         lines = text.split('\n')

#         for lin in lines:
#             s = lin.strip()
#             s = lin.replace('\n', '')
#             s = s.rstrip()
#             s = s.lstrip()
#             text1.append(s)
#         text1 = list(filter(None, text1))
#         pan_number = findword(text_lines, r"[A-Z]{5}\d{4}[A-Z]")
#         try:
#             # Extract Name
#             name = find_after_keyword(text1, 'Name')
#             if name:
#                 name = name.strip()
#             else:
#                 name = "Not found"
#             print(f"Extracted Name: {name}")

#             # Extract Father's Name
#             fname = find_after_keyword(text1, "Father's Name")
#             if fname:
#                 fname = fname.strip()
#             else:
#                 fname = "Not found"
#             print(f"Extracted Father's Name: {fname}")

#             # Extract Date of Birth
#             dob = find_after_keyword(text1, 'Date of Birth')
#             if dob:
#                 dob = dob.strip()
#             # Ensuring only valid date characters
#                 dob = re.sub('[^0-9/]', '', dob)
#                 print(f"Extracted Date of Birth: {dob}")

#             return {"Name": name, "Father Name": fname, "Date of Birth": dob, "PAN Number": pan_number}

#         # Extract PAN Number
#             # pan = find_after_keyword(text1, 'Permanent Account Number')
#             # if pan:
#             #     pan = pan.strip().replace(" ", "")
#             # else:
#             #     pan = "Not found"
#             # print(f"Extracted PAN: {pan}")

#         except Exception as e:
#             print(f"An error occurred: {e}")
#         # return {"PAN Number": pan_number}

#     elif document_type == "Passport":
#         passport_number = findword(text_lines, r"[A-Z]\d{7}")
#         return {"Passport Number": passport_number}

#     return {}
