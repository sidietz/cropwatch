import requests
import pandas
from time import sleep
import math
import copy
from lxml import html


cookies_old = {
        'JSESSIONID': '37668871C9746D7906C7E66C27AE863D',
    }

cookies = {
        'JSESSIONID': '37668871C9746D7906C7E66C27AE863D',
    }

jid = 11111111111111111111111111111111

H = {
        'Host': 'www.agrar-fischerei-zahlungen.de',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Referer': 'https://www.agrar-fischerei-zahlungen.de/Suche',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

RQ_DATA_0 = [
  ('jahr', 'jahr'),
  ('name', ''),
  ('plz', '91586'),
  ('ort', ''),
  ('suchtypBetrag', 'betrag_gesamt'),
  ('operator', 'eq'),
  ('betrag', ''),
  ('suchtypEgfl', 'egfl_alle'),
  ('massnahmen.massnahmenEgfl[0].kurztext', 'Direktzahlungen'),
  ('massnahmen.massnahmenEgfl[0].schluessel', '00001'),
  ('massnahmen.massnahmenEgfl[0].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[0].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[1].kurztext', 'Basispr\xE4mie'),
  ('massnahmen.massnahmenEgfl[1].schluessel', '00002'),
  ('massnahmen.massnahmenEgfl[1].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[1].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[2].kurztext', 'Umverteilungspr\xE4mie'),
  ('massnahmen.massnahmenEgfl[2].schluessel', '00003'),
  ('massnahmen.massnahmenEgfl[2].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[2].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[3].kurztext', 'Greening-Pr\xE4mie'),
  ('massnahmen.massnahmenEgfl[3].schluessel', '00004'),
  ('massnahmen.massnahmenEgfl[3].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[3].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[4].kurztext', 'Junglandwirtepr\xE4mie'),
  ('massnahmen.massnahmenEgfl[4].schluessel', '00005'),
  ('massnahmen.massnahmenEgfl[4].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[4].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[5].kurztext', 'Kleinerzeugerregelung'),
  ('massnahmen.massnahmenEgfl[5].schluessel', '00006'),
  ('massnahmen.massnahmenEgfl[5].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[5].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[6].kurztext', 'Erstattung nicht genutzter Mittel der Krisenreserve'),
  ('massnahmen.massnahmenEgfl[6].schluessel', '00007'),
  ('massnahmen.massnahmenEgfl[6].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[6].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[7].kurztext', '\xD6ffentliche Intervention'),
  ('massnahmen.massnahmenEgfl[7].schluessel', '00008'),
  ('massnahmen.massnahmenEgfl[7].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[7].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[8].kurztext', 'Beihilfen f\xFCr die private Lagerhaltung'),
  ('massnahmen.massnahmenEgfl[8].schluessel', '00009'),
  ('massnahmen.massnahmenEgfl[8].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[8].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[9].kurztext', 'Schulobst- und -gem\xFCseprogramm'),
  ('massnahmen.massnahmenEgfl[9].schluessel', '00010'),
  ('massnahmen.massnahmenEgfl[9].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[9].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[10].kurztext', 'Schulmilchprogramm'),
  ('massnahmen.massnahmenEgfl[10].schluessel', '00011'),
  ('massnahmen.massnahmenEgfl[10].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[10].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[11].kurztext', 'Beihilfen im Obst- und Gem\xFCsesektor'),
  ('massnahmen.massnahmenEgfl[11].schluessel', '00012'),
  ('massnahmen.massnahmenEgfl[11].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[11].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[12].kurztext', 'St\xFCtzungsma\xDFnahmen im Weinsektor'),
  ('massnahmen.massnahmenEgfl[12].schluessel', '00013'),
  ('massnahmen.massnahmenEgfl[12].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[12].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[13].kurztext', 'Beihilfen im Bienenzuchtsektor'),
  ('massnahmen.massnahmenEgfl[13].schluessel', '00014'),
  ('massnahmen.massnahmenEgfl[13].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[13].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[14].kurztext', 'Beihilfe im Hopfensektor'),
  ('massnahmen.massnahmenEgfl[14].schluessel', '00015'),
  ('massnahmen.massnahmenEgfl[14].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[14].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[15].kurztext', 'Ausfuhrerstattungen'),
  ('massnahmen.massnahmenEgfl[15].schluessel', '00016'),
  ('massnahmen.massnahmenEgfl[15].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[15].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[16].kurztext', 'Informations- und Absatzf\xF6rderungsma\xDFnahmen'),
  ('massnahmen.massnahmenEgfl[16].schluessel', '00017'),
  ('massnahmen.massnahmenEgfl[16].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[16].gewaehlt', 'on'),
  ('massnahmen.massnahmenEgfl[17].kurztext', 'Befristete Sonderbeihilfe f\xFCr Erzeuger der Tierhaltungssektoren'),
  ('massnahmen.massnahmenEgfl[17].schluessel', '00070'),
  ('massnahmen.massnahmenEgfl[17].untergruppe', ''),
  ('_massnahmen.massnahmenEgfl[17].gewaehlt', 'on'),
  ('suchtypEler', 'eler_alle'),
  ('massnahmen.massnahmenEler[0].kurztext', 'Berufsbildungs- und Informationsma\xDFnahmen'),
  ('massnahmen.massnahmenEler[0].schluessel', '00019'),
  ('massnahmen.massnahmenEler[0].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[0].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[1].kurztext', 'Vorruhestand'),
  ('massnahmen.massnahmenEler[1].schluessel', '00020'),
  ('massnahmen.massnahmenEler[1].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[1].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[2].kurztext', 'Inanspruchnahme von Beratungsdiensten'),
  ('massnahmen.massnahmenEler[2].schluessel', '00021'),
  ('massnahmen.massnahmenEler[2].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[2].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[3].kurztext', 'Modernisierung landwirtschaftlicher Betriebe'),
  ('massnahmen.massnahmenEler[3].schluessel', '00022'),
  ('massnahmen.massnahmenEler[3].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[3].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[4].kurztext', 'Verbesserung des wirtschaftlichen Wertes der W\xE4lder'),
  ('massnahmen.massnahmenEler[4].schluessel', '00023'),
  ('massnahmen.massnahmenEler[4].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[4].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[5].kurztext', 'Erh\xF6hung der Wertsch\xF6pfung land- und forstwirtschaftlicher Erzeugnisse'),
  ('massnahmen.massnahmenEler[5].schluessel', '00024'),
  ('massnahmen.massnahmenEler[5].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[5].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[6].kurztext', 'Zusammenarbeit bei der Entwicklung neuer Produkte, Verfahren und Technologien'),
  ('massnahmen.massnahmenEler[6].schluessel', '00025'),
  ('massnahmen.massnahmenEler[6].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[6].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[7].kurztext', 'Infrastruktur in Zusammenhang mit der Entwicklung des l\xE4ndlichen Raums'),
  ('massnahmen.massnahmenEler[7].schluessel', '00026'),
  ('massnahmen.massnahmenEler[7].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[7].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[8].kurztext', 'K\xFCsten- und Hochwasserschutz (F\xF6rderperiode 2007 - 2013)'),
  ('massnahmen.massnahmenEler[8].schluessel', '00027'),
  ('massnahmen.massnahmenEler[8].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[8].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[9].kurztext', 'Ausgleichszulage Berggebiete'),
  ('massnahmen.massnahmenEler[9].schluessel', '00028'),
  ('massnahmen.massnahmenEler[9].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[9].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[10].kurztext', 'Ausgleichszulage benachteiligte Gebiete'),
  ('massnahmen.massnahmenEler[10].schluessel', '00029'),
  ('massnahmen.massnahmenEler[10].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[10].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[11].kurztext', 'Natur- und Gew\xE4sserschutz auf landwirtschaftlichen Fl\xE4chen'),
  ('massnahmen.massnahmenEler[11].schluessel', '00030'),
  ('massnahmen.massnahmenEler[11].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[11].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[12].kurztext', 'Agrarumweltma\xDFnahmen'),
  ('massnahmen.massnahmenEler[12].schluessel', '00031'),
  ('massnahmen.massnahmenEler[12].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[12].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[13].kurztext', 'Tierschutzma\xDFnahmen'),
  ('massnahmen.massnahmenEler[13].schluessel', '00032'),
  ('massnahmen.massnahmenEler[13].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[13].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[14].kurztext', 'Nichtproduktive Investitionen'),
  ('massnahmen.massnahmenEler[14].schluessel', '00033'),
  ('massnahmen.massnahmenEler[14].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[14].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[15].kurztext', 'Erstaufforstung landwirtschaftlicher Fl\xE4chen'),
  ('massnahmen.massnahmenEler[15].schluessel', '00034'),
  ('massnahmen.massnahmenEler[15].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[15].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[16].kurztext', 'Erstaufforstung nichtlandwirtschaftlicher Fl\xE4chen'),
  ('massnahmen.massnahmenEler[16].schluessel', '00035'),
  ('massnahmen.massnahmenEler[16].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[16].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[17].kurztext', 'Naturschutz auf Waldfl\xE4chen'),
  ('massnahmen.massnahmenEler[17].schluessel', '00036'),
  ('massnahmen.massnahmenEler[17].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[17].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[18].kurztext', 'Waldumweltma\xDFnahmen'),
  ('massnahmen.massnahmenEler[18].schluessel', '00037'),
  ('massnahmen.massnahmenEler[18].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[18].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[19].kurztext', 'Wiederaufbau des forstwirtschaftlichen Potenzials'),
  ('massnahmen.massnahmenEler[19].schluessel', '00038'),
  ('massnahmen.massnahmenEler[19].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[19].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[20].kurztext', 'Nicht produktive Investitionen auf Waldfl\xE4chen'),
  ('massnahmen.massnahmenEler[20].schluessel', '00039'),
  ('massnahmen.massnahmenEler[20].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[20].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[21].kurztext', 'Diversifizierung hin zu nichtlandwirtschaftlichen T\xE4tigkeiten'),
  ('massnahmen.massnahmenEler[21].schluessel', '00040'),
  ('massnahmen.massnahmenEler[21].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[21].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[22].kurztext', 'Unternehmensgr\xFCndung'),
  ('massnahmen.massnahmenEler[22].schluessel', '00041'),
  ('massnahmen.massnahmenEler[22].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[22].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[23].kurztext', 'F\xF6rderung des Fremdenverkehrs'),
  ('massnahmen.massnahmenEler[23].schluessel', '00042'),
  ('massnahmen.massnahmenEler[23].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[23].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[24].kurztext', 'Dienstleistungseinrichtungen'),
  ('massnahmen.massnahmenEler[24].schluessel', '00043'),
  ('massnahmen.massnahmenEler[24].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[24].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[25].kurztext', 'Dorferneuerung und -entwicklung'),
  ('massnahmen.massnahmenEler[25].schluessel', '00044'),
  ('massnahmen.massnahmenEler[25].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[25].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[26].kurztext', 'Erhaltung und Verbesserung des l\xE4ndlichen Erbes'),
  ('massnahmen.massnahmenEler[26].schluessel', '00045'),
  ('massnahmen.massnahmenEler[26].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[26].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[27].kurztext', 'Bildungs- und Informationsma\xDFnahmen im l\xE4ndlichen Raum'),
  ('massnahmen.massnahmenEler[27].schluessel', '00046'),
  ('massnahmen.massnahmenEler[27].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[27].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[28].kurztext', 'Kompetenzentwicklung lokale Entwicklungsstrategien'),
  ('massnahmen.massnahmenEler[28].schluessel', '00047'),
  ('massnahmen.massnahmenEler[28].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[28].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[29].kurztext', 'Lokale Entwicklungsstrategien (LEADER)'),
  ('massnahmen.massnahmenEler[29].schluessel', '00048'),
  ('massnahmen.massnahmenEler[29].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[29].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[30].kurztext', 'Technische Hilfe'),
  ('massnahmen.massnahmenEler[30].schluessel', '00053'),
  ('massnahmen.massnahmenEler[30].untergruppe', '1'),
  ('_massnahmen.massnahmenEler[30].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[31].kurztext', 'Wissenstransfer und Informationsma\xDFnahmen'),
  ('massnahmen.massnahmenEler[31].schluessel', '00054'),
  ('massnahmen.massnahmenEler[31].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[31].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[32].kurztext', 'Beratungs-, Betriebsf\xFChrungs- und Vertretungsdienste'),
  ('massnahmen.massnahmenEler[32].schluessel', '00055'),
  ('massnahmen.massnahmenEler[32].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[32].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[33].kurztext', 'Investitionen in materielle Verm\xF6genswerte'),
  ('massnahmen.massnahmenEler[33].schluessel', '00056'),
  ('massnahmen.massnahmenEler[33].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[33].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[34].kurztext', 'K\xFCsten- und Hochwasserschutz (F\xF6rderperiode 2014 - 2020)'),
  ('massnahmen.massnahmenEler[34].schluessel', '00057'),
  ('massnahmen.massnahmenEler[34].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[34].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[35].kurztext', 'Entwicklung der landwirtschaftlichen Betriebe und sonstiger Unternehmen'),
  ('massnahmen.massnahmenEler[35].schluessel', '00058'),
  ('massnahmen.massnahmenEler[35].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[35].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[36].kurztext', 'Basisdienstleistungen und Dorferneuerung'),
  ('massnahmen.massnahmenEler[36].schluessel', '00059'),
  ('massnahmen.massnahmenEler[36].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[36].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[37].kurztext', 'Investitionen in die Waldfl\xE4chenentwicklung und die Verbesserung der Lebensf\xE4higkeit der W\xE4lder'),
  ('massnahmen.massnahmenEler[37].schluessel', '00060'),
  ('massnahmen.massnahmenEler[37].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[37].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[38].kurztext', 'Agrarumwelt- und Klimaschutzma\xDFnahmen'),
  ('massnahmen.massnahmenEler[38].schluessel', '00061'),
  ('massnahmen.massnahmenEler[38].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[38].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[39].kurztext', '\xD6kologischer Landbau'),
  ('massnahmen.massnahmenEler[39].schluessel', '00062'),
  ('massnahmen.massnahmenEler[39].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[39].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[40].kurztext', 'Natur- und Gew\xE4sserschutz'),
  ('massnahmen.massnahmenEler[40].schluessel', '00063'),
  ('massnahmen.massnahmenEler[40].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[40].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[41].kurztext', 'Ausgleichszulage benachteiligte Gebiete'),
  ('massnahmen.massnahmenEler[41].schluessel', '00064'),
  ('massnahmen.massnahmenEler[41].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[41].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[42].kurztext', 'Tierschutzma\xDFnahmen'),
  ('massnahmen.massnahmenEler[42].schluessel', '00065'),
  ('massnahmen.massnahmenEler[42].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[42].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[43].kurztext', 'Waldumwelt- und -klimadienstleistungen'),
  ('massnahmen.massnahmenEler[43].schluessel', '00066'),
  ('massnahmen.massnahmenEler[43].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[43].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[44].kurztext', 'Zusammenarbeit'),
  ('massnahmen.massnahmenEler[44].schluessel', '00067'),
  ('massnahmen.massnahmenEler[44].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[44].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[45].kurztext', 'Lokale Aktionsgruppen (LEADER)'),
  ('massnahmen.massnahmenEler[45].schluessel', '00068'),
  ('massnahmen.massnahmenEler[45].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[45].gewaehlt', 'on'),
  ('massnahmen.massnahmenEler[46].kurztext', 'Technische Hilfe'),
  ('massnahmen.massnahmenEler[46].schluessel', '00069'),
  ('massnahmen.massnahmenEler[46].untergruppe', '2'),
  ('_massnahmen.massnahmenEler[46].gewaehlt', 'on')
]

rq_data1 = [
        ('jahr', 'jahr'),
        ('name', ''),
        ('ort', ''),
        ('plz', '91586'),
        ('suchtypBetrag', 'betrag_gesamt'),
        ('operator', 'eq'),
        ('betrag', ''),
        ('suchtypEgfl', 'egfl_alle'),
        ('suchtypEler', 'eler_alle'),
        ('viewOffset', '0'),
        ('viewOrderdir', 'asc'),
        ('viewOrderby', 'zahlungsempfaenger'),
        ('viewCount', ''),
        ('viewCountBeg', ''),
        ('viewLimit', '50'),
        ('offset', '0'),
        ('dir', 'asc'),
        ('order', 'zahlungsempfaenger'),
        ('count', ''),
        ('countBeg', ''),
        ('prevLimit', '50'),
        ('limit', '50'),
        ('seite', '1')
    ]


data_3 = [
  ('jahr', 'jahr'),
  ('name', ''),
  ('ort', ''),
  ('plz', ''),
  ('suchtypBetrag', 'betrag_gesamt'),
  ('operator', 'eq'),
  ('betrag', ''),
  ('suchtypEgfl', 'egfl_alle'),
  ('suchtypEler', 'eler_alle'),
  ('viewOffset', '0'),
  ('viewOrderdir', 'asc'),
  ('viewOrderby', 'zahlungsempfaenger'),
  ('viewCount', '50'),
  ('viewCountBeg', '1'),
  ('viewLimit', '50'),
  ('offset', '0'),
  ('dir', 'asc'),
  ('order', 'zahlungsempfaenger'),
  ('count', ''),
  ('countBeg', ''),
  ('prevLimit', '10'),
  ('limit', '10'),
  ('seite', '1'),
  ('showBeg', '600b8c91-be50-4222-a4d7-a3f3d974baf4')
]

data_change_to_50 = [
  ('jahr', 'jahr'),
  ('name', ''),
  ('ort', ''),
  ('plz', '91586'),
  ('suchtypBetrag', 'betrag_gesamt'),
  ('operator', 'eq'),
  ('betrag', ''),
  ('suchtypEgfl', 'egfl_alle'),
  ('suchtypEler', 'eler_alle'),
  ('viewOffset', '0'),
  ('viewOrderdir', 'asc'),
  ('viewOrderby', 'zahlungsempfaenger'),
  ('viewCount', ''),
  ('viewCountBeg', ''),
  ('viewLimit', '10'),
  ('offset', '0'),
  ('dir', 'asc'),
  ('order', 'zahlungsempfaenger'),
  ('count', ''),
  ('countBeg', ''),
  ('prevLimit', '10'),
  ('limit', '50'),
  ('seite', '1'),
]


def request_1(): # search for PLZ
    return -1


def request_2(): # update list to 50
    return -1


def request_3(): # navigate threw results to extract ids
    return -1


def request_4(): # show result of one bauer
    return -1


def cropwatch():
    return -1


def extract_waste_of_money():
    # 23: showBeg
    return 0


def debug():
    r = handle_request(cookies, RQ_DATA_0)
    text = r.text
    print(text)


def save_grants_to_csv(grant_dict, jahr):
    pd = pandas.DataFrame.from_dict(grant_dict, orient='index')
    pd.reset_index(drop=True, inplace=True)
    # Now you have a csv with columns and index:
    pd.to_csv(str(jahr) + "_grants" + ".csv")
    return True


def extract_grants(jahrtype, jahr):
    df = pandas.read_csv(str("91586_" + str(jahr) + ".csv"))
    #print(df)
    pd = df.loc[:, "pid"]
    pid_list = pd.values.tolist()
    result_dict = {}

    for pid in pid_list:
        grant = adv_parser_by_pid(pid, jahrtype)
        result_dict[pid] = grant

    save_grants_to_csv(result_dict, jahr)
    #print(list(map(list, pd.values)))
    # https://stackoverflow.com/questions/33157522/create-pandas-dataframe-from-dictionary-of-dictionaries

    return 0


def save_ids_to_csv(array_list, jahr):
    columns = ["pid"]
    pd = pandas.DataFrame(array_list, columns=columns)
    pd.drop_duplicates(["pid"], inplace=True)
    pd.reset_index(drop=True, inplace=True)
    # Now you have a csv with columns and index:
    pd.to_csv(str(str(jahr) + "_ids" + ".csv"))
    return True, array_list


def get_meta_data(response):
    count_start = response.find('<span>')
    raw_count = response[count_start + 22:count_start + 27]
    #print(raw_count)
    try:
        count = int(raw_count.strip())
    except ValueError:
        return 0, 0
    view_count_start = response.find('<input id="hCount" name="viewCount" type="hidden" value="', 0)
    view_count_end = response.find('/>', view_count_start)
    raw_v_count = response[view_count_start + 57:view_count_end - 1]
    # print(raw_v_count)
    view_count = int(raw_v_count)
    return view_count, count


def extract_ids(jahrtype, jahr):
    name_list = []

    for i in range(99999, 1, -1):
    #for i in range(96000, 95000, -1):
    #for i in range(95615, 95614, -1):
        factor = 5-len(str(i))
        plz = "0"*factor + str(i)
        print(plz)
        tmp_list = adv_from_plz(plz, jahrtype)
        name_list.extend(tmp_list)
        #sleep(3)
        #print(tmp_list)

    #print(name_list)
    err, _ = save_ids_to_csv(name_list, jahr)
    return 0


def handle_request(c, data):
    try:
        request = requests.post('https://www.agrar-fischerei-zahlungen.de/Suche', headers=H, cookies=c, data=data)
    except requests.exceptions.ConnectionError:
        print("Server to many connections error detected, sleeping!")
        sleep(3)
        request = requests.post('https://www.agrar-fischerei-zahlungen.de/Suche', headers=H, cookies=c, data=data)
    #print(request)
    return request


def adv_parser_ids(response, plz):
    tree = html.document_fromstring(response)
    pid_list = tree.xpath('/html/body/div[5]/div[3]/div/form[2]/table/tbody/tr[*]/th/button/@value')
    return pid_list


def amount_to_cent(amount):
    amount = amount[:-2]
    amounts = euro = amount[:-3]
    euro = int(euro.replace('.', ''))
    cent = int(amount[-2::])
    return euro*100 + cent


def adv_parser_by_pid(pid, yeartype):
    data_3[0] = ('jahr', yeartype)
    data_3[23] = ('showBeg', pid)

    grant = {"pid": pid, "Gesamt": ""}

    r = handle_request(cookies, data_3)
    tree = html.document_fromstring(r.text)
    metadata = tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/h2/text()')[0]  # name + ...
    raw_measures = tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/h3[*]/text()')  # name of grant
    raw_amounts = tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/p[*]/span/text()')  # amount of money
    raw_amounts = raw_amounts[:-2] # drop unrelevant rows

    #print(raw_amounts)

    measure_list = list(map(lambda x: x[2:], raw_measures))
    measure_list.append('Gesamt')
    #print(measure_list)
    #raw_sum = tree.xpath('/html/body/div[5]/div[3]/div/form/div[2]/p[8]/span[1]')

    #print(metadata)
    #print(measure_list)
    #print(raw_amounts)

    name, location = metadata.split('–')
    location = location[1:-3]
    plz, place = location.split(' ')
    #print(location)

    grant["name"] = name[:-1]
    grant["plz"] = int(plz)
    grant["place"] = place

    #print(measure_list)
    #print(raw_amounts)

    amounts = list(map(lambda x: amount_to_cent(x), raw_amounts))
    #print(amounts)

    for _, measure, amount in zip(amounts, measure_list, amounts):
        grant[measure] = amount

    # print(text)
    measure_list = []

    return grant






def test_parser():
    plz = "91586"
    jahr = "jahr"
    RQ_DATA_0[2] = ('plz', str(plz))
    # cookies['JESSIONID'] = str(jid+int(plz))
    # name_list = []
    i = 0
    r1 = handle_request(cookies, RQ_DATA_0)
    text = r1.text
    # print(text)
    view_count, count = get_meta_data(text)

    #rt = handle_request(cookies, data_change_to_50)

    if count == 0:
        return []

    print(plz)
    rq_data1[0] = ('jahr', jahr)
    rq_data1[3] = ('plz', str(plz))
    rq_data1[12] = ('viewCount', view_count)
    rq_data1[13] = ('viewCountBeg', count)
    rq_data1[18] = ('count', view_count)
    rq_data1[19] = ('countBeg', count)
    # print(rq_data1)
    #r2 = handle_request(cookies, rq_data1)
    rq_data2 = copy.deepcopy(rq_data1)
    # print(r1.text)
    # print(r2.text)
    #name_list = extract_columns(r2.text, plz)
    # rq_data2.append(('listNav', 'Vor'))

    # print(count)

    rq = handle_request(cookies, rq_data2)
    text = rq.text
    tmp_list = adv_parser_ids(text, plz)
    print(tmp_list)


def adv_from_plz(plz, jahr):
    RQ_DATA_0[2] = ('plz', str(plz))
    i = 1
    r1 = handle_request(cookies, RQ_DATA_0)
    text = r1.text
    view_count, count = get_meta_data(text)
    # print(view_count, count)

    if count == 0:
        return []

    # print(plz)
    rq_data1[0] = ('jahr', jahr)
    rq_data1[3] = ('plz', str(plz))
    rq_data1[12] = ('viewCount', view_count)
    rq_data1[13] = ('viewCountBeg', count)
    rq_data1[18] = ('count', view_count)
    rq_data1[19] = ('countBeg', count)

    rq_data2 = copy.deepcopy(rq_data1)

    rq = handle_request(cookies, rq_data2)
    name_list = adv_parser_ids(rq.text, plz)
    #i += 1

    while i < math.ceil(view_count/50):
        #rq_data1[9] = ('viewOffset', str(i*50))
        #rq_data1[15] = ('offset', str(i*50))
        rq_data2[22] = ('seite', str(i))

        #print(i+1)
        rq = handle_request(cookies, rq_data2)
        text = rq.text
        tmp_list = adv_parser_ids(text, plz)
        #print(tmp_list)
        if not tmp_list:
            break
        name_list.extend(tmp_list)
        i += 1

    return name_list




#test()
#debug()
#extract_by_id("0")
extract_ids("vorjahr", 2015)
extract_grants("vorjahr", 2015)
extract_ids("jahr", 2016)
extract_grants("jahr", 2016)

#test_parser()