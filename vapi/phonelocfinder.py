import os
import time
from colorama import Fore, Back, Style, init

countries = {
# A
"93" : "Afghanistan",
"355" : "Albania",
"213" : "Algeria",
"376" : "Andorra",
"1" : "US / Canada",
"54" : "Argentina",
"374" : "armen*a", 
"297" : "Aruba",
"61" : "Australia",
"43" : "Austria",
"994" : "Azerbaijan",
# B
"973" : "Bahrain",
"880" : "Bangladesh",
"375" : "Belarus",
"32" : "Belgium",
"501" : "Belize",
"229" : "Benin",
"975" : "Bhutan",
"591" : "Bolivia",
"387" : "Bosnia and Herzegovina",
"267" : "Botswana",
"55" : "Brazil",
"673" : "Brunei Darussalam",
"359" : "Bulgaria",
"226" : "Burkina Faso",
"257" : "Burundi",
# C
"855" : "Cambodia",
"237" : "Cameroon",
"238" : "Cape Verde",
"236" : "Central African Republic",
"235" : "Chad",
"56" : "Chile",
"86" : "China",
"61" : "Christmas Island",
"61" : "Cocos (Keeling) Islands",
"57" : "Colombia",
"269" : "Comoros",
"242" : "Congo (Brazzaville)",
"243" : "Congo (Kinshasa)",
"682" : "Cook Islands",
"506" : "Costa Rica",
"225" : "Cote D'Ivoire (Ivory Coast)",
"385" : "Crotia (Hrvatska",
"53" : "Cuba",
"357" : "Cyprus",
"420" : "Czech Republic",
"376" : "Cote D'Ivoire (Ivory Coast)",
"376" : "Cote D'Ivoire (Ivory Coast)",
# D
"45" : "Denmark",
"253" : "Djibouti",
# E
"593" : "Ecuador",
"20" : "Egypt",
"503" : "El Salvador",
"240" : "Equatorial Guinea",
"291" : "Eritrea",
"372" : "Estonia",
"251" : "Ethiopia",
# F
"500" : "Falkland Islands (Malvinas)",
"298" : "Faroe Islands",
"679" : "Fiji",
"358" : "Finland",
"33" : "France",
"594" : "French Guiana",
"689" : "French Polynesia",
# G
"241" : "Gabon",
"220" : "Gambia",
"995" : "Georgia",
"49" : "Germany",
"233" : "Ghana",
"350" : "Gibraltar",
"30" : "Greece",
"299" : "Greenland",
"590" : "Guadeloupe",
"502" : "Guatemala",
"224" : "Guinea",
"245" : "Guinea-Bissau",
"592" : "Guyana",
# H
"509" : "Haiti",
"379" : "Holy See (Vatican City State",
"504" : "Honduras",
"852" : "Hong Kong, SAR",
"36" : "Hungary",
# I
"354" : "Iceland",
"91" : "India",
"62" : "Indonesia",
"98" : "India, Islamic Republic of",
"964" : "Iraq",
"353" : "Ireland",
"972" : "Israel",
"39" : "Italy",
# J
"81" : "Japan",
"962" : "Jordan",
# K
"7" : "Kazakhstan",
"254" : "Kenya",
"686" : "Kiribati",
"850" : "Korea, Democratic People's Republic of (North)",
"82" : "Korea, Republic of (South)",
"965" : "Kuwait",
"996" : "Kyrgyzstan",
# L
"856" : "Laos",
"371" : "Latvia",
"961" : "Lebanon",
"266" : "Lesotho",
"231" : "Liberia",
"218" : "Libya",
"423" : "Liechtenstein",
"370" : "Lithuania",
"352" : "Luxembourg",
# M
"853" : "Macao",
"389" : "Macedonia, Republic of",
"261" : "Madagascar",
"265" : "Malawi",
"60" : "Malasyia",
"960" : "Maldives",
"223" : "Mali",
"356" : "Malta",
"692" : "Marshall Islands",
"596" : "Martinique",
"222" : "Mauritania",
"230" : "Mauritius",
"262" : "Mayotte",
"52" : "Mexico",
"691" : "Micronesia, Federated States of",
"373" : "Moldova",
"377" : "Monaco",
"976" : "Mongolia",
"382" : "Montenegro",
"212" : "Morocco and Western Sahara",
"258" : "Mozambique",
"95" : "Myanmar",
# N
"264" : "Namibia",
"674" : "Nauru",
"977" : "Nepal",
"31" : "Netherlands",
"599" : "Netherlands Antilles",
"687" : "New Caledonia",
"64" : "New Zealand",
"505" : "Nicaragua",
"227" : "Niger",
"234" : "Nigeria",
"683" : "Niue",
"672" : "Norfolk Island",
"47" : "Norway",
# O
"968" : "Oman",
# P
"92" : "Pakistan",
"680" : "Palau",
"970" : "Palestinian Territory",
"507" : "Panama",
"675" : "Papau New Guinea",
"595" : "Paraguay",
"51" : "Peru",
"63" : "Philippines",
"870" : "Pitcairn",
"48" : "Poland",
"351" : "Portugal",
# Q
"974" : "Qatar",
# R
"262" : "Reunion and Mayotte",
"40" : "Romania",
"7" : "Russian Federation",
"250" : "Rwanda",
"290" : "Saint Helena and also Tristan Da Cunha",
"508" : "Saint Pierre and Miquelon",
"685" : "Samoa",
"378" : "San Marino",
"239" : "Sao Tome and Principe",
"966" : "Saudi Arabia",
"221" : "Senegal",
"381" : "Serbia",
"248" : "Seychelles",
"232" : "Sierra Leone",
"65" : "Singapore",
"421" : "Slovakia",
"386" : "Slovenia",
"677" : "Solomon Islands",
"252" : "Somalia",
"27" : "South Africa",
"34" : "Spain",
"94" : "Sri Lanka",
"249" : "Sudan",
"597" : "Suriname",
"47" : "Svalbard and Jan Mayen Islands",
"268" : "Swaziland",
"46" : "Sweden",
"41" : "Switzerland",
"963" : "Syrian Arab Republic(Syria)",
# T
"886" : "Taiwan, Republic of China",
"992" : "Tajikistan",
"255" : "Tanzania, United Republic of",
"66" : "Thailand",
"670" : "Timor-Leste",
"228" : "Togo",
"690" : "Tokelau",
"676" : "Tonga",
"216" : "Tunisia",
"90" : "Turkey",
"993" : "Turkmenistan",
"688" : "Tuvalu",
# U
"256" : "Uganda",
"380" : "Ukraine",
"971" : "United Arab Emirates",
"44" : "United Kingdom",
"598" : "Uruguay",
"998" : "Uzbekistan",
# V
"678" : "Vanuatu",
"58" : "Venezuela",
"84" : "Viet Nam",
# W
"681" : "Wallis and Futuna Islands",
# Y
"967" : "Yemen",
# Z
"260" : "Zambia",
"263" : "Zimbabwe"
}

providers = {
    "Afghanistan" : {"70" : "AWCC", "71" : "AWCC", "72" : "Roshan", "73" : "Etisalat", "74" : "SALAAM (state owned)", "75" : "Afghan Telecom (state owned)", "24" : "MTN", "77" : "MTN", "78" : "Etisalat", "79" : "Roshan"},
    "Aland" : {"4570" : "Ålands Telekommunikation Ab", "4573" : "Ålands Telekommunikation Ab", "4575" : "Ålands Telekommunikation Ab"}, 
    "Albania" : {"67" : "ALBtelecom", "68" : "One.al", "69" : "Vodafone Albania"},
    "Algeria" : {"5" : "Ooredoo Algerie", "6" : "Mobilis-Algerie Telecom", "7" : "DJezzy Algerie"},
    "Angola" : {"91" : "MOVICEL - CDMA", "92" : "UNITEL - GSM", "93" : "UNITEL - GSM"},
    "armen*a" : {"55" : "Ucom", "95" : "Ucom", "41" : "Ucom", "44" : "Ucom", "77" : "VivaCell-MTS", "93" : "VivaCell-MTS", "94" : "VivaCell-MTS", "98" : "VivaCell-MTS", "91" : "Beeline armen*a", "99" : "Beeline armen*a", "43" : "Beeline armen*a", "97" : "does not exist"},
    "Austria" : {"650" : "T-Mobile Austria GmbH (telering)", "660" : "Hutchison 3G Austria GmbH (drei)", "664" : "mobilkom Austria AG (Mobilkom, A1)", "676" : "T-Mobile Austria GmbH (T-Mobile, formerly max)", "680" : "mobilkom Austria AG (Bob)", "677" : "HoT (T-Mobile, formerly max)", "681" : "YESSS! Telekommunikation GmbH", "688" : "Tele2 Mobil", "699" : "Hutchison 3G Austria GmbH (drei) formerly Orange Austria (Orange [formerly ONE], Yesss)"},
    "Azerbaijan" : {"41" : "Catel", "50" : "Azercell", "51" : "Azercell", "55" : "Bakcell", "70" : "Nar Mobile", "77" : "Nar Mobile", "99" : "Bakcell"},
    "Bahrain" : {"31" : "Royal Court", "322" : "Batelco", "33" : "Viva", "340" : "Viva", "341" : "Viva", "343" : "Viva", "344" : "Viva", "345" : "Viva", "353" : "Viva", "355" : "Viva", "36" : "Zain", "377" : "Zain", "383" : "Batelco", "384" : "Batelco", "388" : "Batelco", "39" : "Batelco", "663" : "Zain", "666" : "Zain", "669" : "Zain"},
    "Bangladesh" : {"13xx" : "GrameenPhone", "140x" : "Banglalink", "15xx" : "Teletalk", "16xx" : "Airtel", "17xx" : "GrameenPhone", "18xx" : "Robi", "19xx" : "Banglalink"},
    "Belarus" : {"291" : "A1", "292" : "MTS", "293" : "A1", "294" : "DIALLOG(not in use)", "295" : "MTS", "296" : "A1", "297" : "MTS", "298" : "MTS", "299" : "A1", "33" : "MTS", "44" : "A1"},
    "Belgium" : {"456" : "Mobile Vikings / JIM Mobile", "47x" : "Proximus", "48x" : "Telenet / Base", "49x" : "Orange Belgium"},
    "Belize" : {"6" : "Mobile Smart"},
    "Bosnia and Herzegovina" : {"60" : "BH Mobile", "69" : "BH Mobile", "62" : "BH Mobile", "63" : "Eronet", "64" : "Hallo", "65" : "m:tel", "66" : "m:tel"},
    "Botswana" : {"7" : "Mascom"},
    "Bulgaria" : {"48" : "Vivacom", "88" : "A1 Bulgaria", "89" : "Telenor (Bulgaria)"},
    "Burkina Faso" : {"70" : "Telmob", "71" : "Telmob", "72" : "Telmob", "74" : "Celtel", "75" : "Celtel", "77" : "Celtel", "78" : "Telecel", "79" : "Telecel"},
    "Cambodia" : {"92" : "Cellcard", "12" : "Cellcard", "11" : "Cellcard", "76" : "Cellcard", "77" : "Cellcard", "99" : "Cellcard", "10" : "Smart", "15" : "Smart", "16" : "Smart", "69" : "Smart", "70" : "Smart", "81" : "Smart", "86" : "Smart", "87" : "Smart", "93" : "Smart", "96" : "Smart", "98" : "Smart"},
    "Cameroon" : {"7" : "MTN", "9" : "Orange"},
    "Central African Republic" : "Telecel",
    "Chad" : {"66" : "Airtel", "63" : "Airtel", "65" : "Airtel", "99" : "Tigo", "95" : "Tigo", "93" : "Tigo", "90" : "Tigo", "77" : "Salamat"},
    "Chile" : {"9" : "Movistar / Claro / Entel / WOM / Virgin Mobile"},
    "China" : {"130" : "China Unicom", "131" : "China Unicom", "132" : "China Unicom", "133" : "China Telecom", "1349" : "China Telecom", "134" : "China Mobile", "135" : "China Mobile", "136" : "China Mobile", "137" : "China Mobile", "138" : "China Mobile", "139" : "China Mobile", "1400" : "China Unicom", "146" : "China Unicom", "1410" : "China Telecom", "1440" : "China Mobile", "148" : "China Mobile", "145" : "China Unicom", "149" : "China Telecom", "147" : "China Mobile", "155" : "China Unicom", "156" : "China Unicom", "153" : "China Telecom", "150" : "China Mobile", "151" : "China Mobile", "152" : "China Mobile", "157" : "China Mobile", "158" : "China Mobile", "159" : "China Mobile", "166" : "China Unicom", "167" : "China Unicom", "162" : "China Telecom", "165" : "China Mobile", "1704" : "China Unicom", "1707" : "China Unicom", "1708" : "China Unicom", "1709" : "China Unicom", "171" : "China Unicom", "175" : "China Unicom", "176" : "China Unicom", "1700" : "China Telecom", "1701" : "China Telecom", "1702" : "China Telecom", "173" : "China Telecom", "17400" : "China Telecom", "17401" : "China Telecom", " 17402" : "China Telecom", "17403" : "China Telecom", "17404" : "China Telecom", "17405" : "China Telecom", "177" : "China Telecom", "172" : "China Mobile", "178" : "China Mobile", "185" : "China Unicom", "186" : "China Unicom", "180" : "China Telecom", "181" : "China Telecom", "189" : "China Telecom", "182" : "China Mobile", "183" : "China Mobile", "184" : "China Mobile", "187" : "China Mobile", "188" : "China Mobile", "196" : "China Unicom", "190" : "China Telecom", "191" : "China Telecom", "193" : "China Telecom", "199" : "China Telecom", "195" : "China Mobile", "197" : "China Mobile", "198" : "China Mobile", "192" : "China Broadcast Network"},
    "Colombia" : {"30x" : "Tigo", "310" : "Claro", "311" : "Claro", "312" : "Claro", "313" : "Claro", "314" : "Claro", "315" : "Movistar", "316" : "Movistar", "317" : "Movistar", "318" : "Movistar", "319" : "Movistar", "32x" : "Claro", "350" : "Avantel", "351" : "Avantel"},
    "Congo (Kinshasa)" : {"81" : "Vodacom", "82" : "Vodacom", "84" : "Orange", "85" : "Orange", "90" : "Africell", "99" : "Airtel"},
    "Costa Rica" : {"6" : "Movistar", "7" : "Claro", "8" : "Instituto Costarricense de Electricidad"},
    "Croatia" : {"91" : "Vipnet", "92" : "Tomato", "95" : "Tele2", "97" : "bonbon", "98" : "T-Mobile", "99" : "T-Mobile"},
    "Cuba" : {"5" : "ETESCA"},
    "Cyprus" : {"94" : "LemonTel", "95" : "PrimeTel", "96" : "MTN", "97" : "Cytamobile-Vodafone", "99" : "Cytamobile-Vodafone"},
    "Czech Republic" : {"601" : "Telefonica O2", "602" : "Telefonica O2", "603" : "T-Mobile", "604" : "T-Mobile", "605" : "T-Mobile", "606" : "Telefonica O2", "607" : "Telefonica O2", "608" : "Vodafone", "702" : "Telefonica O2", "72x" : "Telefonica O2", "73x" : "T-Mobile", "77x" : "Vodafone", "730" : "None", "790" : "U:fon"},
    "Denmark" : {"2x" : "TDC", "50" : "Telenor"},
    "Egypt" : {"10" : "Vodafone", "11" : "Etisalat", "12" : "Orange Egypt", "15" : "WE Egypt"},
    "Estonia" : {"51" : "Telia Eesti AS", "53" : "Telia Eesti AS", "54" : "Multiple", "55" : "Tele2 Eesti AS", "56" : "Elisa Eesti AS", "57" : "Multiple", "58" : "Telia Eesti AS", "59" : "Telia Eesti AS", "50" : "Telia Eesti AS", "510" : "Telia Eesti AS", "511" : "Telia Eesti AS", "512" : "Telia Eesti AS", "513" : "Telia Eesti AS", "514" : "Telia Eesti AS", "515" : "Telia Eesti AS", "516" : "Telia Eesti AS", "517" : "Telia Eesti AS", "518" : "Telia Eesti AS", "5195" : "Telia Eesti AS", "52" : "Telia Eesti AS", "550" : "Tele2 Eesti AS", "551" : "Tele2 Eesti AS", "552" : "Tele2 Eesti AS", "553" : "Tele2 Eesti AS", "554" : "Tele2 Eesti AS", "557" : "Tele2 Eesti AS", "558" : "Tele2 Eesti AS", "5640" : "Elisa Ees", "5641" : "Elisa Eesti AS", "5642" : "Elisa Eesti AS", "5643" : "Elisa Eesti AS", "5644" : "Elisa Eesti AS", "5651" : "Elisa Eesti AS", "5652" : "Elisa Eesti AS", "5653" : "Elias Eesti AS", "5654" : "Elisa Eesti AS", "5655" : "Elisa Eesti AS", "5658" : "Elisa Eesti AS", "5659" : "Elisa Eesti AS"},
    "Ethiopia" : {"9x" : "Ethio Telecom"},
    "Fiji" : {"3" : "Telecom", "7" : "Digicel", "9" : "Vodafone"},
    "Finland" : {"40" : "Telia Finland Oyj", "41" : "DNA Oyj", "42" : "Telia Finland Oyj", "44" : "DNA Oyj", "46" : "Elisa Oyj", "50" : "Elisa Oyj"},
    "Georgia" : {"544" : "Aquafon", "514" : "Silknet / Geocell", "551" : "MagtiCom", "555" : "Silknet / Geocell", "557" : "Silknet / Geocell", "558" : "Silknet / Geocell", "568" : "Beeline", "570" : "Silknet / Geocell", "571" : "Beeline", "574" : "Beeline", "577" : "Silknet / Geocell", "578" : "Silknet / Geocell", "579" : "Beeline", "591" : "MagtiCom", "592" : "Beeline", "593" : "Silknet / Geocell", "595" : "MagtiCom", "596" : "Magticom", "597" : "Beeline", "598" : "MagtiCom", "599" : "MagtiCom"},
    "Germany" : {"151x" : "T-Mobile", "152x" : "Vodafone D2", "155x" : "E-Plus", "157x" : "E-Plus", "159x" : "O2 Germany", "160" : "T-Mobile", "162" : "Vodafone D2", "163" : "E-Plus", "170" : "T-Mobile", "171" : "T-Mobile", "172" : "Vodafone D2", "173" : "Vodafone D2", "174" : "Vodafone D2", "175" : "T-Mobile", "176" : "O2 Germany", "177" : "E-Plus", "178" : "E-Plus", "179" : "O2 Germany"},
    "Ghana" : {"20" : "Vodafone", "50" : "Vodafone", "23" : "Glo Mobile", "24" : "MTN", "54" : "MTN", "55" : "MTN", "59" : "MTN", "26" : "Airtel (Zain)", "56" : "Airtel (Zain)", "27" : "Tigo", "57" : "Tigo", "28" : "Kasapa"},
    "Greece" : {"2" : "Landline", "690" : "WIND", "693" : "WIND", "694" : "Vodafone", "695" : "Vodafone", "697" : "Cosmote", "698" : "Cosmote", "699" : "WIND"},
    "Guatemala" : "Comcel Mobile",
    "Haiti" : {"34" : "Comcel (Voila)", "39" : "Comcel (Voila)", "35" : "Haitel", "36" : "Digicel", "37" : "Digicel", "38" : "Digiccel"},
    "Honduras" : {"3" : "Claro", "7" : "Hondutel", "8" : "Digicel", "9" : "Tigo"},
    "Hungary" : {"20" : "Telenor HU", "30" : "Telekom HU", "31" : "UPC Mobile", "38" : "GSM-R", "50" : "DIGI.MOBILE HU", "70" : "Vodafone HU"},
    "India" : {"6xx" : "Reliance Jio", "7xx" : "Aircel / Airtel", "8xx" : "Aircel / Airtel", "90x" : "Various GSM", "91x" : "Varius GSM", "92x" : "Tata Indicom", "93x" : "Reliance", "94x" : "BSNL", "95x" : "Airtel / Aircel / Vodafone / Reliance", "96x" : "Airtel / Aircel / Vodafone / Reliance", "97x" : "Airtel / Aircel / Vodafone / Reliance", "98x" : "Airtel / Aircel / Vodafone / Reliance", "99x" : "Airtel / Aircel / Vodafone / Reliance"},
    "Indonesia" : {"811" : "Telkomsel", "812" : "Telkomsel", "813" : "Telkomsel", "814" : "Indosat", "815" : "Indosat", "816" : "Indosat", "817" : "XL", "818" : "XL", "819" : "XL", "838" : "AXIS", "852" : "Telkomsel", "853" : "Telkokmsel", "855" : "Indosat", "856" : "Indosat", "858" : "Indosat", "859" : "XL", "878" : "XL", "896" : "Hutchison", "897" : "Hutchison", "898" : "Hutchison", "899" : "Hutchison"},
    "Iran" : {"901" : "MTN Irancell", "902" : "MTN Irancell", "903" : "MTN Irancell", "91x" : "Hamrah Aval", "920" : "RighTel", "921" : "RighTel", "922" : "RighTel", "930" : "MTN Irancell", "931" : "MTCE", "932" : "Taliya", "933" : "MTN Irancell", "934" : "Kish-TCI", "935" : "MTN Irancell", "936" : "MTN Irancell", "937" : "MTN Irancell", "938" : "MTN Irancell", "939" : "MTN Irancell", "990" : "Hamrah Aval", "9999" : "SamanTel"},
    "Iraq" : {"73x" : "Korek Telecom", "74x" : "Itisaluna and Kalemat", "75x" : "Korek Telecom", "76x" : "Mobitel (Iraq-Kurdistan) and Moutiny", "77x" : "AsiaCell", "78x" : "Zain Iraq", "79x" : "Zain Iraq"},
    "Ireland" : {"83" : "Three", "85" : "eir", "86" : "Three", "87" : "Vodafone", "89" : "Tesco"},
    "Israel" : {"50" : "Pelephone / Walla Mobile / YouPhone", "52" : "Cellcom / Mvoice", "53" : "Hot Mobile", "54" : "Partner / 012 Mobile", "5522" : "Home Cellular", "5523" : "Home Cellular", "556" : "Rami Levy Hashikma Marketing", "5570" : "Cellact", "5571" : "Cellact", "558" : "Pelephone / Walla Mobile / YouPhone", "559" : "019 Telecom", "58" : "Golan Telecom"},
    "Italy" : {"310" : "Elsacom", "31100" : "Telespazio", "31101" : "Telespazio", "31105" : "Spal Telecommunications", "313" : "RFI Rete Ferroviaria Italiana", "319" : "Intermatica", "320" : "WIND", "322" : "WIND", "323" : "WIND", "324" : "WIND", "327" : "WIND", "328" : "WIND", "329" : "WIND", "330" : "TIM", "331" : "TIM", "333" : "TIM", "334" : "TIM", "335" : "TIM", "366" : "TIM", "337" : "TIM", "338" : "TIM", "339" : "TIM", "340" : "Vodafone", "341" : "Vodafone", "342" : "Vodafone", "342" : "Vodafone", "343" : "Vodafone", "344" : "Vodafone", "345" : "Vodafone", "346" : "Vodafone", "347" : "Vodafone", "348" : "Vodafone", "349" : "Vodafone", "3505" : "MVNO Noverca", "3510" : "MVNO Lycamobile", "3512" : "MVNO Lycamobile", "360" : "TIM", "361" : "TIM", "362" : "TIM", "363" : "TIM", "366" : "TIM", "368" : "TIM", "370" : "MVNO", "3710" : "MVNO", "3711" : "MVNO", "373" : "HVNO", "377" : "Vodafone", "380" : "WIND", "381" : "MVNO", "382" : "MVNO", "383" : "Vodafone", "385" : "Telecom Italia", "388" : "WIND", "389" : "WIND", "390" : "H3G", "391" : "H3G", "392" : "H3G", "397" : "H3G"},
    "Jordan" : {"77" : "Orange", "79" : "Zain Jordan", "78" : "Umniah"},
    "Kazakhstan" : {"700" : "Altel", "708" : "Altel", "701" : "Kcell", "702" : "Kcell", "775" : "Kcell", "778" : "Kcell", "705" : "Beeline", "771" : "Beeline", "776" : "Beeline", "777" : "Beeline", "707" : "Tele2", "747" : "Tele2"},
    "Kenya" : {"10x" : "Airtel", "11x" : "Safaricom", "70x" : "Safaricom", "71x" : "Safaricom", "72x" : "Safaricom", "73x" : "Airtel", "74x" : "Jamii", "75x" : "Yu", "763" : "Equitel", "77x" : "Orange", "78x" : "Airtel"},
    "Kosovo" : {"44" : "Post and Telecom of Kosovo", "45" : "Z Mobile", "49" : "IPKO"},
    "Kuwait" : {"5" : "Viva", "6" : "Ooredoo Kuwait", "9" : "Zain"},
    "Luxembourg" : {"621" : "LuxGSM", "628" : "LuxGSM", "661" : "Orange", "668" : "Orange", "691" : "Tango Mobile", "698" : "Tango Mobile"},
    "Malaysia" : {"10" : "DIGI", "11" : "Maxis", "12" : "Maxis", "13" : "Celcom", "14" : "DIGI", "16" : "DIGI", "17" : "Maxis", "18" : "U Mobile", "19" : "Celcom"},
    "Maldives" : {"7" : "Dhiraagu", "9" : "Ooredoo"},
    "Mali" : {"6" : "Malitel", "7" : "Orange Mali"},
    "Malta" : {"77" : "Melita Mobile Ltd", "79" : "Go Mobile Ltd", "98" : "Red Touch Phone", "99" : "Epic Malta"},
    "Moldova" : {"60" : "Orange", "65" : "Eventis", "67" : "Unite", "68" : "Orange", "69" : "Orange", "78" : "Moldcell", "79" : "Moldcell"},
    "Mongolia" : {"70" : "Mongolian Telecom Company", "88" : "Unitel Corporation", "89" : "Unitel Corporation", "91" : "Skytel", "93" : "G-Mobile", "94" : "Mobicom Corporation", "95" : "Mobicom Corporation", "96" : "Skytel", "98" : "G-Mobile", "99" : "Mobicom Corporation"},
    "Montenegro" : {"60" : "MTEL CG", "63" : "Telenor Montenegro", "66" : "T-Mobile", "67" : "T-Mobile", "68" : "MTEL CG", "69" : "Telenor Montenegro"},
    "Mozambique" : {"82" : "Tmcel", "83" : "Tmcel", "84" : "Vodacom", "85" : "Vodacom", "86" : "Movitel", "87" : "Movitel"},
    "Myanmar" : {"92" : "MPT", "925" : "MPT", "926" : "MPT", "943" : "MPT", "94" : "MPT", "944" : "MPT", "95" : "MPT", "96" : "MPT", "973" : "MPT"," 991" : "MPT", "93" : "MEC", "996" : "Ooredoo Myanmar", "997" : "Ooredoo Myanmar", "977" : "Telenor Myanmar", "978" : "Telenor Myanmar", "979" : "Telenor Myanmar"},
    "Namibia" : {"60" : "Switch", "81" : "MTC", "85" : "Leo"},
    "Nepal" : {"98" : "Ncell"},
    "New Zeland" : {"20" : "Orcon", "21" : "Vodafone", "22" : "2degrees", "27" : "Spark New Zealand", "280" : "Compass Communications", "28" : "CallPlus", "283" : "Teletraders MVNO", "29" : "Telstra Clear", "24" : "Unused", "25" : "Unused"},
    "Nigeria" : {"804" : "ntel", "805" : "glo", "803" : "mtn", "802" : "airtel", "809" : "etisalat"},
    "North Macedonia" : {"70" : "Makedonski Telekom", "71" : "Makedonski Telekom", "72" : "Makendonski Telekom", "73" : "Green Mobile MK", "74" : "Telekabel", "75" : "A1 Macedonia", "76" : "A1 Macedonia", "77" : "A1 Macedonia", "78" : "A1 Macedonia"},
    "Oman" : {"91" : "Oman Mobile", "92" : "Oman Mobile", "93" : "Nawras", "94" : "Nawras", "95" : "Nawras", "96" : "Nawras", "97" : "Nawras", "98" : "Friendy", "99" : "Oman Mobile"},
    "Pakistan" : {"30x" : "Mobilink", "31x" : "Zong", "32x" : "Warid Pakistan", "33x" : "Ufone", "34x" : "Telenor"},
    "Palestinian Territory" : {"56" : "Wataniya", "59" : "Jawwal"},
    "Paraguay" : {"961" : "VOX", "963" : "VOX", "971" : "Personal", "972" : "Personal", "973" : "Personal", "975" : "Personal", "981" : "Tigo", "982" : "Tigo", "983" : "Tigo", "984" : "Tigo", "985" : "Tigo", "991" : "Claro", "992" : "Claro", "993" : "Claro", "995" : "Claro"},
    "Philippines" : {"973" : "Express Telecom", "974" : "Express Telecom", "905" : "Globe Telecom / Touch Mobile", "906" : "Globe Telecom / Touch Mobile", "977" : "Globe Telecom / Touch Mobile", "915" : "Globe Telecom / Touch Mobile", "916" : "Globe Telecom / Touch Mobile", "926" : "Globe Telecom / Touch Mobile", "927" : "Globe Telecom / Touch Mobile", "935" : "Globe Telecom / Touch Mobile", "936" : "Globe Telecom / Touch Mobile", "937" : "Globe Telecom / Touch Mobile", "996" : "Globe Telecom / Touch Mobile", "997" : "Globe Telecom / Touch Mobile", "917" : "Globe Telecom", "979" : "Next Mobile", "920" : "Smart Communications", "930" : "Smart Communications", "938" : "Smart Communications", "939" : "Smart Communications", "907" : "Smart Communications", "908" : "Smart Communications", "909" : "Smart Communications", "910" : "Smart Communications", "912" : "Smart Communications", "919" : "Smart Communications", "921" : "Smart Communications", "928" : "Smart Communications", "929" : "Smart Communications", "947" : "Smart Communications", "948" : "Smart Communications", "949" : "Smart Communications", "918" : "Smart Communications", "999" : "Smart Communications", "922" : "Sun Cellular", "923" : "Sun Cellular", "932" : "Sun Cellular", "933" : "Sun Cellular", "942" : "Sun Cellular", "943" : "Sun Cellular"},
    "Portugal" : {"91" : "Vodafone", "921" : "Vodafone", "922" : "Phone-lx", "924" : "MEO", "925" : "MEO", "926" : "MEO", "927" : "MEO", "9290" : "NOS", "9291" : "NOS", "9292" : "NOS", "9293" : "NOS", "9294" : "NOS", "93" : "NOS", "96" : "MEO"},
    "Qatar" : {"33" : "Qtel", "55" : "Qtel", "66" : "Qtel", "77" : "Vodafone"},
    "Romania" : {"711" : "Telekom Romania", "72x" : "Vodafone Romania", "73x" : "Vodafone Romania", "74x" : "Orange Romania", "75x" : "Orange Romania", "76x" : "Telekom Romania", "77x" : "DIGIMobil", "78x" : "Zapp Mobile"},
    "Russian Federation" : {"901" : "Skylink (Russia)", "902" : "Tele2 (Russia)", "903" : "Beeline", "904" : "Tele2 (Russia)", "905" : "Beeline", "906" : "Beeline", "908" : "Tele2 (Russia)", "909" : "Beeline", "91x" : "MTS", "92x" : "Megafon", "93x" : "Megafon", "950" : "Tele2 (Russia)", "951" : "MTS", "952" : "Tele2 (Russia)", "953" : "Tele2 (Russia)", "96x" : "Beeline", "980" : "Beeline", "983" : "Beeline", "986" : "Beeline"},
    "Saudi Arabia" : {"50" : "STC", "51" : "Bravo", "53" : "STC", "54" : "mobily", "55" : "STC", "56" : "mobily", "57" : "Bravo", "58" : "Zain", "59" : "Zain"},
    "Serbia" : {"60" : "Vip mobile", "61" : "Vip mobile", "62" : "Telenor Serbia", "63" : "Telenor Serbia", "64" : "mt:s", "65" : "mt:s", "66" : "mt:s", "677" : "Globaltel", "68" : "Vip mobile", "69" : "Telenor Serbia"},
    "Slovakia" : {"901" : "T-Mobile", "902" : "T-Mobile", "903" : "T-Mobile", "904" : "T-Mobile", "905" : "Orange", "906" : "Orange", "907" : "Orange", "908" : "Orange", "910" : "T-Mobile", "911" : "T-Mobile", "912" : "T-Mobile", "914" : "T-Mobile", "915" : "Orange", "916" : "Orange", "917" : "Orange", "918" : "Orange", "940" : "O2", "944" : "O2", "948" : "O2", "949" : "O2", "950" : "SWAN", "951" : "SWAN"},
    "Slovenia" : {"30" : "Si.mobil", "31" : "Mobitel", "40" : "Si.mobil", "41" : "Mobitel", "49" : "Mobitel", "51" : "Mobitel", "64" : "T-2", "70" : "Telemach Mobile", "71" : "Mobitel"},
    "South Africa" : {"60" : "MTN", "710" : "MTN", "711" : "Vodacom", "712" : "Vodacom", "713" : "Vodacom", "715" : "Vodacom", "716" : "Vodacom", "717" : "MTN", "718" : "MTN", "719" : "MTN", "72" : "Vodacom", "73" : "MTN", "74" : "Cell C", "741" : "Virgin Mobile", "76" : "Vodacom", "78" : "MTN", "79" : "Vodacom", "811" : "Telko" , "812" : "Telkom", "813" : "Telkom", "814" : "Telkom", "82" : "Vodacom", "83" : "MTN", "84" : "Cell C"},
    "South Korea" : "SK Telecom / KT / LG U+",
    "Sri Lanka" : {"70" : "Mobitel", "71" : "Mobitel", "72" : "Hutch", "74" : "Dialog", "75" : "Airtel", "76" : "Dialog", "77" : "Dialog", "78" : "Hutch"},
    "Sweden" : {"7300" : "Telia Sonera Sv AB", "7301" : "Wireless Maingate N", "7302" : "Telia Sonera Sv AB", "7303" : "Telia Sonera Sv AB", "7304" : "Telia Sonera Sv AB", "7305" : "Telia Sonera Sv AB", "7306" : "Telia Sonera Sv AB", "7307" : "Telia Sonera Sv AB", "7308" : "Telia Sonera Sv AB", "7309" : "Telia Sonera Sv AB", "7310" : "Timepiece Servicos", "7311" : "Wireless Maigate N", "7312" : "Ledig", "7313" : "Wireless Maingate N", "7314" : "Campuz Mobile AB", "7315" : "Campuz Mobile AB", "7316" : "Abbla Mobile Sv AB", "73170" : "Netnet AS", "73171" : "Ledig", "73172" : "Ledig", "73173" : "Ledig", "73174" : "Ledig", "73175" : "Ledig", "73175" : "Ledig", "73176" : "Ledig", "73177" : "Ledig", "73178" : "Ledig", "73179" : "Ledig", "7318" : "ACN Communications S", "7319" : "Terraflex Europe LPP", "7320" : "Telenor Sverige AB", "7321" : "Optimal Telecom Sver", "7322" : "Optimal Telecom Sver", "7323" : "Telenor Sverige AB", "7324" : "Telenor Mobile Sv", "7325" : "Telenor Mobile Sv", "7326" : "Telenor Mobile Sv", "7327" : "Ventelo Sverige AB", "7328" : "Chess AB", "7329" : "Telogic Aps", "733" : "Telenor Sverige AB", "7340" : "Telenor Sverige AB", "7341" : "Telenor Sverige AB", "7342" : "Telenor Sverige AB", "7343" : "Telenor Sverige AB", "7344" : "Telenor Sverige AB", "73450" : "Telogic ApS", "73451" : "Telogic ApS", "73452" : "Telogic ApS", "73453" : "Telogic ApS", "73454" : "Telogic ApS", "73455" : "Ledig", "73456" : "Intelligent Appl. AB", "73457" : "Ledig", "73458" : "Ledig", "73459" : "Ledig", "7346" : "Ledig", "7347" : "Ledig", "7348" : "Ledig", "7349" : "Ledig", "7350" : "Hi3G Access AB", "7351" : "Hi3G Access AB", "7352" : "Hi3G Access AB", "7353" : "Hi3G Access AB", "7354" : "Hi3G Access AB", "7355" : "Tele2 Sverige AB", "7356" : "Tele2 Sverige AB", "7357" : "Tele2 Sverige AB", "7358" : "Tele2 Sverige AB", "7359" : "Tele2 Sverige AB", "736" : "Tele2 Sverige AB", "7370" : "Tele2 Sverige AB", "7371" : "Tele2 Sverige AB", "7372" : "Tele2 Sverige AB", "7373" : "Tele2 Sverige AB", "7374" : "Tele2 Sverige AB", "7375" : "Tele2 Sverige AB", "7376" : "Tele2 Sverige AB", "7377" : "Tele2 Sverige AB", "7378" : "Tele2 Sverige AB", "7379" : "Tele2 Sverige AB", "7380" : "TeliaSonera Sv AB", "7381" : "TeliaSonera Sv AB", "7382" : "TeliaSonera Sv AB", "7383" : "TeliaSonera Sv AB", "7384" : "TeliaSonera Sv AB", "7385" : "Telenor Sverige AB", "7386" : "Lebara Ltd", "7387" : "Ledig", "7388" : "Newphon SP AB", "7389" : "Ledig", "739" : "Tele2 Sverige AB"},
    "Switzerland" : {"75" : "Swisscom", "76" : "Sunrise", "77" : "Swisscom", "78" : "Salt Mobile", "79" : "Swisscom"},
    "Syria" : {"93" : "Syriatel", "98" : "Syriatel", "99" : "Syriatel", "94" : "MTN", "95" : "MTN", "96" : "MTN"},
    "Tajikistan" : {"90" : "MLT GSM/3G", "910" : "Beeline-TJ GSM/3G", "911" : "Beeline-TJ GSM/3G", "912" : "Beeline-TJ GSM/3G", "913" : "Beeline-TJ GSM/3G", "914" : "Beeline-TJ GSM/3G", "915" : "Beeline-TJ GSM/3G", "916" : "Beeline-TJ GSM/3G", "917" : "Beeline-TJ GSM/3G", "918" : "Babilon-Mobile GSM/3G", "919" : "Beeline-TJ GSM/3G", "92" : "TCell-Somoncom GSM/3G", "93" : "TCell-Tajikistan GSM/3G", "95" : "TK-Mobile CDMA", "96" : "M.Teko CDMA", "97" : "Skytel CDMA", "98" : "Babilon-Mobile GSM/3G"},
    "Tanzania" : {"62x" : "Halotel", "65x" : "TiGO", "67x" : "TiGO", "71x" : "TiGO", "66x" : "Smile", "68x" : "Airtel Tanzania", "69x" : "Airtel Tanzania", "78x" : "Airtel Tanzania", "73x" : "TTCL", "74x" : "Vodacom Tanzania", "75x" : "Vodacom Tanzania", "76x" : "Vodacom Tanzania", "77x" : "ZanTel"},
    "Togo" : {"90" : "Togocel", "91" : "Togocel", "92" : "Togocel", "97" : "Moov Togo", "98" : "Moov Togo", "99" : "Moov Togo"},
    "Trinidad and Tobago" : {"868" : "Trinidad and Tobago Cellular"},
    "Tunisia" : {"2" : "Tunisia Mobile Ooredoo", "3" : "Tunisia Mobile Orange", "4" : "Tunisia Mobile Tuntel", "5" : "Tunisia Mobile Orange", "9" : "Tunisia Mobile Tuntel"},
    "Turkey" : {"50" : "Turk Telecom", "53" : "Turkcell", "54" : "Vodafone Turkey", "55" : "Turk Telecom"},
    "Turkmenistan" : {"65" : "TMCELL", "66" : "BCTI", "67" : "BTCI"},
    "Uganda" : {"720" : "Smile Communications", "730" : "K2 Telecom", "740" : "Sure Telcom Uganda", "741" : "Sure Telcom Uganda", "742" : "Sure Telcom Uganda", "743" : "Sure Telcom Uganda", "744" : "Sure Telcom Uganda", "750" : "Airtel Uganda Limited", "751" : "Airtel Uganda Limited", "752" : "Airtel Uganda Limited", "753" : "Airtel Uganda Limited", "754" : "Airtel Uganda Limited", "755" : "Airtel Uganda Limited", "756" : "Airtel Uganda Limited", "757" : "Airtel Uganda Limited", "758" : "Airtel Uganda Limited", "759" : "Airtel Uganda Limited", "760" : "iTel Limited", "761" : "iTel Limited", "762" : "iTel Limited", "763" : "iTel Limited", "764" : "iTel Limited", "770" : "MTN Uganda Limited", "771" : "MTN Uganda Limited", "772" : "MTN Uganda Limited", "773" : "MTN Uganda Limited", "774" : "MTN Uganda Limited", "775" : "MTN Uganda Limited", "776" : "MTN Uganda Limited", "777" : "MTN Uganda Limited", "778" : "MTN Uganda Limited", "779" : "MTN Uganda Limited", "780" : "MTN Uganda Limited", "781" : "MTN Uganda Limited", "782" : "MTN Uganda Limited", "783" : "MTN Uganda Limited", "784" : "MTN Uganda Limited", "785" : "MTN Uganda Limited", "786" : "MTN Uganda Limited", "787" : "MTN Uganda Limited", "788" : "MTN Uganda Limited", "789" : "MTN Uganda Limited", "790" : "Orange Uganda Limited", "791" : "Orange Uganda Limited", "792" : "Orange Uganda Limited", "793" : "Orange Uganda Limited", "794" : "Orange Uganda Limited"},
    "Ukraine" : {"50" : "Vodafone Ukraine", "63" : "Lifecell (Astelit)", "66" : "Vodafone Ukraine", "67" : "Kyivstar", "73" : "Lifecell (Astelit)", "91" : "UTEL", "92" : "Peoplenet", "93" : "Lifecell (Astelit)", "94" : "Intertelecom", "95" : "Vodafone Ukraine", "96" : "Kyivstar", "97" : "Kyivstar", "98" : "Kyivstar", "99" : "Vodafone Ukraine"},
    "United Arab Emirates" : {"50" : "Etisalat", "52" : "Du", "54" : "Etisalat", "55" : "Du", "56" : "Etisalat", "58" : "Du"},
    "United Kingdom" : {"74xx" : "Hutchison 3G UK", "7624" : "Isle of Man"},
    "Uruguay" : {"91" : "Ancel", "93" : "Movistar", "94" : "Movistar", "95" : "Movistar", "96" : "Claro", "97" : "Claro", "98" : "Ancel", "99" : "Ancel"},
    "Uzbekistan" : {"90" : "Beeline", "91" : "Beeline", "93" : "UCell", "94" : "Ucell", "97" : "UMS", "33" : "Humans.uz"},
    "Venezuela" : {"412" : "Digitel GSM", "414" : "Movistar", "416" : "Movilnet", "424" : "Movistar", "426" : "Movilnet"},
    "Yemen" : {"70" : "Y (Yemen)", "71" : "Sabafon", "73" : "MTN", "77" : "Yemen Mobile"},
    "Zimbabwe" : {"71" : "Net One", "73" : "Telecel Zimbabwe", "77" : "Econet Zimbabwe"}
}


def plookup(ccode,pcode,rempart):
    phone = str(ccode)+str(pcode)+str(rempart)
    #checking all elements not to be letter
    for ch in ccode:
        checkthiskidisstupidornot1 = ch.isalpha()
        if checkthiskidisstupidornot1 == True:
            # This is ELON MUSK
            print(Fore.CYAN + "Wrong...Not Letters, only digits :)")
            exit()
    checkthiskidisstupidornot2 = '+' in ccode
    if checkthiskidisstupidornot2 == True:
        # This is ElOn MuSk
        print(Fore.CYAN + "Wrong...Not Letters, only digits :)")
        exit()
    country = countries[str(ccode)]
    checkthiskidisstupidornot31 = ' ' in rempart
    if checkthiskidisstupidornot31 == True:
        # This is ElOn MuSk
        print(Fore.CYAN + "Wrong...No Space, only digits :)")
        exit()
    checkthiskidisstupidornot3 = ' ' in pcode
    if checkthiskidisstupidornot3 == True:
        # This is ElOn MuSk
        print(Fore.CYAN + "Wrong...No Space, only digits :)")
        exit()
    for ch in pcode:
        checkthiskidisstupidornot4 = ch.isalpha()
        if checkthiskidisstupidornot4 == True:
            # This is ELON MUSK
            print(Fore.CYAN + "Wrong...Not Letters, only digits :)")
            exit()
    provider = "None"

    ruseriousrnnow = country not in providers

    cforp = "Bruh"
    if ruseriousrnnow == False:
        cforp = providers[country]
    wtfisthis = type(cforp) is str
    if wtfisthis == True:
        provider = cforp
    for k, v in cforp.items():
        #print(v)
        if k == pcode:
            provider = v
            break
        else:
            isx = 'x' in k
            if isx == True:
                if len(k) != len(pcode):
                    continue
                else:
                    i = 0
                    j = 0
                    cnt = 0
                    while k[i] != 'x' and k[i] == pcode[j]:
                        cnt += 1
                        i += 1
                        j += 1
                    if cnt >= 1:
                        provider = v
                        break
    print("For results : +" + Fore.RED + ccode + pcode + rempart)
    print(Fore.CYAN + "Country : " + Fore.GREEN + country)
    print(Fore.CYAN + "Provider : " + Fore.GREEN + provider)

    #Coded by Shahin
