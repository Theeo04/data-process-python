import csv

# def split_array(array):
#     # Define separator
#     separator = ';'

#     # Split each element of the array
#     split_array = []
#     current_element = ''
#     for element in array:
#         if '"' in element:
#             current_element += element
#             if current_element.count('"') % 2 != 0:
#                 continue
#         else:
#             current_element += element

#         split_array.append(current_element)
#         current_element = ''

#     return split_array

def split_ignore_quotes(text, separator=';'):
    result = []
    inside_quotes = False
    current_token = ''
    
    for char in text:
        if char == '"':
            inside_quotes = not inside_quotes
        elif char == "'" and not inside_quotes:
            inside_quotes = not inside_quotes
        elif char == separator and not inside_quotes:
            result.append(current_token.strip())
            current_token = ''
        else:
            current_token += char
    
    result.append(current_token.strip())
    
    return result

def split_array_with_quotes(array):
    split_array = []
    current_element = ''
    in_quotes = False

    for element in array:
        for char in element:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                split_array.append(current_element)
                current_element = ''
                continue
            current_element += char
        
        split_array.append(current_element)
        current_element = ''
    
    return split_array

def cauta_in_csv_cu_key(keyword, datasetName):
    with open(datasetName, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for linie in csvreader:
            for camp in linie:
                if keyword in camp:
                    return linie
    return None

def readSearchParamInDataset(datasetName, indexCautare, n):
    with open(datasetName, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        numar_linii = 0
        for linie in csvreader:
            numar_linii += 1
            if numar_linii == n:
                return linie[indexCautare]  # Caută în funcție al i cuvânt din linie

def get_line_from_facebook_dataset(n):
    with open('facebook_dataset.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        numar_linii = 0
        for linie in csvreader:
            numar_linii += 1
            if numar_linii == n:
                return linie

# Verificarea datelor care exista
def checkIfExist(a=None, b=None, c=None):
    if a is not None:
        return a
    elif b is not None:
        return b
    elif c is not None:
        return c
    else:
        return ''

# Verificarea adresei
def checkValidAddress(a=None, b=None, c=None):
    addresses = [a, b, c]  # Le stocam într-o listă pentru a putea itera mai ușor
    valid_address = None
    max_digits = 0 m

    for address in addresses:
        # Verificăm dacă adresa este None sau niciun caracter
        if address is None or len(address) == 0:
            continue  # Trecem la următoarea adresă

        # Numar cifre din adresa curenta
        num_digits = sum(1 for char in address if char.isdigit())

        # Verificare criterii
        if len(address) > 0 and num_digits > max_digits:
            valid_address = address
            max_digits = num_digits

    return valid_address 

def cautare_si_scriere_csv():
    with open('sortare_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header_row = ['address', 'category', 's_category', 'city', 'country_code', 'country_name', 'name', 'phone', 'phone_country_code', 'raw_address', 'raw_phone', 'region_code', 'region_name', 'text/description', 'zip_code', 'domain', 'domain_suffix', 'language', 'legal_name', 'region', 'site_name', 'tld', 'email', 'link', 'zip_code']
        writer.writerow(header_row)

        for n in range(2, 70000):
            rezultat = [None, None, None] # 0: Google; 1: Website; 2: Facebook
            row = [''] * len(header_row)
            rezultat[2] = get_line_from_facebook_dataset(n)
            index = 0
            paramCautare = readSearchParamInDataset('facebook_dataset.csv', index, n) 
            
            # Cautăm în 'google_dataset.csv'
            cautareGoogle = cauta_in_csv_cu_key(paramCautare, 'google_dataset.csv')
            if cautareGoogle is not None: 
                rezultat[0] = cautareGoogle
            else:
                while cautareGoogle is None:
                    index += 1
                    paramCautare = readSearchParamInDataset('facebook_dataset.csv', index, n)
                    cautareGoogle = cauta_in_csv_cu_key(paramCautare, 'google_dataset.csv')
                rezultat[0] = cautareGoogle

            # Cautăm în 'website_dataset.csv'
            index = 0
            paramCautare = readSearchParamInDataset('facebook_dataset.csv', index, n)
            cautareWebsite = cauta_in_csv_cu_key(paramCautare, 'website_dataset.csv')
            if cautareWebsite is not None: 
                rezultat[1] = cautareWebsite
            else:
                while cautareWebsite is None:
                    index += 1
                    paramCautare = readSearchParamInDataset('facebook_dataset.csv', index, n)
                    cautareWebsite = cauta_in_csv_cu_key(paramCautare, 'website_dataset.csv')
                rezultat[1] = cautareWebsite

            
            rezultat[1] = rezultat[1][0].split(';')

            for i in range(3):
                while len(rezultat[i]) < 15:
                    rezultat[i].append(None)

            #Pentru a observa cum evolueaza procesul
            print(f'Rezultat index 1: {rezultat[1]}')
            
            row[0] = checkValidAddress(rezultat[0][0], rezultat[2][1])
            row[1] = checkIfExist(rezultat[0][1], rezultat[1][10])
            row[2] = checkIfExist(rezultat[1][7])
            row[3] = checkIfExist(rezultat[0][2], rezultat[1][4], rezultat[2][3])
            row[4] = checkIfExist(rezultat[0][3], rezultat[1][4])
            row[5] = checkIfExist(rezultat[0][4], rezultat[2][5])
            row[6] = checkIfExist(rezultat[0][5], rezultat[2][9])
            row[7] = checkIfExist(rezultat[0][6], rezultat[1][7], rezultat[2][11])
            row[8] = checkIfExist(rezultat[0][7], rezultat[2][12])
            row[9] = checkIfExist(rezultat[0][8])
            row[10] = checkIfExist(rezultat[0][9])
            row[11] = checkIfExist(rezultat[0][10], rezultat[2][13])
            row[12] = checkIfExist(rezultat[0][11], rezultat[2][14])
            row[13] = checkIfExist(rezultat[0][12], rezultat[1][6])
            row[14] = checkIfExist(rezultat[0][13], rezultat[2][15])
            row[15] = checkIfExist(rezultat[0][13], rezultat[1][0], rezultat[2][0])
            row[16] = checkIfExist(rezultat[1][1])
            row[17] = checkIfExist(rezultat[1][2])
            row[18] = checkIfExist(rezultat[1][3])
            row[19] = checkIfExist(rezultat[1][4])
            row[20] = checkIfExist(rezultat[1][5])
            row[21] = checkIfExist(rezultat[1][6])
            row[22] = checkIfExist(rezultat[2][7])
            row[23] = checkIfExist(rezultat[2][8])
            row[24] = checkIfExist(rezultat[2][15])

            # Scriem în fisierul CSV
            writer.writerow(row)

cautare_si_scriere_csv()
