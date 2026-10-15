#Magánhangzó eltávolítás
"Input: 'Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol.'"
"Return: 'dn Jv szgtn vltnk nyrln. Nm s tdtm, hgy lnvztk gy hlyt gy prgrmzs nylvrl.'"
maganhangzo = "aáeéiíuúüűoóöőAÁEÉIÍUÚÜŰÖŐOÓ"
def maganhangzo_eltavolitas(szoveg:str)->str:
    alakitott = ""
    for betu in szoveg:
        if betu not in maganhangzo:
            alakitott += betu
    
    return alakitott


print(maganhangzo_eltavolitas('Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol.'))