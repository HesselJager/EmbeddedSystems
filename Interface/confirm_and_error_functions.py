def confirmation_message(last_command):
    switcher = {
        0x01: "Maximale uitrol waarde is succesvol aangepast",
        0x02: "Maximale oprol waarde is succesvol aangepast",
        0x03: "Het rolluik rolt nu uit (let op: automatisch rollen is uitgeschakeld)",
        0x04: "Het rolluik rolt nu op (let op: automatich rollen is uitgeschakeld)",
        0x05: "De maximale op- en uitrol waarden zijn gereset naar de standaard waarden",
        0x06: "Automatisch rollen is nu uitgeschakeld",
        0x07: "Automatisch rollen is nu ingeschakeld"}
    return switcher.get(last_command)

def error_message(last_command):
    switcher = {
        0x01: "Fout: Maximale uitrol waarde mag niet kleiner zijn dan de maximale oprol waarde",
        0x02: "Fout: Maximale oprol waarde mag niet groter zijn dan de maximale uitrol waarde",
        0x03: "Fout: Het rolluik rolt al uit",
        0x04: "Fout: Het rolluik rolt al op",
        0x06: "Fout: Automatisch rollen is al uitgeschakeld",
        0x07: "Fout: Automatisch rollen is al ingeschakeld"}
    return switcher.get(last_command)

if(receive == 0xAA):
    confirmation_message(last_sent)
elif(receive == 0xBB):
    error_message(last_sent)
else:
    print("oeps, er ging iets fout hihi")