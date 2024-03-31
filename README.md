# Dataset Process

Scopul proiectului este să organizeze și să returneze un nou set de date care grupează informațiile din toate cele trei seturi de date, furnizând un set complet de date consolidat.


# Pasii de implementare a proiectului

1. Ca si prim pas al proiectului am folosit libraria CSV pentru citirea datelor.
2. Urmatorul pas a fost cautarea in celor doua seturi de date in baza unui keyword valid (diferit de 'None'), avand ca reper datele extrase de pe Facebook - facebook_dataset.csv 
3. Imediat ce au fost gasite si extrase aceste date in baza unui keyword, a fost returnat - ca pas intermediar - un alt csv pentru a vizualiza rezultatul, acesta continand un array de string-uri:
* Exemplu de rezultat din acest csv intermediar:

    [ [elemente_facebook_dataset], [elemente_google_dataset], [elemente_website_dataset] ] => fiind acceste sub forma de matrice [i][0]

4. La interpretarea rezultatului, am avut surpriza sa aflu ca exista un singur element in cadrul vectorului, si acesta sa fie nevoie sa fie procesat cu ajutorul unor functii speciale (Fiind printre primele dati in care folosesc Python :) )

5. Logica de alegere a formatului csv-ului final este prezent in CSV-ul "grupareElemente.csv", iar functiile de procesare avand o forma simpla de evitare a alegerii unei valori 'None'



* Nota: Din cauza perioadei aglomerate de examene nu am avut destul timp pentru a aduce o implementare mai eficenta a procesarii datelor, fiind printre primele dati cand am lucrat in Python.

